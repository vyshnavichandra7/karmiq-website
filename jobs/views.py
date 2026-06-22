from django.shortcuts import render, redirect
from .models import Application, Job
from users.models import User
import json
import urllib.request
import urllib.parse
from django.contrib import messages
from users.decorators import custom_login_required
# 📍 Map coordinates
def get_coordinates(location):
    mapping = {
        "kukatpally": (17.4948, 78.3996),
        "ameerpet": (17.4375, 78.4483),
        "gachibowli": (17.4401, 78.3489),
        "banjara hills": (17.4126, 78.4482),
        "secunderabad": (17.4399, 78.4983),
    }

    loc_lower = location.lower()
    if loc_lower in mapping:
        return mapping[loc_lower]

    try:
        encoded_loc = urllib.parse.quote(location)
        url = f"https://nominatim.openstreetmap.org/search?q={encoded_loc}&format=json&limit=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'KarmiqApp/1.0'})
        with urllib.request.urlopen(req, timeout=3) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
    except Exception:
        pass

    return (17.3850, 78.4867)


# 🏗️ Contractor posts job
@custom_login_required
def post_job(request):
    user_id = request.session.get('user_id')

    if request.method == "POST":
        lat, lng = get_coordinates(request.POST['location'])

        Job.objects.create(
            title=request.POST['title'],
            salary=request.POST['salary'],
            location=request.POST['location'],
            contractor_id=user_id,
            is_urgent='is_urgent' in request.POST,
            max_workers=request.POST['max_workers'],
            latitude=lat,
            longitude=lng,
            timing=request.POST.get('timing'),
            job_date=request.POST.get('job_date') or None
        )
        return redirect('home')

    return render(request, 'post_job.html')


# 👷 Worker views jobs
@custom_login_required
def job_list(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    jobs = Job.objects.all()

    return render(request, 'jobs.html', {
        'jobs': jobs,
        'user': user
    })


# 📩 Worker applies for job
@custom_login_required
def apply_job(request, job_id):
    user_id = request.session.get('user_id')

    job = Job.objects.get(id=job_id)

    total_applied = Application.objects.filter(job=job).count()

    # limit check
    if total_applied >= job.max_workers:
        return redirect('jobs')

    # prevent duplicate apply
    already_applied = Application.objects.filter(
        job_id=job_id,
        worker_id=user_id
    ).exists()

    if not already_applied:
        Application.objects.create(
            job_id=job_id,
            worker_id=user_id
        )

    return redirect('jobs')


# 👥 Contractor views applicants
@custom_login_required
def view_applicants(request, job_id):
    applications = Application.objects.filter(job_id=job_id)
    return render(request, 'applicants.html', {'applications': applications})


# ✅ Hire worker
@custom_login_required
def hire_worker(request, app_id):
    application = Application.objects.get(id=app_id)
    application.status = "hired"
    application.save()

    return redirect('view_applicants', job_id=application.job.id)


# ⭐ Rate worker
@custom_login_required
def rate_worker(request, app_id):
    application = Application.objects.get(id=app_id)

    if request.method == "POST":
        application.rating = request.POST['rating']
        application.review = request.POST.get('review')
        application.save()

    return redirect('view_applicants', job_id=application.job.id)


# ⭐ Rate contractor
@custom_login_required
def rate_contractor(request, app_id):
    application = Application.objects.get(id=app_id)

    if request.method == "POST":
        application.contractor_rating = request.POST['contractor_rating']
        application.contractor_review = request.POST.get('contractor_review')
        application.save()

    return redirect('dashboard')


# 🗑️ Delete Job
@custom_login_required
def delete_job(request, job_id):
    user_id = request.session.get('user_id')
    try:
        job = Job.objects.get(id=job_id, contractor_id=user_id)
        job.delete()
        messages.success(request, "Job deleted successfully.")
    except Job.DoesNotExist:
        messages.error(request, "Job not found or permission denied.")

    return redirect('dashboard')


# ✅ Mark Job as Complete
@custom_login_required
def mark_complete(request, job_id):
    user_id = request.session.get('user_id')
    try:
        job = Job.objects.get(id=job_id, contractor_id=user_id)
        job.is_completed = True
        job.save()
        messages.success(request, "Job marked as complete.")
    except Job.DoesNotExist:
        messages.error(request, "Job not found or permission denied.")

    return redirect('dashboard')


# ✏️ Edit Job
@custom_login_required
def edit_job(request, job_id):
    user_id = request.session.get('user_id')
    try:
        job = Job.objects.get(id=job_id, contractor_id=user_id)
    except Job.DoesNotExist:
        messages.error(request, "Job not found or permission denied.")
        return redirect('dashboard')

    if request.method == 'POST':
        job.title = request.POST.get('title', job.title)
        job.salary = request.POST.get('salary', job.salary)
        job.timing = request.POST.get('timing', job.timing)
        job.max_workers = request.POST.get('max_workers', job.max_workers)
        job.is_urgent = 'is_urgent' in request.POST
        date_val = request.POST.get('job_date')
        job.job_date = date_val if date_val else job.job_date
        job.save()
        messages.success(request, "Job updated successfully.")
        return redirect('dashboard')

    return render(request, 'edit_job.html', {'job': job})


# 🚫 Withdraw Application (Worker)
@custom_login_required
def withdraw_application(request, app_id):
    user_id = request.session.get('user_id')
    try:
        app = Application.objects.get(id=app_id, worker_id=user_id, status='applied')
        app.delete()
        messages.success(request, "Application withdrawn.")
    except Application.DoesNotExist:
        messages.error(request, "Application not found or already processed.")

    return redirect('dashboard')


# 🔍 Browse Workers (Contractor)
@custom_login_required
def worker_list(request):
    user_id = request.session.get('user_id')

    skill_filter = request.GET.get('skill', '')
    location_filter = request.GET.get('location', '')

    workers = User.objects.filter(role='worker')
    if skill_filter:
        workers = workers.filter(skills__icontains=skill_filter)
    if location_filter:
        workers = workers.filter(location__icontains=location_filter)

    return render(request, 'workers.html', {
        'workers': workers,
        'skill_filter': skill_filter,
        'location_filter': location_filter,
    })


# 📍 Map view (WITH POPUP DATA)
def map_view(request):
    jobs = Job.objects.all()

    jobs_data = []
    for job in jobs:
        if job.latitude and job.longitude:
            jobs_data.append({
                'title': job.title,
                'salary': job.salary,
                'location': job.location,
                'lat': job.latitude,
                'lng': job.longitude,
                'is_urgent': job.is_urgent,
                'is_completed': job.is_completed,
                'timing': job.timing or '',
                'job_date': str(job.job_date) if job.job_date else '',
                'max_workers': job.max_workers,
                'applicants': job.application_set.count(),
                'contractor_name': job.contractor.name,
            })

    return render(request, 'map.html', {
        'jobs_json': json.dumps(jobs_data)
    })
@custom_login_required
def dashboard(request):
    user_id = request.session.get('user_id')

    from users.models import User
    from django.db.models import Avg

    user = User.objects.get(id=user_id)

    if user.role == 'worker':
        applications = Application.objects.filter(worker=user).select_related('job')
        total_applied = applications.count()
        total_hired_count = applications.filter(status='hired').count()
        total_pending = applications.filter(status='applied').count()
        avg_rating = applications.filter(rating__isnull=False).aggregate(Avg('rating'))['rating__avg']

        return render(request, 'dashboard_worker.html', {
            'user': user,
            'applications': applications,
            'total_applied': total_applied,
            'total_hired': total_hired_count,
            'total_pending': total_pending,
            'avg_rating': avg_rating,
        })
    else:
        total_jobs = Job.objects.filter(contractor=user).count()
        total_applications = Application.objects.filter(job__contractor=user).count()
        total_hired = Application.objects.filter(job__contractor=user, status='hired').count()

        jobs = Job.objects.filter(contractor=user)

        return render(request, 'dashboard.html', {
            'user': user,
            'total_jobs': total_jobs,
            'total_applications': total_applications,
            'total_hired': total_hired,
            'jobs': jobs,
        })
@custom_login_required
def notifications_view(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    
    # Currently, notifications are primarily "hired" jobs for workers
    notifications = []
    if user.role == 'worker':
        notifications = Application.objects.filter(worker=user, status='hired').order_by('-id')
        
    return render(request, 'notifications.html', {
        'user': user,
        'notifications': notifications
    })

from django.shortcuts import render, redirect
from .models import User
from jobs.models import Application
from django.db.models import Avg
from django.contrib.auth.hashers import make_password, check_password
from .decorators import custom_login_required
# 👤 USER PROFILE VIEW
@custom_login_required
def profile_view(request, user_id):
    profile_user = User.objects.get(id=user_id)
    avg_rating = None
    applications = []

    if profile_user.role == 'worker':
        applications = Application.objects.filter(worker=profile_user).select_related('job')
        avg_rating = applications.filter(rating__isnull=False).aggregate(Avg('rating'))['rating__avg']

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'avg_rating': avg_rating,
        'applications': applications,
    })


# 🚪 LOGOUT
def logout_view(request):
    request.session.flush()
    return redirect('login')


# 📝 REGISTER
def register(request):
    if request.method == "POST":
        User.objects.create(
            name=request.POST['name'],
            password=make_password(request.POST['password']),
            role=request.POST['role'],
            language=request.POST['language'],
            location=request.POST['location'],
            skills=request.POST.get('skills', ''),
            wage=request.POST.get('wage') or None,
            profile_image=request.FILES.get('profile_image'),
            bio=request.POST.get('bio')
        )
        return redirect('login')

    return render(request, 'register.html')


# 🔐 LOGIN
def login_view(request):
    if request.method == "POST":
        user = User.objects.filter(
            name=request.POST['name']
        ).first()

        if user:
            # Check hashed password or fallback to plaintext
            if check_password(request.POST['password'], user.password):
                request.session['user_id'] = user.id
                request.session['role'] = user.role
                return redirect('home')
            elif user.password == request.POST['password']:
                # Upgrade plaintext to hash
                user.password = make_password(request.POST['password'])
                user.save()
                request.session['user_id'] = user.id
                request.session['role'] = user.role
                return redirect('home')

    return render(request, 'login.html')


# 🏠 HOME (HIRE + RATING + NOTIFICATIONS)
@custom_login_required
def home(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)

    # 🔥 Applications of this user
    applications = Application.objects.filter(worker=user)

    # ⭐ Average rating
    avg_rating = Application.objects.filter(
        worker=user,
        rating__isnull=False
    ).aggregate(Avg('rating'))['rating__avg']

    # 🔔 Notification count (hired jobs)
    notifications_count = Application.objects.filter(
        worker=user,
        status="hired"
    ).count()

    return render(request, 'home.html', {
        'user': user,
        'applications': applications,
        'avg_rating': avg_rating,
        'notifications_count': notifications_count
    })
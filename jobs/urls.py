from django.urls import path
from . import views

urlpatterns = [
    path('post-job/', views.post_job, name='post_job'),
    path('jobs/', views.job_list, name='jobs'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('applicants/<int:job_id>/', views.view_applicants, name='view_applicants'),
    path('hire/<int:app_id>/', views.hire_worker, name='hire_worker'),
    path('rate/<int:app_id>/', views.rate_worker, name='rate_worker'),
    path('rate-contractor/<int:app_id>/', views.rate_contractor, name='rate_contractor'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('complete-job/<int:job_id>/', views.mark_complete, name='mark_complete'),
    path('edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('withdraw/<int:app_id>/', views.withdraw_application, name='withdraw_application'),
    path('workers/', views.worker_list, name='worker_list'),
    path('map/', views.map_view, name='map_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('notifications/', views.notifications_view, name='notifications'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('create-student/', views.create_student, name='create_student'),
    path('update-student/<int:telegram_id>/', views.update_student, name='update_student'),
    path('get-student/<int:telegram_id>/', views.get_student, name='get_student'),
    path('get-all-students/', views.get_all_students, name='get_all_students'),
]
from django.urls import path
from . import views

app_name = 'cafesubmission'

urlpatterns = [
    path('', views.cafesubmission, name='cafesubmission'),
    path('draft/', views.draftcafesubmission, name='draftcafesubmission'),
    path('cafesubmission_approve/<int:pk>', views.cafesubmission_approve, name='cafesubmission_approve'),
    path('cafesubmission_delete/<int:pk>', views.cafesubmission_delete, name='cafesubmission_delete'),
]
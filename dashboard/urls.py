from django.urls import path

from . import views

app_name = 'blockchain_app'

urlpatterns = [
    path('', views.overview, name='overview'),
    # ex: /dashboard/batches/
    path('current_batches/', views.batches, name='current_batches'),
    # ex: /dashboard/batches/info
    path('mixed/', views.batchinfo, name='batch_info')
]
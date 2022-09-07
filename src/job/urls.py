from django.urls import include, path
from . import views
from . import api
app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add_job/', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job'),

    # functions based API
    path('api/list', api.job_list_api, name='job_list_api'),
    path('api/list/<int:id>', api.job_detail_api, name='job_detail_api'),

    # class based views API
    path('api/v2/list', api.JobListAPI.as_view(), name='job_list_api_v2'),
    path('api/v2/list/<int:id>', api.JobDetailAPI.as_view(),
         name='job_detail_api_v2'),


]

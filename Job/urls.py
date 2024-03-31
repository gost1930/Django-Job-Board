from django.urls import path ,include
from . models import views

urlpatterns = [
    path('/',views.job_list),
    path('detail=<int:id>',views.job_detail),


]
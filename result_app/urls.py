from django.urls import path
from .views import *

app_name = "result_app"

urlpatterns = [
    path('counselee/', CounseleeListView.as_view()),
    path('result/', ResultListView.as_view()),
    path('result/pres/', PrescriptionListView.as_view()),
    path('result/pres/detail/', PrescriptionDetail.as_view())

]

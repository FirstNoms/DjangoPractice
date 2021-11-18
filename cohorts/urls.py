from django.urls import path
from cohorts import views as cv

urlpatterns=[
    path('/create', cv.create_cohort),
    path('/all', cv.get_cohorts),
    path('/get_one', cv.get_cohort),
    path('/update', cv.update_cohort),
    path('/delete', cv.delete_cohort),
]
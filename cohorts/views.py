from django.shortcuts import render

# Create your views here.
#CRUD OPERATION(FUNCTIONS) FOR COHORTS
def create_cohort(request):
    return render(request, "create_cohort.html")


def get_cohorts(request):
    return render(request, "get_cohorts.html")


def get_cohort(request):
    return render(request, "get_cohort.html")


def update_cohort(request):
    return render(request, "update_cohort.html")


def delete_cohort(request):
    return render(request, "delete_cohort.html")

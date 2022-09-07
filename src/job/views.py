from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import job
from django.core.paginator import Paginator
from .form import ApplyForm, AddJob
from .filter import JobFilter
# Create your views here.


@login_required
def job_list(request):
    jobs_filter = JobFilter(request.GET, queryset=job.objects.all().order_by(
        '-published_at', '-salary'))
    job_list = jobs_filter.qs
    paginator = Paginator(job_list, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj, 'jobs_filter': jobs_filter}
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job_detail = job.objects.get(slug=slug)
    if (request.POST):
        form = ApplyForm(request.POST, request.FILES)
        if (form.is_valid()):   # save in the database
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()
    else:
        form = ApplyForm()  # show the form
    context = {'form': form}
    return render(request, 'job/job_detail.html', context)


@login_required
def add_job(request):
    if request.POST:
        job_details = AddJob(request.POST, request.FILES)
        if job_details.is_valid():
            my_form = job_details.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('jobs:job_list'))

    else:
        job_details = AddJob()

    context = {'job_infos': job_details}
    return render(request, 'job/add_job.html', context)

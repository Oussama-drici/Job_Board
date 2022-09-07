import profile
from django.shortcuts import render
from . import forms
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
# Create your views here.
from .models import profile, city
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse("accounts:profile_edit"))
    else:
        form = forms.SignupForm()
    context = {'form': form}
    return render(request, 'registration/sign_up.html', context)


def profile_details(request):
    profile1 = profile.objects.get(user=request.user)
    return render(request, "registration/profile.html", {'profile': profile1})


def profile_edit(request):
    profile1 = profile.objects.get(user=request.user)
    if (request.method == 'POST'):
        user_form = forms.UserForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(
            request.POST, request.FILES, instance=profile1)
        if (user_form.is_valid() and profile_form.is_valid()):
            user_form.save()
            profile_form1 = profile_form.save(commit=False)
            profile_form1.user = request.user
            profile_form1.save()
            return redirect(reverse('accounts:profile'))

    else:
        user_form = forms.UserForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=profile1)
    return render(request, "registration/profile_edit.html",
                  {'profile_form': profile_form, 'user_form': user_form})

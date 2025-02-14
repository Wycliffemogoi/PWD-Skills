from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm, AuthenticationForm
from .models import Profile
from django.db.models import Q
from django.contrib import messages

from django.core.paginator import Paginator
from django.db.models import Q
from .models import Profile  # Import your Profile model

def home(request):
    query = request.GET.get('q')

    if query:
        profiles = Profile.objects.filter(
            Q(id_number__icontains=query) |
            Q(ncpwd_number__icontains=query) |
            Q(county__icontains=query) |
            Q(subcounty__icontains=query) |
            Q(ward__icontains=query) |
            Q(skills__icontains=query) |
            Q(level_of_education__icontains=query)
        )
    else:
        profiles = Profile.objects.all()

    # Add pagination (10 profiles per page)
    paginator = Paginator(profiles, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'profiles/home.html', {'profiles': page_obj})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile_create')
    else:
        form = UserRegisterForm()
    return render(request, 'profiles/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'profiles/login.html', {'form': form})

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile


@login_required
def profile_create(request):
    # Check if the user already has a profile
    if Profile.objects.filter(user=request.user).exists():
        messages.warning(request, "You already have a profile. You can update it instead.")
        return redirect('profile_update')  # Redirect to profile update page if they already have a profile

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile created successfully.")
            return redirect('home')
    else:
        form = ProfileForm()

    return render(request, 'profiles/profile_create.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def profile_update(request):
    # Get the user's profile or return a 404 error if it doesn't exist
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        # Populate the form with the submitted data and the existing profile instance
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('home')
    else:
        # Populate the form with the existing profile data
        form = ProfileForm(instance=profile)

    return render(request, 'profiles/profile_update.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
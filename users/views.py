from django.shortcuts import render, redirect, get_object_or_404
from . forms import CustomUserCreationForm, UserProfileForm, VideoSubmitForm
from . models import UserProfile, Video
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def SignupPage(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            return redirect("UserPage")
    context = {"form" :form}
    return render(request, 'users/signup.html', context)
def LogOutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("HomePage")
    else:
        return redirect("SignInPage")
@login_required(login_url="SignInPage")
def dashboard(request):
    active_user = request.user
    user_profile = UserProfile.objects.get(user=active_user)
    videos = Video.objects.filter(owner=active_user)
    form = UserProfileForm(request.POST, instance=user_profile)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid:
            form.save()
            return redirect("UserPage")
    context = {"profile": user_profile, "form": form, "videos":videos}
    return render(request,'users/dashboard.html', context)
def SigninPage(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        new_user =authenticate(username= username, password=password)
        login(request,new_user)
        return redirect("UserPage")
    return render(request, 'users/sign-in.html')

@login_required(login_url="SignInPage")
def UploadVideoPage(request):
    form = VideoSubmitForm()
    active_user = request.user

    if request.method =="POST":
        form = VideoSubmitForm(request.POST, request.FILES)
        if form.is_valid:
            form.save(commit=False)
            form.instance.owner = active_user
            form.save()
            return redirect("UserPage")   
    context = {"form": form}
    return render(request, 'users/upload-video.html', context)
@login_required(login_url="SignInPage")
def VideoReview(request,pk):
    active_user = request.user
    userProfile = active_user
    if "like_video" in request.POST:
        video = get_object_or_404(Video, id=request.POST.get('like_video'))
        video.likes.add(active_user)
        if userProfile in video.dislikes.all():
            video.dislikes.remove(active_user)
    elif "dislike_video" in request.POST:
        video = get_object_or_404(Video, id=request.POST.get("dislike_video"))
        video.dislikes.add(active_user)
        if userProfile in video.likes.all():
            video.likes.remove(active_user)
    return HttpResponseRedirect(reverse("PlayerPage", args=[str(pk)]))

# TEST VIEWS
# def dashboard(request):
#     pass
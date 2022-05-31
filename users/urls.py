from django.urls import path , include
from . import views
urlpatterns = [
    path('dashboard/' , views.dashboard, name="UserPage"),
    path('signup/', views.SignupPage, name="SignUpPage"),
    path('signin/', views.SigninPage, name="SignInPage"),
    path('logout/', views.LogOutPage, name="LogOutPage"),
    path('upload-video/', views.UploadVideoPage, name="UploadPage"),
    path('video-review/<str:pk>/', views.VideoReview, name="VideoReviewPage")
]
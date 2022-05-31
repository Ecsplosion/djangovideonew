from django.shortcuts import render
from users.models import Video, UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="SignInPage")
def videoplayer(request, pk):
    up = request.user
    associated_up = UserProfile.objects.get(user=up)
    video_obj = Video.objects.get(id=pk)
    likes= video_obj.likes.all().count()
    dislikes = video_obj.dislikes.all().count()
    user_review = ""
    if up in video_obj.likes.all():
        user_review = "liked"
    elif up in video_obj.dislikes.all():
        user_review = "disliked"
    else:
        user_review= ""
    context = {"video": video_obj, "likes": likes , "dislikes":dislikes, "user_review": user_review, "profile": associated_up}
    return render(request, 'videoplayer/player.html', context)

# TEST VIEW
# def videoplayer(request,pk):
#     pass
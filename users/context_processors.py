def Profile(request):
    from users.models import UserProfile
    active_user =request.user
    if request.user.is_authenticated:
        if request.user is not None:
            object = UserProfile.objects.get(user=active_user)
            return {'Profile': object}
    else:
        return {}
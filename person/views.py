from django.shortcuts import render, redirect
from person.models import UserProfile, WallPost
from person.forms import UserForm, UserProfileForm, WallPostForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control
from django.utils import timezone

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    profiles = UserProfile.objects.all()
    return render(request, 'index.html', {'profiles':profiles})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def details(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    wall_posts = profile.wallpost_set.order_by('-pub_date')
    form = WallPostForm()
    if request.POST:
        form = WallPostForm(request.POST)
        if form.is_valid():
            wall_post = form.save(commit=False)
            wall_post.receiver = profile
            wall_post.sender = request.user.userprofile
            wall_post.pub_date = timezone.now()
            wall_post.save()
            return redirect('person:details', profile_id)
    return render(request, 'details.html',{'profile':profile,
                                           'wall_posts':wall_posts,
                                           'form':form})


def register(request):
    if request.POST:
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid():
            print('forms are valid')
        else:
            print('forms ar invalid')

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if profile.avatar:
                profile.avatar = request.FILES['avatar']
            profile.save()
        else:
            print(user_form.errors, profile_form.errors)
        return redirect('person:home')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        return render (request, "register.html", {'user_form': user_form,
                                                  'profile_form': profile_form})

def user_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('person:details', profile_id = user.userprofile.id)
        else:
            return redirect('person:register')
    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return redirect('person:home')


def edit(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    profile_form = UserProfileForm(instance=profile)
    if not request.user.is_authenticated():
        profile_form = UserProfileForm(instance=profile)
        return redirect("person:login")
   # elif int(profile_id) != request.user.id:
   #     return redirect("person:edit", request.user.id)
    else:
        if request.POST:
            profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect("person:details", profile.id)
        return render(request, "edit.html", {'profile':profile,
                                             'profile_form':profile_form})

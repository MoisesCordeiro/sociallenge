from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from bootcamp.iauth.forms import SignUpForm,PeriodForm
from django.contrib.auth.models import User
from bootcamp.feeds.models import Feed

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'auth/signup.html', {'form': form})
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            welcome_post = u'{0} has joined the network.'.format(user.username, user.username)
            feed = Feed(user=user, post=welcome_post)
            feed.save()
            return redirect('/iauth/period')
    else:
        return render(request, 'auth/signup.html', {'form': SignUpForm()})


def period(request):
    if request.method=="GET":
        form = PeriodForm(instance=request.user.profile)
        return render(request, 'auth/period.html', {'form': form})
    elif request.method == "POST":
        form = PeriodForm(request.POST,instance=request.user.profile)
        if not form.is_valid():
            return render(request, 'auth/period.html', {'form': form})   
        form.save()
        return redirect('/')
    
    
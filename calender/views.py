from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, AddEvent, RegistrationForm
from .models import Event



def index(request):
	return HttpResponse("I'm home user")



def user_login(request):

    # print(request, request.method)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse("YEah")
                    return redirect('viewEvent')
                    # return render(request,'Task/viewTask.html')


        else:
            return render(request, 'calender/login.html', {'form': form})
    else:
        return render(request, 'calender/login.html', {'form': LoginForm()})

    # return redirect('addEvent:index')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            return redirect('auth:login')
        else:
            return render(request, 'calender/register.html', {'form': form})
    else:
        return render(
            request, 'calender/register.html', {'form': RegistrationForm()}
        )


def logout_view(request):
    logout(request)
    return redirect('lists:index')

def addEvent(request):

    if request.method == 'POST':
        event_name = request.POST["event_name"]
        event_data = Event(event_name = event_name)
        event_data.save()
    
        # return HttpResponse(request,"Your Task Added")
        return redirect('viewEvent')


    else:
        return render(request, 'calender/addEvent.html', {'form': AddEvent()})



def viewEvent(request):
    # return HttpResponse("List of Task")
    list_event = Event.objects.all()

    print(list_event,"getting the list of task")

    return render(request,'calender/viewEvent.html',{'events': list_event}) 
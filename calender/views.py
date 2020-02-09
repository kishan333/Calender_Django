from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect ,JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, AddEvent, RegistrationForm
from .models import Event
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import eventSerializer
 

# def index(request):
# 	return HttpResponse("I'm home user")

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
        else:
            return render(request, 'calender/login.html', {'form': form})
    else:
        return render(request, 'calender/login.html', {'form': LoginForm()})

    # return redirect('addEvent:index')

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             User.objects.create_user(
#                 username=request.POST['username'],
#                 email=request.POST['email'],
#                 password=request.POST['password']
#             )
#             return redirect('auth:login')
#         else:
#             return render(request, 'calender/register.html', {'form': form})
#     else:
#         return render(
#             request, 'calender/register.html', {'form': RegistrationForm()}
#         )

def logout_view(request):
    logout(request)
    return redirect('lists:index')

@login_required
def addEvent(request):

    if request.method == 'POST':
        title = request.POST["title"]
        # event_description = request.POST["event_description"]
        end = request.POST["end"]
        start = request.POST["start"]
        event_data = Event(
        	title = title, 
        	# event_description = event_description, 
        	end = end ,
        	start = start,
        	)
        event_data.save()
    
        # return HttpResponse(request,"Your Task Added")
        return redirect('viewEvent')


    else:
        return render(request, 'calender/addEvent.html', {'form': AddEvent()})

@login_required
def viewEvent(request):

    list_event = Event.objects.all()
    print(list_event,"getting the list of task")
    return render(request,'calender/viewEvent.html',{'events': list_event}) 

# @login_required
class addEventList(APIView):

	def post(self, request, format=None):
		recevied_field_data = eventSerializer(data = request.data)
		if recevied_field_data.is_valid():
			recevied_field_data.save()
			return Response(recevied_field_data.data, status = status.HTTP_201_CREATED)
		return Response(recevied_field_data.data, status = status.HTTP_400_BAD__REQUEST)	

# @login_required
class displayEventList(APIView):

	def get(self, request):
		event_list_data = Event.objects.all()
		serializer = eventSerializer(event_list_data, many = True)
		return Response(serializer.data)

	def post(self):
		pass
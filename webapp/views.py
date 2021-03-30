from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

def sample(request):
    return render(request,'webapp/sample.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("webapp/profile.html")
        else:
            messages.info(request, 'invalid credential')
            return redirect('webapp/login.html')


    else:
        return render(request, 'webapp/login.html')


def registration(request):
    if request.method =="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'/')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save();
                messages.info(request,'user created successfully')
                return redirect('/')
        else:
            messages.info('password not matching')
    else:
        return render(request,'webapp/registration.html')




# Create your views here.

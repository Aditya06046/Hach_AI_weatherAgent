from django.shortcuts import render
from myapp.models import User
from django.contrib import messages

from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import mysql.connector

from rest_framework.decorators import api_view

from django.shortcuts import redirect
from rest_framework.authtoken.models import Token


# Create your views here.
@api_view(['GET','POST'])
def registerUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = (request.POST.get('password'))
        confirmpass = (request.POST.get('confirmpass'))

        if(username=='' or email=='' or password=='' or confirmpass==''):
            messages.warning(request,"User must fill all the fields")
            return render(request,'userForm.html')
        print(password, confirmpass)
        if(password != confirmpass):
            messages.warning(request,"passwords must match")
            return render(request,'userForm.html')

        con = mysql.connector.connect(host='localhost',user='root',password='',database='user')
        cursor = con.cursor()
        sqlst = f"SELECT email FROM users WHERE email='{email}'"
        cursor.execute(sqlst)
        dbUser = ''
        for i in cursor:
            print(i)
            dbUser = i[0]
        print(f"dbUser : {dbUser}")
        if request.POST.get('username'):
            if(dbUser==''):
                user = User()
                user.name = username
                user.email = email
                user.password = make_password(password)
                user.save()
                messages.success(request,"Successfully created user") 
                return redirect('login/')
            else:
                messages.warning(request,"User already exists with this mail")
                return redirect('http://localhost:8000/')
    else:
        return render(request,'userForm.html')
    

@api_view(['GET','POST'])
def loginUser(request):
    if request.method=='POST':

        con = mysql.connector.connect(host='localhost',user='root',password='',database='user')
        cursor = con.cursor()

        email = request.POST.get('email')
        password = request.POST.get('password')

        sqlst = f"SELECT password FROM users WHERE email='{email}'"
        cursor.execute(sqlst)

        for i in cursor:
            dbPass = i[0]
            print(dbPass)
        if(check_password(password,dbPass)):
            print("Really Nice")
            return redirect('http://localhost:8000/home/')
        else:
            print("Bad Luck")
        return render(request,'loginForm.html')

    else:
        return render(request,'loginForm.html')

def homePage(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        min_temp = request.POST.get('min_temp')
        max_temp = request.POST.get('max_temp')
        print(location, min_temp, max_temp)

    return render(request,'homePage.html')
def logoutUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpass = request.POST.get('conformpass')

        if request.POST.get('username'):
            saveRecord = User()
            saveRecord.name = username
            saveRecord.email = email
            # saveRecord.password = make_password(password)
            saveRecord.save()  
            messages.success(request,"record saved")  
            return render(request,'userForm.html')
    else:
        return render(request,'userForm.html')


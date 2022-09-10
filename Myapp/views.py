from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import StudentUser,User,Book
from django.contrib.messages import error,success
from django.contrib.auth import logout,login
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method=='POST':
        fullname=request.POST.get('name')
        username=request.POST.get('username')
        if request.POST.get('password') == request.POST.get('password2'):
            try:
                user=StudentUser.objects.get(username=username)
                error(request,'UserName Already Exist')
                return render(request,'signup.html')
            except StudentUser.DoesNotExist:
                user=StudentUser(full_name=fullname,username=username,password=request.POST.get('password'))
                user.save()
                success(request,'Your Registration successfull ! Please Login')
                return redirect('/')
        else:
            return render(request,'signup.html')
    else:    
        return render(request,'signup.html')

def user_login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_obj=StudentUser.objects.filter(username=username,password=password)
        if user_obj:
            request.session['username']=username
            return redirect('/home/')
        else:
            error(request,'invalid username or Password') 
            return render(request,'login.html')
    else:
        return render(request,'login.html')   


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')         

def home(request):
    all_obj=Book.objects.all()
    return render(request,'home.html',{"all_books":all_obj})     
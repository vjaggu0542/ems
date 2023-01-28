from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from sms_app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from sms_app.models import Customuser

def BASE_FILE(request):

    return render(request, 'base.html')

def LOGIN(request):
    return render(request, 'login.html')
def DOLOGIN(request):

    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
            username=request.POST.get('email'),
            password=request.POST.get('password'),)
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('manager_home')

            elif user_type == '2':
                 return HttpResponse('this is Teamlead panel')
            elif user_type == '3':
                 return HttpResponse('this is Employee panel')
            else:
                messages.error(request,'username or password invalied')
                return redirect('login')
            
        else:
            messages.error(request,'username or password invalied')
            return redirect('login')
        
def LOGOUT(request):
    logout(request)
    return redirect('login')
@login_required(login_url="/")
def PROFILE(request):
    user = Customuser.objects.get(id = request.user.id)
    context = {
        'user':user,
    }
    return render(request, 'profile.html',context)


@login_required(login_url="/")
def PROFILE_UPDATE(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
             customuser = Customuser.objects.get(id = request.user.id)
             customuser.first_name = first_name
             customuser.last_name = last_name
             
             if password != None and password != "":
                    customuser.set_password(password)
             if profile_pic != None and profile_pic != "":
                    customuser.profile_pic = profile_pic
                    
             customuser.save()
             messages.success(request,'your profile updated successfully')
             return redirect('profile')
        except:
             messages.error(request,'failed to uplode your request')


    return render(request, 'profile.html')


            

        


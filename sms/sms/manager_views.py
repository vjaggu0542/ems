from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from sms_app.models import Designation,Duration,Customuser,Employee,Teamlead
from django.contrib import messages

@login_required(login_url="/")
def HOME(request):
    return render(request, 'manager/home.html')

@login_required(login_url="/")
def EMPLOYEE_ADD(request):
    designation = Designation.objects.all()
    duration = Duration.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        designation_id = request.POST.get('designation_id')
        duration_id = request.POST.get('duration_id')

        if Customuser.objects.filter(email=email).exists():
           messages.warning(request,'email is already taken')
           return redirect('employee_add')
        if Customuser.objects.filter(username=username).exists():
           messages.warning(request,'username is already taken')
           return redirect('employee_add')
        
        else: 
            user = Customuser(
              profile_pic = profile_pic,
              first_name = first_name,
              last_name = last_name,
              email = email,
              username =username,
              user_type = 3

            )
            user.set_password(password)
            user.save()

            designation = Designation.objects.get(id = designation_id)
            duration = Duration.objects.get(id = duration_id)

            employee = Employee(
                 admin = user,
                 address = address,
                 gender = gender,
                 designation_id = designation,
                 duration_id = duration,
            ) 

            employee.save()
            messages.success(request, user.first_name + "  " + user.last_name + ' are successfully saved')
            return redirect('employee_add')

    context = {
        'designation' :designation,
        'duration' : duration
    }
        
        
    return render(request, 'manager/employee_add.html', context)


def VIEW_EMPLOYEE(request):
    employee = Employee.objects.all()

    context = {
        'employee':employee,
    }
    return render(request,'manager/view_employee.html',context)

def EDIT_EMPLOYEE(request,id):
    employee = Employee.objects.filter(id = id)
    designation = Designation.objects.all()
    duration = Duration.objects.all()
    context ={
        'employee':employee,
        'designation':designation,
        'duration':duration,
    }
    return render(request,'manager/edit_employee.html',context)

def UPDATE_EMPLOYEE(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee_id')
       
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        designation_id = request.POST.get('designation_id')
        duration_id = request.POST.get('duration_id')

        user = Customuser.objects.get(id = employee_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username =username

        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)

        user.save()

        employee = Employee.objects.get(admin = employee_id)

        employee.address = address
        employee.gender = gender
        
        designation = Designation.objects.get(id=designation_id)
        employee.designation_id = designation

        duration = Duration.objects.get(id=duration_id)
        employee.duration_id = duration

        employee.save()

        messages.success(request, 'records updated successfully')
        return redirect('view_employee')

    return render(request,'manager/edit_employee.html')


def DELETE_EMPLOYEE(request,admin):
    employee = Customuser.objects.get(id = admin)
    employee.delete()
    messages.success(request,'record deleted successfully')
    return redirect('view_employee')

def ADD_DESIGNATION(request):

    if request.method == "POST":

        designation_name = request.POST.get('designation_name')

        designation = Designation(
            name = designation_name
        )
        designation.save()
        messages.success(request, 'designation added successfully')
        return redirect('add_designation')


    return render(request,'manager/add_designation.html')

def VIEW_DESIGNATION(request):
    designation = Designation.objects.all()

    context = {
        'designation':designation,
    }


    return render(request,'manager/view_designation.html',context)

def EDIT_DESIGNATION(request,id):
    designation = Designation.objects.get(id = id)
    context = {
        'designation':designation,
    }
    return render(request,'manager/edit_designation.html',context)

def UPDATE_DESIGNATION(request):

    if request.method == 'POST':
        designation_name = request.POST.get('designation_name')

        designation_id = request.POST.get('designation_id')
        designation = Designation.objects.get(id=designation_id)
        designation.name = designation_name
        designation.save()

        messages.success(request, 'designation are successfully updated')
        return redirect('view_designation')
    
    return render(request,'manager/edit_designation.html')

def DELETE_DESIGNATION(request,id):
    designation = Designation.objects.get(id=id)
    designation.delete()
    messages.success(request,'designation are successfully deleted')
    return redirect('view_designation')

def ADD_TEAMLEAD(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if Customuser.objects.filter(email = email).exists():
           messages.warning(request,'email is already taken')
           return redirect('add_teamlead')
        if Customuser.objects.filter(username=username).exists():
            messages.warning(request,'username is already taken')
            return redirect('add_teamlead')
        else:
            user = Customuser(
                profile_pic = profile_pic,
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                user_type =2
            ) 

            user.set_password(password)
            user.save()

            teamlead = Teamlead(
                admin = user,
                address = address,
                gender  = gender
            )
            teamlead.save()
            messages.success(request,user.username + ' is successfully added')
            return redirect('add_teamlead')


    return render(request,'manager/add_teamlead.html')

def VIEW_TEAMLEAD(request):
    teamlead = Teamlead.objects.all()
    context = {
        'teamlead':teamlead,
    }
    return render(request, 'manager/view_teamlead.html',context)

def EDIT_TEAMLEAD(request,id):
    teamlead = Teamlead.objects.get(id=id)

    context = {
        'teamlead':teamlead,
    }

    return render(request,'manager/edit_teamlead.html',context)

def UPDATE_TEAMLEAD(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        teamlead_id = request.POST.get('teamlead_id')

        user = Customuser.objects.get(id=teamlead_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        if password != None and password != "":
            user.set_password(password)

        user.save()

        teamlead = Teamlead.objects.get(admin=teamlead_id)
        teamlead.address = address
        teamlead.gender = gender

        teamlead.save()

        messages.success(request, user.first_name + ' data is successfully updated' )
        return redirect('view_teamlead')

    
    return render(request,'manager/edit_teamlead.html')

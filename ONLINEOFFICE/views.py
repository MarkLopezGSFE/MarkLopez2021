from django.shortcuts import redirect, render
from .forms import CreateUserForm, requestform, StatusForm
from .models import registration, requesttable
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group


def indexpage(request):
    return render(request, 'index.html')

@unauthenticated_user
def Signuppage(request):
     form = CreateUserForm()
     if request.method == 'POST':
          form = CreateUserForm(request.POST)
          if form.is_valid():
               user = form.save()
               username = form.cleaned_data.get('username')
               
               group = Group.objects.get(name='Clients')
               user.groups.add(group)


               messages.success(request, 'Account was created for ' + username)
               return redirect('/Login')


     context =  {'form':form}
     return render(request, 'Signup.html', context)

@unauthenticated_user
def Loginpage(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/Home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'Login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('Login')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Clients'])
def Schedulerpage(request):
    Schedpage = requesttable.objects.filter(user=request.user)
    return render(request, 'Scheduler.html', {'Schedpage': Schedpage})

@login_required(login_url='Login')
def Homepage(request):
    return render(request, 'Home.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['Clients'])
def requestpage(request):
    form = requestform()
    if request.method == 'POST':
        form = requestform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Scheduler')
    context =  {'form':form}
    return render(request, 'Request.html', context)


# @login_required(login_url='Login')
# def information(request):
#      info = registration.objects.all()
#      return render(request, 'AdminPage.html', {'info': info})

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Coordinator'])
def updatepage(request, pk):
	user = registration.objects.get(id=pk)
	form = CreateUserForm(instance=user)

	if request.method == 'POST':
		form = CreateUserForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('/info')

	context = {'form':form}
	return render(request, 'Signup.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Coordinator'])
def deletepage(request, pk):
	delit = registration.objects.get(id=pk)
	if request.method == "POST":
		delit.delete()
		return redirect('/')

	context = {'item':delit}
	return render(request, 'delete.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Coordinator'])
def coordinator(request):

    Var1 = requesttable.objects.all()
    accept = Var1.filter(Status='Accept').count()
    denied = Var1.filter(Status='Denied').count()
    pending = Var1.filter(Status='Pending').count()
    form = StatusForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/coordinator')
    context = {'form':form,'Var1': Var1, 'accept': accept, 'denied': denied, 'pending': pending}
    return render(request, 'Adminpagerequest.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Coordinator'])
def updatepage2(request, pk):
    user = requesttable.objects.get(id=pk)
    form = StatusForm(instance=user)

    if request.method == 'POST':
        form = StatusForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/coordinator')

    context = {'form':form}
    return render(request, 'update.html', context)

def Warning(request):
    return render(request, 'Warning.html')

# def updaterequest(request, pk):

#     user = requesttable.objects.get(id=pk)
#     form = StatusForm(instance=user)

#     if request.method == 'POST':
#         form = StatusForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('/Adminpagerequest')

#     context = {'form':form}
#     return render(request, 'Signup', context)
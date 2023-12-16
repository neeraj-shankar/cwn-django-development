from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from MemberApp.forms import SignUpForm

# Create your views here.
#************************ Login Page View *********************************
def LoginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in")
            return redirect("home_page")
        else:
            messages.success(request, ("Unable to login! Incorrect username or password. Try again"))
            return redirect('login_page')
    else:

        return render(request, 'members/login.html')

def LogoutView(request):
    logout(request)
    messages.success(request, "You are logged out!!!")
    return redirect("home_page")

#******************************** Register Page View************************
def RegisterView(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered and logged in..!!!")
            return redirect("home_page")
    else:
        form = SignUpForm()
    
    return render(request, 'members/register.html', {'form': form})
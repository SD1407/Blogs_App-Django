from django.shortcuts import render , redirect
# from django.contrib.auth.forms import UserCreationForm  # this will import the django forms class which we can use fro forms template
from django.contrib import messages  # here we are importing django messages(we wanted to pop out some msgs so )
from django.contrib.auth.decorators import login_required # importing decorator this will add functionality to our existing func
from .forms import UserRegisterForm  # we are importing UserRegisterForm so UserCreationForm is no more required


def register(request):
    # form = UserCreationForm()  # created a variable to use that form class of django so here as we use that "form = UserCreationForm" then after entering values in that form the form's data will not be stored as it is a POST_REQUEST type request so we need to use some condition to capture that data and use it
    if request.method == 'POST':  # here we use that "method POST  of that form html templates tag" we are checking one condition ifmethod is == POST then we will create a form which will create a form and will store the POST_REQUEST data in it
        # form = UserCreationForm(request.POST)  # request.POST will store the data in it
        form = UserRegisterForm(request.POST)
        if form.is_valid():   # here django checks after that POST_REQUEST that if the form is valid or not(if valid then it wil create that usernme variable to get the username)
            form.save()  # this will save the form
            username = form.cleaned_data.get('username')  #  creates the username variable and stores the username from the database (form.cleaned_data)
            messages.success(request, f'Account created for {username}!')  # we wanted to pop out that success msg on he base template and after that we wanted to redirect the page to home page so bove section we are importing "redirect" from django.shortcuts along wht render
            # return redirect('blog-home')  # redirecting the home page (here we uses the name blog-home)
            return redirect('login')  # after successfully creating the account this will redirect it to 'login' page
    else:
        # form = UserCreationForm()  # else it will not colllect the data and will behave like normal
        form = UserRegisterForm() 

    return render(request, 'users/register.html', {'form': form})  # here we are passing that from through an argument by creating a dictionary ('form' : form) which uses the form

# here we are making this profile page forlogged in users only so we need to make sure that iff the user is logged in then its profile is accessable
# for making this sure we need to use django login decorator
@login_required  # this will now make sure that the user must log in to view his profile
def profile(request):
    return render(request, 'users/profile.html')
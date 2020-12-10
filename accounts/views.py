from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, IntroForm, AboutForm
from .models import Contact, About, Intro
from .forms import UserRegistrationForm


# from django.contrib import messages


# @login_required decorator allows to limit access to the index page and check whether the user is authenticated
# if so, index page is rendered. If not, the user is redirected to the login page via login_url
@login_required(login_url='login')
def index(request):
    # Render the index page
    return render(request, 'accounts/index.html')


def register_view(request):
    # This function renders the registration form page and create a new user based on the form data
    if request.method == 'POST':
        # We use Django's UserCreationForm which is a model created by Django to create a new user.
        # UserCreationForm has three fields by default: username (from the user model), password1, and password2.
        # If you want to include email as well, switch to our own custom form called UserRegistrationForm
        form = UserCreationForm(request.POST)
        # check whether it's valid: for example it verifies that password1 and password2 match
        if form.is_valid():
            form.save()
            # if you want to login the user directly after saving, use the following two lines instead, and redirect to index
            # user = form.save()
            # login(user)
            # redirect the user to login page so that after registration the user can enter the credentials
            return redirect('login')
    else:
        # Create an empty instance of Django's UserCreationForm to generate the necessary html on the template.
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    # this function authenticates the user based on username and password
    # AuthenticationForm is a form for logging a user in.
    # if the request method is a post
    if request.method == 'POST':
        # Plug the request.post in AuthenticationForm
        form = AuthenticationForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            # get the user info from the form data and login the user
            user = form.get_user()
            login(request, user)
            # redirect the user to index page
            return redirect('index')
    else:
        # Create an empty instance of Django's AuthenticationForm to generate the necessary html on the template.
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    # This is the method to logout the user
    logout(request)
    # redirect the user to index page
    return redirect('index')


def create_profile(request):
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        form2 = IntroForm(request.POST)
        form3 = AboutForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            return redirect('profile')
            # context = {'form1': form1, 'form2': form2, 'form3': form3}
            # return render(request, 'accounts/view_profile.html', context)
    else:

        form1 = ContactForm()
        form2 = IntroForm()
        form3 = AboutForm()
        # context = {'form1': form1, 'form2': form2, 'form3': form3}
    return render(request, 'accounts/create_profile.html', {'form1': form1, 'form2': form2, 'form3': form3})


@login_required(login_url='login')
def view_profile(request):
    info1 = Contact.objects.all()
    info2 = About.objects.all()
    info3 = Intro.objects.all()
    context = {'info1': info1, 'info2': info2, 'info3': info3}
    return render(request, 'accounts/view_profile.html', context)


def update_profile(request, id):
    bio = Intro.objects.get(id=id)
    form = IntroForm(request.POST or None, instance=bio)

    if form.is_valid():
        form.save()

        return redirect('profile')

    return render(request, 'accounts/update_profile.html', {'form': form, 'bio': bio})


def delete_profile(request, id):
    bio = Intro.objects.get(id=id)

    if request.method == 'POST':
        bio.delete()

        return redirect('profile')

        return render(request, 'accounts/delete-confirm.html', {'bio': bio})

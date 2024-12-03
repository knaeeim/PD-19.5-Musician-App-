from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
# @login_required
# def add_musician(request):
#     if request.method == 'POST':
#         form = MusicianForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = MusicianForm()
#     return render(request, 'musician.html', {'form' : form})

# class based view for adding Musician
@method_decorator(login_required, name="dispatch")
class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('add_mus')

    def form_valid(self, form):
        messages.success(self.request, "Musician added successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add'
        return context

# @login_required
# def add_album(request):
#     if request.method == 'POST':
#         form = AlbumForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AlbumForm()
#     return render(request, 'album.html', {'form' : form, 'type' : 'Add'})

# class based view for adding Album
@method_decorator(login_required, name="dispatch")
class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        messages.success(self.request, "Album added successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Add"
        return context
    

# def reistration(request):
#     if request.user.is_authenticated:
#         return redirect('profile')
#     if request.method == 'POST':
#         form = ReistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "User registered successfully")
#             return redirect('login')
#     else:
#         form = ReistrationForm()
#     return render(request, 'registration.html', {'form' : form, 'type' : 'Registation'})

# class based view for user registration
class RegistrationView(CreateView):
    model = User
    form_class = ReistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "User registered successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Registration"
        return context

# def userLogin(request):
#     if request.user.is_authenticated:
#         return redirect('profile')
#     if request.method == "POST":
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             userpassword = form.cleaned_data['password']
#             user = authenticate(username = user_name, password = userpassword)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Logged in Succesfully")
#                 return redirect('profile')
#         else:
#             messages.success(request, "User credential is not correct")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration.html', {'form' : form, 'type' : 'Login'})

# class based view for user login

class UserLoginView(LoginView):
    template_name = 'registration.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Logged in Succesfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "User credential is not correct")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Login"
        return context

@login_required
def profile(request):
    return render(request, 'profile.html')

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('login')

def show_musician(request):
    albums = Album.objects.all()
    return render(request, 'home.html', {'albums' : albums})

# @login_required
# def edit_album(request, id):
#     if request.user.is_authenticated:
#         album = Album.objects.get(pk=id)
#         if request.method == 'POST':
#             form = AlbumForm(request.POST, instance = album)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Album Updated successfully")
#                 return redirect('home')
#         else:
#             form = AlbumForm(instance = album)
#         return render(request, 'album.html', {'form' : form, 'type' : 'Edit'})
    
# class based view for editing Album
@method_decorator(login_required, name="dispatch")
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Album updated successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Edit"
        return context

# @login_required
# def delete_album(request, id):
#    if request.user.is_authenticated:
#         album = Album.objects.get(pk=id)
#         album.delete()
#         messages.success(request, "Album deleted successfully")
#         return redirect('home')
   
# class based view for deleting Album
@method_decorator(login_required, name="dispatch")
class DeleteAlbumView(DeleteView):
    model = Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Album deleted successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Delete"
        return context

# def edit_musician(request, id):
#     if request.user.is_authenticated:
#         musician = Musician.objects.get(pk=id)
#         if request.method == 'POST':
#             form = MusicianForm(request.POST, instance=musician)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Musician Updated successfully")
#                 return redirect('home')
#         else:
#             form = MusicianForm(instance=musician)
#         return render(request, 'musician.html', {'form': form, 'type': 'Edit'})
    
# class based view for editing Musician
@method_decorator(login_required, name="dispatch")
class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Musician updated successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Edit"
        return context
    
# def user_data(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = EditProfileForm(request.POST, instance=request.user)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "User data updated successfully")
#                 return redirect('profile')
#         else:
#             form = EditProfileForm(instance=request.user)
#         return render(request, 'registration.html', {'form': form, 'type': 'Edit'})
    
# class based view for user data
@method_decorator(login_required, name="dispatch")
class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'registration.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "User data updated successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Edit"
        return context
    
# def password_change(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = PasswordChangeForm(request.POST, request.user)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Password changed successfully")
#                 update_session_auth_hash(request, form.user)
#                 return redirect('profile')
#         else:
#             form = PasswordChangeForm(request.user)
#         return render(request, 'registration.html', {'form': form, 'type': 'Change Password'})
    
# class based view for changing password
@method_decorator(login_required, name="dispatch")
class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'registration.html'
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwarg = super().get_form_kwargs()
        kwarg['user'] = self.request.user
        return kwarg
        
    def form_valid(self, form):
        messages.success(self.request, "Password changed successfully")
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Change Password"
        return context
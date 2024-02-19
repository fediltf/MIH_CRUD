from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def user_list(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
def update_user(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UpdateUserForm(instance=user)

    return render(request, 'update_user.html', {'form': form, 'user_id': user_id})

def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('home')

    return redirect('home')
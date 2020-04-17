from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('market')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


'''
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''
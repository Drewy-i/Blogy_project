from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Done!Welcome {username}.')
            return redirect('movies-home')
    else:
            form = UserCreationForm()
    return render(request,'bloggers/register.html', {'form': form})


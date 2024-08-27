from django.shortcuts import render,redirect
from .forms import UserInfoForm


def home(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            country = form.cleaned_data.get('country')
            language = form.cleaned_data.get('language')
            bio = form.cleaned_data.get('bio')
            # Handle the form data as needed (e.g., save it to a database)
            
            return redirect('home')
    else:
        form = UserInfoForm()

    return render(request, 'home/home.html', {'form': form})




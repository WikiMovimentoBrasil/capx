from django.shortcuts import render
from .forms import UserRegistrationForm
# Create your views here.

# Spanish translation
#TODO pensar nas telas básicas
#TODO criar alguns dados no BD para ter dados para puxar para resultados na tela

# English translation
#TODO: Design the basic screens
#TODO: Insert some data into the database to have data to display on the screen

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return render(request, 'register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'home.html')



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

def contact_messages(request):
    messages = Contact.objects.all()
    return render(request, 'contact_messages.html', {'messages': messages})
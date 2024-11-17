from django.shortcuts import render, redirect, get_object_or_404
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


def about(request):
    return render(request, 'about.html')



def contacts_view(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'contact_detail.html', {'contact': contact})


def contacts_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts_list') 
    return redirect('contact_view', id=id)
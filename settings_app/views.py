from django.shortcuts import render, redirect
from settings_app.models import Contact, Ads
from settings_app.forms import ContactForm
from datetime import datetime
# Create your views here.

def contact(request):
    template_name = 'base/contact.html'
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            text = form.cleaned_data.get("text")
            new_contect = Contact.objects.create(name=name, email=email, text=text, date_sent=datetime.now(), accept=False)
            if new_contect is not None:
                new_contect.save()
                return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def ads(request):
    template_name = 'base/ads.html'
    ads = Ads.objects.last()
    context = {
        'ads': ads,
    }
    return render(request, template_name, context)
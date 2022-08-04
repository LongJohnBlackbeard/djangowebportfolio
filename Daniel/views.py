from django.forms import NullBooleanField
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Home, About, Profile, Category, Skills, Portfolio
from .forms import ContactForm


def index(request, success_alert=False):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success_alert'] = True
            return redirect(reverse('index'))
        else:
            print('invalid form')

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')

    # Profile
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    portfolios = Portfolio.objects.all()

    form = ContactForm()
    success_alert = request.session.get('success_alert')

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'form': form,
        'success_alert': success_alert,
    }

    return render(request, 'index.html', context=context)

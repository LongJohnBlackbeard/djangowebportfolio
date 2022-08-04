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
    try:
        home = Home.objects.latest('updated')
    except Home.DoesNotExist:
        home = None

    # About
    try:
        about = About.objects.latest('updated')
    except About.DoesNotExist:
        about = None

    # Profile
    try:
        profiles = Profile.objects.filter(about=about)
    except Profile.DoesNotExist:
        profiles = None

    # Skills
    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        categories = None

    try:
        portfolios = Portfolio.objects.all()
    except Portfolio.DoesNotExist:
        portfolios = None

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

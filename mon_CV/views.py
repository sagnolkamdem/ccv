from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Autre, Formation, Experience, Competence, Contact


# Create your views here.

def home(request):
    """
    Vue permattant d'afficher l'accueil
    """
    autre = Autre.objects.all()
    formation = Formation.objects.all()
    experience = Experience.objects.all()
    context = {
        'autres': autre,
        'formations': formation,
        'experiences': experience
    }
    return render(request, 'mon_cv/accueil.html', context)


def techno(request):
    """
    Vue permettant d'afficher les technologies et les projets
    """
    autre = Autre.objects.all()
    competence = Competence.objects.all()
    context = {
        'autres': autre,
        'competences': competence,
    }
    return render(request, 'mon_CV/techno.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        nom_contact = form.cleaned_data['nom_contact']
        prenom_contact = form.cleaned_data['prenom_contact']
        email = form.cleaned_data['email']
        messagees = form.cleaned_data['messagees']

        contact_n = Contact(nom_contact=nom_contact,
                            prenom_contact=prenom_contact,
                            email=email,
                            messagees=messagees
                            )
        contact_n.save()
        renvoi = True
        return redirect('contact')
    return render(request, 'mon_CV/contact.html', locals())

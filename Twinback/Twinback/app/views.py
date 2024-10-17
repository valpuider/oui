from django.shortcuts import render,redirect
from .models import User

# Create your views here.

def home(request):
    return render(request, 'first.html')

def login(request):
    return render(request, 'second.html')

"""def register(request):
    return render(request, 'third.html')
"""
def accueil(request):
    return render(request, 'fourth.html')

def etudiant(request):
    return render(request, 'etudiant.html')

def alumni(request):
    return render(request, 'alumni.html')

def annonce(request):
    return render(request, 'Annonce.html')

def projet(request):
    return render(request, 'projet.html')
 
from .forms import UserRegistrationForm
from .models import User
#se connecter
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['mot_de_passe'])  
            user.save()
            return redirect('login')  # Redirige vers la page de connexion après l'inscription
    else:
        form = UserRegistrationForm()
    return render(request, 'register2.html', {'form': form})#mettre l'url de login
#afficher
# views.py
def afficher_utilisateur(request):
    utilisateurs = User.objects.all()
    for utilisateur in utilisateurs:
        print(utilisateur.pseudonyme, utilisateur.email,)
    return render(request, 'fourthr.html', {'utilisateurs': utilisateurs})
#modifier un utilisateur
# views.py
def modifier_utilisateur(request, user_id):
    user = User.objects.get(id=user_id)
    user.nom = "Nouveau Nom"
    user.mot_de_passe="nouveau passe word"
    user.save()
# supprimer un utilisateur
# views.py
def supprimer_utilisateur(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()

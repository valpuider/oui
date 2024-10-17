#from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    nom = models.CharField(max_length=100)
    prénom =models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    sexe = models.CharField(max_length=6, choices=[('HOMME', 'Homme'), ('FEMME', 'Femme')])
    mot_de_passe = models.CharField(max_length=255,null=True)
    pseudonyme = models.CharField(max_length=100, blank=True, null=True)
    date_naissance = models.DateField(null=True, blank=True)
    date_inscription = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'twinet'  # Nom exact de la table dans MariaDB
        managed = False
    def __str__(self):
        return (self.nom, self.prénom,self.email)
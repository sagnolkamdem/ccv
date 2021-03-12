from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Formation(models.Model):
    """Model pour les differentes formations"""
    text_intro = models.TextField(blank=True)
    diplom = models.CharField(max_length=200, null=False)
    sessOb = models.CharField(max_length=15, null=False)
    nbre_annee_ob = models.CharField(max_length=200, null=False)
    description = models.TextField()

    def __str__(self):
        return self.diplom


class Experience(models.Model):
    """Model pour les differentes experiences"""
    total_exp = models.IntegerField()
    date_debut = models.CharField(max_length=200)
    date_fin = models.CharField(max_length=200, blank=True)
    nom_entreprise = models.CharField(max_length=200)
    poste_occupe = models.CharField(max_length=200)
    taches_effectuees = models.TextField()

    def __str__(self):
        return self.nom_entreprise


class Competence(models.Model):
    """Model pour les differentes competences"""
    level = (
        ('Advanced', 'Advance'),
        ('Intermediate', 'Intermediate'),
        ('Beginner', 'Beginner')
    )
    type = (
        ('L', 'LANGUAGE'),
        ('F', 'FRAMEWORK'),
        ('GP', 'GESTION DE PROJET'),
        ('L', 'LANGUAGE DE PROGRAMMATION'),
        ('BD', 'BASE DE DONNEES')
    )
    nom_de_la_competence = models.CharField(max_length=200)
    nom_du_projet = models.CharField(max_length=200, blank=True)
    niveau_de_maitrise = models.CharField(max_length=5, blank=True)
    statut_competence = models.CharField(max_length=200, choices=level, blank=True)
    type_de_la_competence = models.CharField(max_length=200, choices=type, blank=True)

    def __str__(self):
        return self.nom_de_la_competence


class Autre(models.Model):
    """Model qui permettra d'enregistrer des choses qui n'ont pas besoin d'une table"""
    photo = models.ImageField(upload_to='photos/', blank=True)
    titre = models.CharField(max_length=200, blank=True)


class Contact(models.Model):
    nom_contact = models.CharField(max_length=200)
    prenom_contact = models.CharField(max_length=200)
    email = models.EmailField()
    messagees = models.TextField()

    def __str__(self):
        return self.nom_contact

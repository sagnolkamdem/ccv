from django.contrib import admin
from .models import Formation, Experience, Competence, Autre, Contact


# Register your models here.


class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('nom_de_la_competence', 'niveau_de_maitrise', 'statut_competence', 'type_de_la_competence')
    list_filter = ('statut_competence', 'type_de_la_competence')


class FormationAdmin(admin.ModelAdmin):
    list_display = ('diplom', 'sessOb', 'nbre_annee_ob', 'description')


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('nom_entreprise', 'poste_occupe', 'taches_effectuees')


admin.site.register(Formation, FormationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(Autre)
admin.site.register(Contact)
from django.db import models
#from crispy_forms.helper import FormHelper
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey, TreeManyToManyField

# Create your models here.
class Sejour(models.Model):
    arrivee = models.DateField()
    depart  = models.DateField()
    visiteur = models.CharField(verbose_name='Nom hôte', max_length=25)

    def __str__(self):
        return self.visiteur

class TissueCategory(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True)
    title  = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name = 'Catégorie'

class WorkCategory(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True)
    title  = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name = 'Type de travail'



class Work(models.Model):
    work_category = TreeManyToManyField(WorkCategory, blank=True)
    sejour = models.ForeignKey(Sejour)
    work_name = models.CharField(max_length=50, default='Travail')
    heure = models.SmallIntegerField(default=1)
    minutes = models.SmallIntegerField(default=0)
    quantity = models.IntegerField(default=0)


class Tissue(models.Model):
    name  = models.CharField(max_length=25)
    tissuecategory = TreeForeignKey(TissueCategory, verbose_name="Catégories")
    tarif = models.DecimalField(max_digits=4, decimal_places=2, default=2.00)

    def __str__(self):
        return self.name


# class PressingWork(Work):
#     work_name = 'Lessive'
#     pressing_unit = models.ManyToManyField(Tissue)
#
#
# class CleaningWork(Work):
#     work_name = 'Nettoyages'
#     timeused = models.TimeField(verbose_name='Durée')
    
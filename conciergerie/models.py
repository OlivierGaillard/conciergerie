from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


def no_digits(titre):
    tot = 0
    for char in titre:
        if char.isdigit():
            tot += 1
    if tot > 2:
        raise ValidationError("Ce champ ne doit pas contenir plus de 2 chiffres")

def max_value(temps):
    try:
        hours = float(temps)
    except:
        raise
    else:
        if hours > 4.0:
            raise ValidationError("N'entrez pas plus de 4h pour une tâche.")


class Travail(models.Model):
    titre = models.CharField(max_length=50, validators=[no_digits])
    temps = models.DecimalField(help_text="1.5 = 1h30, 1.25: 1h15. Maximum = 4h", decimal_places=2, max_digits=3,
                                validators=[max_value])
    datefr  = models.DateField('Date', help_text='jj/mm/aaaa', default=timezone.now)
    owner = models.ForeignKey(User, editable=False, null=True)
    choices = ('C', 'Conciergerie'), ('A', 'AirBnB')
    type  = models.CharField(max_length=1, null=True, choices=choices, default='C')

    class Meta:
        ordering = ['datefr']

    def __str__(self):
        return str(self.datefr) + ' ' +  self.titre + ' ' + str(self.temps)




class Salary(models.Model):
    hour_amount = models.DecimalField(decimal_places=2, max_digits=4, default=25.00)
    owner = models.ForeignKey(User, null=True)



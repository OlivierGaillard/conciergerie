from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def no_digits(titre):
    tot = 0
    for char in titre:
        if char.isdigit():
            tot += 1
    if tot > 2:
        raise ValidationError("Ce champ ne doit pas contenir plus de 2 chiffres")

class Travail(models.Model):
    titre = models.CharField(max_length=50, validators=[no_digits])
    temps = models.DecimalField(help_text="1.5 = 1h30, 1.25: 1h15", decimal_places=2, max_digits=3)
    date  = models.DateField()
    owner = models.ForeignKey(User, editable=False, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return str(self.date) + ' ' +  self.titre + ' ' + str(self.temps)




class Salary(models.Model):
    hour_amount = models.DecimalField(decimal_places=2, max_digits=4)



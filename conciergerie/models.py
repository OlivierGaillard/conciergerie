from django.db import models
from django.utils import timezone

class Travail(models.Model):
    titre = models.CharField(max_length=50)
    temps = models.DecimalField(help_text="1.5 = 1h30, 1.25: 1h15", decimal_places=2, max_digits=3)
    date  = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.date) + ' ' +  self.titre + ' ' + str(self.temps)




class Salary(models.Model):
    hour_amount = models.DecimalField(decimal_places=2, max_digits=4)



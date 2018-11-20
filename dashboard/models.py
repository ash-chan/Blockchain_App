from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)
    join_date = models.DateField('join date')

    class Meta:
        abstract = True


class Mentor(Users):
    profession = models.CharField(max_length=50)
    inv_usd = models.FloatField()
    inv_zco = models.FloatField()

    def __str__(self):
        return self.name


class Mentee(Users):
    major = models.CharField(max_length=50)
    grad_date = models.DateField('graduation date')

    def __str__(self):
        return self.name



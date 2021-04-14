from django.db import models

# Create your models here.


class Add(models.Model):
    n = models.IntegerField()
    m = models.IntegerField()
    res = models.IntegerField()


    def __str__(self):
        return f'{self.id}: {self.n} + {self.m} = {self.res}'


    def is_valid_variable(self):
        return type(self.n) == int and type(self.m) == int and (self.n + self.m) == self.res
from django.db import models

# Create your models here.

class state(models.Model):
    State_name = models.CharField(max_length=200)
    State_population = models.BigIntegerField()
    State_language = models.CharField(max_length=200)
    State_capital = models.CharField(max_length=200)

class Meta:
    db_table = "statedetail"
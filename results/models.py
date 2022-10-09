from django.db import models
from django.contrib.auth.models import User


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.PositiveBigIntegerField()
    ward_number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'Ward {self.ward_number}'


class Result(models.Model):
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE)
    apc = models.IntegerField()
    pdp = models.IntegerField()

    def __str__(self):
        return f'Ward {self.agent.ward_number} results'

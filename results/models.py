from django.db import models
from django.contrib.auth.models import User
    

class Ward(models.Model):
    ward_number = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    supervisor_first_name = models.CharField(max_length=50)
    supervisor_phone_number = models.CharField(max_length=50)
    supervisor_last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Ward {self.ward_number} - {self.name}'


class PollingUnit(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    polling_unit_id = models.PositiveIntegerField()
    polling_unit_name = models.CharField(max_length=100)
    apc = models.IntegerField()
    pdp = models.IntegerField()
    accord = models.IntegerField()
    remarks = models.TextField()

    def __str__(self):
        return f'Ward {self.ward.ward_number}-00{self.polling_unit_id}'

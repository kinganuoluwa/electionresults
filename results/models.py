from django.db import models
    

class Ward(models.Model):
    ward_number = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    supervisor_first_name = models.CharField(max_length=50, blank=True, null=True)
    supervisor_phone_number = models.PositiveBigIntegerField(blank=True, null=True)
    supervisor_last_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'Ward {self.ward_number} - {self.name}'

class PollingUnit(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    agent_first_name = models.CharField(max_length=30, blank=True, null=True)
    agent_last_name = models.CharField(max_length=30, blank=True, null=True)
    agent_phone_number = models.PositiveBigIntegerField(blank=True, null=True)
    polling_id = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Result(models.Model):
    polling_unit = models.OneToOneField(PollingUnit, on_delete=models.CASCADE, editable=False)
    apc = models.IntegerField(default=0)
    pdp = models.IntegerField(default=0)
    accord = models.IntegerField(default=0)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.polling_unit.name} results'

from django.db import models
    

class Ward(models.Model):
    ward_number = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    supervisor_first_name = models.CharField(max_length=50)
    supervisor_phone_number = models.PositiveBigIntegerField()
    supervisor_last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Ward {self.ward_number} - {self.name}'

class Agent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class PollingBooth(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE)
    polling_unit_id = models.PositiveIntegerField()
    polling_unit_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Ward {self.ward.ward_number}-00{self.polling_unit_id}'

class Result(models.Model):
    polling_booth = models.OneToOneField(PollingBooth, on_delete=models.CASCADE)
    apc = models.IntegerField()
    pdp = models.IntegerField()
    accord = models.IntegerField()
    remarks = models.TextField()

    def __str__(self):
        return f'Ward {self.polling_booth.ward.ward_number}-00{self.polling_booth.polling_unit_id} {self.polling_booth.ward.name} results'

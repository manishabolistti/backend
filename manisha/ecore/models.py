from django.contrib.auth.models import User
from django.db import models

class Marchent(models.Model):
    marchentName=models.CharField(max_length=50)
    code=models.CharField(max_length=4)

    def __str__(self):
        return self.marchentName

class Lenin(models.Model):
    marchent = models.ForeignKey(Marchent, on_delete=models.CASCADE)
    leninName=models.CharField(max_length=50)
    leninCode=models.CharField(max_length=4)

    def __str__(self):
        return f"{self.marchent}-{self.leninName}-{self.leninCode}"
class RFID(models.Model):
    marchent=models.ForeignKey(Marchent, on_delete=models.CASCADE)
    leninName=models.ForeignKey(Lenin,on_delete=models.CASCADE)

    RFIDNumber=models.IntegerField()

    def __str__(self):
        return f"{self.marchent}-{self.leninName} - {self.RFIDNumber}"
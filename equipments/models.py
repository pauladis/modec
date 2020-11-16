from django.db import models
from vessels.models import Vessel

class Equipment(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, primary_key=True, unique=True, blank=False, null=False)
    location = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    vessel = models.ForeignKey(Vessel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)

    #@property
    #def name(self):
    #    return self.name

    #@property
    #def code(self):
    #    return self.code
from django.db import models

# Create your models here.
class CovidPrediction(models.Model):
    cough = models.IntegerField()
    fever = models.IntegerField()
    sore_throat = models.IntegerField()
    shortness_breath = models.IntegerField()
    headache = models.IntegerField()
    age60 = models.IntegerField()
    contact_with_positive = models.IntegerField()
    gender = models.IntegerField()
    abroad = models.IntegerField()
    record_date = models.DateTimeField(auto_now=True)
    classification = models.IntegerField()
    

    def __str__(self):
        return str(self.record_date)

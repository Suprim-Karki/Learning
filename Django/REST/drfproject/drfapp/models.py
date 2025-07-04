from django.db import models

# Create your models here.
class Transactions(models.Model):
    title=models.CharField(max_length=100)
    amount=models.FloatField()
    transaction_type =models.CharField(max_length=100,choices=(("CREDIT","CREDIT"),("DEBIT","DEBIT")))

    #Since we want to make balance +ve when credit and -ve when debit, we overwrite save function
    def save(self,*args,**kwargs):
        if self.transaction_type == "DEBIT":
            self.amount = self.amount* -1
        return super().save(*args,**kwargs)
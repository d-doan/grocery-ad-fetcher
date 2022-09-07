from django.db import models

# Create your models here.

class Preferences(models.Model):
    ralphs = models.BooleanField(default=False)
    hmart = models.BooleanField(default=False)
    user_email = models.EmailField(max_length=254, primary_key=True)
    time = models.DateTimeField()
    
    def __str__(self):
        return self.user_email
    
    def save(self,force_insert=False, force_update=False):
        
        if Preferences.objects.filter(user_email__iexact=self.user_email).exists():
            Preferences.objects.filter(pk=self.user_email).delete()
            
        super(Preferences, self).save(force_insert, force_update)
        

class Unsubscribe(models.Model):
    email = models.EmailField(max_length=254, primary_key=True)
    
    def unsub(self):
        if Preferences.objects.filter(user_email__iexact=self.email).exists():
            Preferences.objects.filter(pk=self.email).delete()    
            
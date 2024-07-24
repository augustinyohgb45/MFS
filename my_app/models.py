from django.db import models
from django.contrib.auth.models import User

class Changement(models.Model):
    service_impacte = models.CharField(max_length=255)
    date_changement = models.DateTimeField()
    duree_changement = models.DurationField()
    destinataire = models.EmailField()
    description = models.TextField()
    statut_changement = models.CharField(max_length=50)

class Incident(models.Model):
    service_impacted = models.CharField(max_length=255)
    destinataire = models.EmailField()
    date = models.DateTimeField()
    statut = models.CharField(max_length=50)

class ITMFS(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)

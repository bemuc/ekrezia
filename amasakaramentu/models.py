from django.db import models

# Create your models here.

class amsakaramentu(models.Model):
    nomen =  models.CharField(max_length=200,  null=False)
    domicilium =  models.CharField(max_length=200,  null=False)
    baptizus =  models.DateField(auto_now= False,null=True)
    com_prima =  models.DateField(auto_now= False,null=True, blank=True)
    com_solen =  models.DateField(auto_now= False,null=True, blank=True)
    confirmatis =  models.DateField(auto_now= False,null=True, blank=True)
    matrimonium =  models.DateField(auto_now= False,null=True, blank=True)
    natus =  models.DateField(auto_now= False, null= True)
    patrinus =  models.CharField(max_length=200)
    matrina =  models.CharField(max_length=200)
    pater =  models.CharField(max_length=200,  null=False)
    mater =  models.CharField(max_length=200,  null=False)
    status =  models.CharField(max_length=200, null=True, default='actif')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


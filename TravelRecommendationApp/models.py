from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class DreamDestination(models.Model):
    tms_owner = models.OneToOneField(User,on_delete=models.CASCADE,default='')
    drm_dest_rigistered = models.BooleanField(default=False)
    pTitle = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pLocation = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pdetails = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pic = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pCategory = models.TextField(blank=True,max_length=518,default='no category provided !')
    amount = models.PositiveIntegerField(default=100000)

class RecommendedDestination_cat(models.Model):
    recommendation_template = models.ForeignKey(DreamDestination, on_delete=models.CASCADE,default='')
    pTitle = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pLocation = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pdetails = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pic = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pCategory = models.TextField(blank=True,max_length=518,default='no category provided !')
    amount = models.PositiveIntegerField(default=100000)

class RecommendedDestination_tag(models.Model):
    recommendation_template = models.ForeignKey(DreamDestination, on_delete=models.CASCADE,default='')
    pTitle = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pLocation = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pdetails = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pic = models.CharField(max_length=25,blank=True,null=True,default='sample_destination')
    pCategory = models.TextField(blank=True,max_length=518,default='no category provided !')
    amount = models.PositiveIntegerField(default=100000)
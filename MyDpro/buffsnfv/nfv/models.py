from django.db import models


class Images(models.Model):
	def __str__(self):
		return self.Repo
	ImageName=models.CharField(max_length=200)
	Tag=models.CharField(max_length=200)
	ImageId=models.CharField(max_length=200)
	Function=models.CharField(max_length=200)
	Size=models.CharField(max_length=200, default='NONE')
	Repo=models.CharField(max_length=200, default='NONE')

class Instances(models.Model):
	def __str__(self):
		return self.Name
	Name=models.CharField(max_length=200)
	TimeCreated=models.CharField(max_length=100, default='NONE')
	Image=models.ForeignKey(Images)
	Status=models.CharField(max_length=200, default='NONE')
	ContainerId=models.CharField(max_length=100, default='NONE')

class Interfaces(models.Model):
        def __str__(self):
                return self.Name
        Name=models.CharField(max_length=100)
        IP=models.GenericIPAddressField(protocol='IPv4', default='0.0.0.0')
        Mask=models.IntegerField(default=24)
        Mac=models.CharField(max_length=100,default='NONE')
        InstanceName=models.ForeignKey(Instances,models.SET_NULL, blank=True, null=True )
        def GetName(self):
                return self.Name

# Create your models here.

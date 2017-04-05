from django.db import models

class Interfaces(models.Model):
	def __str__(self):
        	return self.InterfaceName

	InterfaceName=models.CharField(max_length=100)

class IPAddress(models.Model):
	def __str__(self):
		return self.Interface, self.IPAddr, self.Mask
	Interface=models.ForeignKey(Interfaces, on_delete=models.CASCADE)
	IPAddr=models.GenericIPAddressField(protocol='IPv4')
	Mask=models.IntegerField()
	
class Resources(models.Model):
	def __str__(self):
		return self.ImageName, self.FunctionName
	ImageName=models.CharField(max_length=200)
	FunctionName=models.CharField(max_length=200)

class Instance(models.Model):
	def __str__(self):
		return self.Interface, self.InterfaceName, self.Image
	Interface=models.ForeignKey(Interfaces, on_delete=models.CASCADE)
	InstanceName=models.CharField(max_length=200)
	Image=models.ForeignKey(Resources, on_delete=models.CASCADE)
# Create your models here.

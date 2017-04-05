from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from .oldcode import database
from .models import Interfaces, Images, Instances
from .fire import FireCommand

def netmask_to_cidr(netmask):
    return sum([bin(int(x)).count('1') for x in netmask.split('.')])

def UpdateInterfaces():
	DataDict=database()
	RegisterInterfaces=Interfaces.objects.all()
	RegIntName=[]
	for interface in RegisterInterfaces:
		RegIntName.append(interface.Name)
	DataIntName=[]	
	for interface in DataDict.keys():
		DataIntName.append(interface)
	for IntName in DataIntName:
		CalMask=netmask_to_cidr(DataDict[IntName][2])
		if IntName not in RegIntName:
			Interfaces.objects.create(Name=IntName, IP=DataDict[IntName][0], Mask=CalMask, Mac=DataDict[IntName][1])	
	  
def UpdateImages():
	cmd=["docker","images","--format","'{{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.ID}}'"]
	OutputDict=FireCommand(cmd)
	RegisterImages=Images.objects.all()
	RegImgName=[]
	for Image in RegisterImages:
		RegImgName.append(Image.Repo)
	for key in OutputDict.keys():
		if key not in RegImgName:
			try:
				splitkey=key.split('/')
			except:
				splitkey=[key,]
			ImgName=splitkey[(len(splitkey)-1)]
			Images.objects.create(ImageName=ImgName, Repo=key, Tag=OutputDict[key][0], Size=OutputDict[key][1], ImageId=OutputDict[key][2])
	

def UpdateInstances():
	cmd=["docker","ps","-a","--format","'{{.Names}}\t{{.CreatedAt}}\t{{.Image}}\t{{.Status}}\t{{.ID}}'"]	
	OutputDict=FireCommand(cmd)
	RegisterInstances=Instances.objects.all()
	RegInsName=[]
	for instance in RegisterInstances:
		if instance.Name not in RegInsName:
			RegInsName.append(instance.Name)
	for key in OutputDict.keys():
		if key not in RegInsName:
			ImgName=OutputDict[key][1]
			print("The Image name is "+str(ImgName))
			Img=Images.objects.get(Repo=ImgName)
			Instances.objects.create(Name=key, TimeCreated=OutputDict[key][0], Image=Img, Status=OutputDict[key][2], ContainerId=OutputDict[key][3])
		
def index(request):
	UpdateImages()
	UpdateInstances()
	UpdateInterfaces()
	ImgObj=Images.objects.all()
	InsObj=Instances.objects.all()
	IntObj=Interfaces.objects.all()
	image_list=[]
	instance_list=[]
	interface_list=[]
	for Image in ImgObj:
		Dict={}
		Dict["ImageName"]=Image.ImageName
		Dict["Tag"]=Image.Tag
		Dict["ImageId"]=Image.ImageId
		Dict["Size"]=Image.Size
		Dict["Repo"]=Image.Repo
		image_list.append(Dict)
	for Instance in InsObj:
                Dict={}
                Dict["Name"]=Instance.Name
                Dict["TimeCreated"]=Instance.TimeCreated
                Dict["Image"]=Instance.Image
                Dict["Status"]=Instance.Status
                Dict["ContainerId"]=Instance.ContainerId
                instance_list.append(Dict)
	for Interface in IntObj:
                Dict={}
                Dict["Name"]=Interface.Name
                Dict["IP"]=Interface.IP
                Dict["Mask"]=Interface.Mask
                Dict["Mac"]=Interface.Mac
                Dict["InstanceName"]=Interface.InstanceName
                interface_list.append(Dict)
	
	#print(image_list)
	#print(instance_list)
	#print(interface_list)
	return render(request, 'nfv/index.html', {'image_list':image_list,'instance_list':instance_list,'interface_list':interface_list })


def FireCmd(cmd):
	process=subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	out, err=process.communicate()
	errorcode=process.returncode
	out=out.decode()
	return out, errorcode

def ShowImages(request):
	cmd=["docker","images","--format","'{{.Repository}}'",]
	out, errorcode = FireCmd(cmd)
	images_list=out.split()
	return render(request,'nfv/images.html',{'images_list':images_list})

def ShowInstances(request):
	cmd=["docker","ps","--format","'{{.Names}}\t{{.ID}}\t{{.Status}}'"]
	out, errorcode = FireCmd(cmd)
	instances_list=out.split('\n')
	return render(request,'nfv/instances.html',{'instances_list':instances_list})
	

def ShowInterfaces(request):
	db=database()
	return render(request,'nfv/interfaces.html',{'interface_list':db.keys()})

def StartInstance(request):
	()
# Create your views here.

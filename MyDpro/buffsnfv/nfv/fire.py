import subprocess

def FireCommand(cmd):
	#cmd=["docker","images","--format","'{{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.ID}}'"]
	process=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err= process.communicate()
	errorcode=process.returncode
	out=out.decode('UTF-8')
	OutDict={}
	outsplit=out.split('\n')
	for line in outsplit:
		if line:
			if line[0]=="'":
				line=line[1:]
			if line[len(line)-1]=="'":
				line=line[:(len(line)-1)]
			splitline=line.split('\t')
			OutDict[splitline[0]]=[]
			key=splitline.pop(0)
			
			for item in splitline:
				OutDict[key].append(item)
	return OutDict
				
			



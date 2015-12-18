import sys

filename=sys.argv[1]
seconds=float(sys.argv[2])
count=1

outstring=""
with open(filename,"r") as infile:
	subtitles=infile.read()
	lines=subtitles.split("\n")
	i=0
	while (i <len(lines)):
		outstring+=lines[i]+"\n"
		if lines[i].strip()==str(count):
			i+=1
			positions=lines[i].split("-->")
			start_time=True
			for position in positions:
				units=position.split(":")
				units[2]=units[2].split(",")
				s=int(units[2][0])+seconds
				units[2]=str(int(s)%60)+","+units[2][1]
				if (int(s)%60)<10:
					units[2]="0"+units[2]
				if s<0:
					minutes=((s+1)/60)-1
				else:
					minutes=int(s/60)
				m=int(units[1])+minutes
				units[1]=str(int(m)%60)
				if (int(m)%60)<10:
					units[1]="0"+units[1]
				if m<0:
					hours=((m+1)/60)-1
				else:
					hours=int(m/60)
				h=int(units[0])+hours
				units[0]=str(int(h))
				if (h)<10:
					units[0]="0"+units[0]
				for j in range(len(units)):
					outstring+=units[j]
					if (j==len(units)-1):
						if (start_time):
							start_time=False
							outstring+=" --> "
						else:
							outstring+="\n"
					else:
						outstring+=":"
			
			count+=1
		i+=1
with open(filename,"w") as outfile:
	outfile.write(outstring)
import sys
print(sys.argv)
fd = open(sys.argv[1])

i=0
c1=0
while(True):
    lines = fd.readline()
    line=lines.split(" ")
    for data in line:      
        if (data.find("warning") >= 0):
            c1 = c1+1
    if (len(lines)<=0):
        break       
i=i+1              
print(c1)
fd.close() 

fd = open(sys.argv [2])

i=0
c2=0
while(True):
    lines = fd.readline()
    line = lines.split(" ")
    for data in line:
        if (data.find("warning") >= 0 ):
            c2 = c2+1    
    if (len(lines)<=0):
        break 
i=i+1        
print(c2)
fd.close()
 
if (c1==c2):
    print("promoted")
elif(c1<c2):
    print(" not promoted")    
else:
   print("promoted")    
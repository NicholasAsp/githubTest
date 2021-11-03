import numpy as np
lines = []
with open('GA71TEndfix') as f:
    lines = f.readlines()

count = 0
for line in lines:
        count+=1
        if "mt444" in line:
            print(line)
            break
   
for i in range (count+3, count+773):
   linespl = lines[i].split(" ")
   doublsplit = np.array(linespl)
   fltsplit= doublsplit.astype(np,float)
   print(fltsplit)

    #'GA71TEndfix'

            

        

import numpy as np
f = open('CurrentMat.txt', "r")
CurrentMat = [[int(num) for num in line.split(' ')] for line in f]
f.close()

f = open('TP.txt', "r")
TP = [int(num) for num in f]
f.close()

f = open('TA.txt', "r")
TA = [int(num) for num in f]

A = np.ones((len(TA)))
B = np.ones((len(TA)))
Aprev = np.ones((len(TA)))
Bprev = np.ones((len(TA)))
while(1):
     
    for i in range(len(TA)):
        Sum=0
        for j in range(len(TA)):
            Sum+= B[j]*CurrentMat[i][j]
        A[i]=TP[i]/Sum

    for i in range(len(TA)):
        Sum=0
        for j in range(len(TA)):
            Sum+= A[j]*CurrentMat[j][i]
        B[i]=TA[i]/Sum  
    if (Aprev == A).all() and (Bprev == B).all():
        break
    else:
        Aprev = np.copy(A)
        Bprev = np.copy(B)      

CoeefMat = []
for a in A:
    temp = []
    for b in B:
        temp.append(a*b)
    CoeefMat.append(temp) 

futureMat=np.ones((len(TA),len(TA)))
for i in range(len(TA)):
    for j in range(len(TA)):
        futureMat[i][j]=CurrentMat[i][j]*CoeefMat[i][j]

futureMat=np.int16(futureMat)
f = open('FutureMat.txt', "w")
Output=str(futureMat).replace('[',"")
Output=Output.replace(']',"")
f.write(Output)

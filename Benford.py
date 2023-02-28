import math
import numpy as np
def benford(L):
    """
    This function recives a list of type float numbers and obtain a list with the 
    distribution of thees numbers according to the firts digit of each numbergit 
    (difrent from 0) in ascendinng order from 1 to 9 and a percentage of how 
    close is the original list of numbers to Benford distribution
    """
    Clasification=[[],[],[],[],[],[],[],[],[]]
    for i in range(len(L)):
        number = str(L[i])
        first_digit=''
        for j in number:
            if j!='0' and j!='.':
                first_digit = j
                break
            else:
                continue
        Clasification[int(j)-1].append(number)

    Theor_Distribution = []
    for n in range(1,10):
        Theor_Distribution.append(math.log(1+(1/n),10))

    Real_Distribution=[]
    total = 0
    for k in range(len(Clasification)):
        total = total + len(Clasification[k])
    for m in range(len(Clasification)):
        Real_Distribution.append(len(Clasification[m])/total)

    mse = 0

    actual,pred = np.array(Real_Distribution),np.array(Theor_Distribution)
    mse = np.sqrt(np.square(np.subtract(actual,pred))).mean()
    
    return Real_Distribution, str(round(mse*471.5869,2))+' %'
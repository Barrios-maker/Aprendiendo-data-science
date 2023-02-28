import math
import numpy as np
def benford(L):
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
        Real_Distribution.append(Clasification[m]/total)

    def mse (actual,pred):
        actual,pred = np.array(actual),np.array(pred)
        return np.sqrt(np.square(np.subtract(actual,pred)))
    

    return Real_Distribution, mse(Real_Distribution,Theor_Distribution)


'''
l=[0.1,0.0002,0.389,478,99,6675,147.2,563,135,456,510,289,267,111,0.3587]
print(benford(l))



Lista = [1459,0.0028,347,477,0.5,606,707,801,0.9,100]

print(benford(Lista))
'''
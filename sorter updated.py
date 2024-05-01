import numpy as np 
import matplotlib as plt
import hashlib as hs


Students= ['#23388102,Connolly,James ', '#23388102,Bickley Enda', '#23388102,Bursaz Andrei','#23388102,Bursan Andrei', '#23387102,AAirsan Andrei']
def insertionSortTest():
    for i in range(1,len(Students)):
        charVal = 10
        key=Students[i][charVal]
        j=i-1
        x = 0
       
        while x<len(key)-11:
            while j>=0 and key<Students[j][charVal]:
                Students[j+1]=Students[j]
                j=j-1
                charVal= charVal +1
                print("charval = ", charVal)
            print(len(key))
            x= x +1
            print("x = ", x)
                
                
    print(Students)

insertionSortTest()
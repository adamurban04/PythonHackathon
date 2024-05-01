import numpy as np 
import matplotlib as plt
import hashlib as hs


Students= ['#23388102,Connolly,James ', '#23388102,Buckley Enda', '#23388102,Birsan Andrei', '#23387102,AAirsan Andrei']
def insertionSortTest():
    for i in range(1,len(Students)):
        key=Students[i]
        j=i-1
        while j>=0 and key<Students[j][10]:
            Students[j+1]=Students[j]
            j=j-1
        Students[j+1]=key
    print(Students)

insertionSortTest()
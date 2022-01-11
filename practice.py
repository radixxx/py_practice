
#Arrays vs List 
import array as arr

My_Array=arr.array('i',[1,2,3,4])
My_list=[1,'abc',1.20]
print(My_Array[::-1])
print(My_list)

#Shyffle
from random import shuffle
x = ['Brown', 'Yellow', 'Red', 'Green']
shuffle(x)
print(x)

#Operations with arrays
import array as arr
Ma=arr.array('d', [1.1 , 2.1 ,3.1] )
Ma.append(3.4)
print(Ma)
Ma.extend([4.5,6.3,6.8])
print(Ma)
Ma.insert(2,3.8)
print(Ma)

#Tree
def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))    
pyfunc(9)
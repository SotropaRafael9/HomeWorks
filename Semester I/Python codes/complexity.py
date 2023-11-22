import random
from array import array
from asyncore import write
def GeneratingNumbers(Numbers):
    generate_numbers_array = []

    for i in range (0, Numbers):
        generate_numbers_array.append(random.randint(1,100))

    return generate_numbers_array


def SelectionSort(size, array, steps):
    Contor = 0
    for index in range (size): # O(n)
         min_index = index

         for CurrentIndex in range(index + 1, size): # O(N)
            if array[CurrentIndex] < array[min_index]:
                min_index = CurrentIndex
                Contor+= 1
                if Contor % steps == 0:
                    print(array)
                    

         (array[index], array[min_index])= (array[min_index],array[index])


def StoogeSort(array, length: int, left : int, steps, Contor):
    steps = steps + 1
    print(array)
    if length >= left:
        return 1
    
    if array[length] > array[left]:
        Auxiliar = array[length]
        array[length] = array[left]
        array[left] = Auxiliar
        

    if left - length + 1 > 2:
        MiddlePartOfArray = int((left - length + 1)/ 3)

        Contor += StoogeSort(array, length, (left - MiddlePartOfArray),steps,Contor)

        Contor += StoogeSort(array, length + MiddlePartOfArray, (left),steps,Contor)

        Contor += StoogeSort(array, length, (left - MiddlePartOfArray),steps,Contor)
    return 1
        

def Meniu():
    while True:
        print("0, Exit")
        print("1, Generating numbers")
        print("2, Sort the array by Selection Sort")
        print("3, Sort the array by Stooge Sort")
        Number = int(input("The Number that you choose: "))     
        match Number:
            case 0:
                break
            case 1: 
                LengthOfGenerateNumbers = int(input("How many numbers do you want array have?"))
                Array = GeneratingNumbers(LengthOfGenerateNumbers)
                GeneratingNumbers(LengthOfGenerateNumbers)
                print (Array)
            case 2:
                steps = int(input("How many steps do you want? "))
                if LengthOfGenerateNumbers == 0:
                    print ("Please generate first ")
                else:
                    SelectionSort(len(Array),Array,steps)
                    print (Array)
            case 3:
                steps = int(input("How many steps do you want? "))
                if LengthOfGenerateNumbers == 0:
                    print ("Please generate first ")
                else:
                    Contor = 0
                    StoogeSort(Array, 0,len(Array)-1,steps,Contor) 
                    print (Array)
   


if __name__== "__main__":
    Meniu()




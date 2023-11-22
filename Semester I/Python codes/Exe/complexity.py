import timeit
import random

def generate_list(Numbers):
    generate_numbers_array = []

    for i in range (0, Numbers):
        generate_numbers_array.append(random.randint(1, 100))
    return generate_numbers_array

#
# O(n ** 2) - in worst case 
# O(n ** 2) - in average case
# O(n ** 2) - in best case : is already sorted but we have to go through array O(n^2) times to be sure
# 1st : n-1
# 2nd : n-2
# 3rd : n-3
# .........
# (n - 1) + (n - 2) + (n - 3) + ...+ 1 = n(n-1)/2  witch is n ^ 2
def SelectionSort(array):
    for index in range (len(array)): # goes to 0 to size => n
         min_index = index # T(n)=1

         for CurrentIndex in range(index + 1, len(array)): # n ^ 2
            if array[CurrentIndex] < array[min_index]: # 
                min_index = CurrentIndex # T(n)=1
         (array[index], array[min_index]) = (array[min_index],array[index])
# Complexity in :
# O(n ^ (log 3 / log 1.5)) = O (n ^ 2.7) - worst case : when is already sorted we waste time to sort it again
# O(n ^ (log 3 / log 1.5)) = O (n ^ 2.7) - best case : when we have an unsorted array and we have to sort it
# O(n ^ (log 3 / log 1.5)) = O (n ^ 2.7) - average case : same as best case

def StoogeSort(array, length, left : int, steps, Contor):
    steps = steps + 1
    if length >= left:
        return 1
    
    if array[length] > array[left]:
        (array[length], array[left]) = (array[left], array[length])
        
    if left - length + 1 > 2:
        third_part_of_array = int((left - length + 1)/ 3)

        Contor += StoogeSort(array, length, (left - third_part_of_array),steps,Contor)

        Contor += StoogeSort(array, length + third_part_of_array, (left),steps,Contor)

        Contor += StoogeSort(array, length, (left - third_part_of_array),steps,Contor)
    return 1
def StoogeWrapper(list):
    StoogeSort(1, 1, 1, 1, 0)

def DO_TESTS(algorithms: list, list_lengths: list):
    for algorithm, algorithm_name in algorithms:
        print(f"{ algorithm_name }: ")

        for list_length in list_lengths:
            data = generate_list(list_length)
            t1 = timeit.default_timer()
            algorithm(data)
            t2 = timeit.default_timer()
            print(f"Executed for { list_length } numbers in { t2 - t1 } seconds.")

def Meniu():
    while True:
        print("0, Exit")
        print("1, Time StoogeSOrt and SelectionSort")
        Number = int(input("The Number that you choose: "))     
        match Number:
            case 0:
                break
            case 1:
                AlgorithList=[(StoogeWrapper, "Stooge Sort"),(SelectionSort, "Selection Sort")]
                LengthList=[1000, 2000, 3000, 5000]
                DO_TESTS(AlgorithList, LengthList)
                


if __name__== "__main__":
    Meniu()
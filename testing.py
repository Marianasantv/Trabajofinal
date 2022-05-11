list=[5,10,3,7,4,9,8]


# ### SORTING 


print("   ")
print ("Bubble sort: ")
print("   ")

from sorting.bubblesort import bubble_sort 


print("   ")

print("   ")
print ("Selection sort: ")
print("   ")

from sorting.selectionsort import selection_sort

print("   ")
print ("Bubble sort optimizado: ")
print("   ")

from sorting.bubblesortopt import bubble_sort_opt

print("   ")
print ("Insertion sort: ")
print("   ")

from sorting.insertionsort import selection_sort


# #### LISTAS 



print("   ")
print ("Largest number in list: ")
print("   ")

from listas.largestnumber import maximo
maximo ()


print("   ")
print ("Merge lists: ")
print("   ")

from listas.merge_list import combinar
combinar()



### BRUTE FORCE 

from bruteforce.sumaprimerosnumerosN import suma

print("   ")
print ("Suma de los primeros numeros n numeros: ")
print("   ")

# n = int(input("ingrese un numero n: "))

print("   ")
print ("Pin unlock:  ")
print("   ")



from bruteforce.pin_unlock import unlock

print("***Pin unlock***")
print(unlock("2812"))




print("   ")
print ("Divisores de N:  ")
print("   ")


from bruteforce.divisores import divisores


print("   ")
print ("linear Search:  ")
print("   ")


from Searching.busquedalineal import linear_search


print("input: " , [2, 92, 8, -4, 0])
print("output: " , linear_search([2, 92, 8, -4, 0] , 8))


print("   ")
print ("Binary Search:  ")
print("   ")

from Searching.busquedabinaria import binary_search

#### RECURSION 

print("   ")
print ("Cuenta regresiva:  ")
print("   ")


from recursion.countdown import regresive
print("***Cuenta regresiva***")
print(regresive(10+1))

print("   ")
print ("Fibonacci:  ")
print("   ")


from recursion.fibonacci import fibonacci
print(fibonacci(10))

print("   ")
print ("Suma de los primeros N numeros:  ")
print("   ")

from recursion.sum import sum
print(sum(10))


print("   ")
print ("Factorial de n:  ")
print("   ")

from recursion.factorial import fact

print("El factorial es: " , fact(8))

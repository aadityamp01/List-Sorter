# Implementation of Bubble Sort in Python
  
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
      
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

#Main Code
user_i = int(input("Enter a size of a list: "))
lst = []
for i in range(user_i):
    num = int(input("Enter a number: "))
    lst.append(num)
  
bubbleSort(lst) 

for i in range(len(lst)):
    num = (lst)

print("Sorted list is: ", num)


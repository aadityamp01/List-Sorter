# Selection sort in Python
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


# Main Code
#data = [-2, 45, 0, 11, -9]    ## Hard Code
user_i = int(input("Enter a size of an list: "))
lst = []
for i in range (user_i):
    num = int(input("Enter a number: "))
    lst.append(num)

size = len(lst)
selectionSort(lst, size)
print('Sorted list in Ascending Order:')
print(lst)

def reverse(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1): 
        reversed_arr.append(arr[i])
    return reversed_arr

lista = [1, 2, 3, 4, 5]
print(reverse(lista))  

def min(arr):
    menor = arr[0]  
    for num in arr:
        if num < menor:
            menor = num
    return menor


lista = [3, 7, 2, 9, 5]
print(min(lista))  

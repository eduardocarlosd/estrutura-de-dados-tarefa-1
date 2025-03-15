def max(arr):
    maior = arr[0]  
    for num in arr:
        if num > maior:
            maior = num
    return maior

lista = [3, 7, 2, 9, 5]
print(max(lista))  

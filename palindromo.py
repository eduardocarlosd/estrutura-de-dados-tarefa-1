def palindromo():
    palavra = input("Digite uma palavra: ").strip().lower()  
    if palavra == palavra[::-1]:  
        print("Palíndromo")
    else:
        print("Não é palíndromo")


palindromo()

#Escreva uma list comprehension em Python que crie uma lista contendo os números de 1 a 100,
#mas substitua os números divisíveis por 3 pela palavra "Fizz", 
#os números divisíveis por 5 pela palavra "Buzz" e os números divisíveis por ambos 3 e 5 pela palavra "FizzBuzz".

list = [
    'BuzzFizz' if x % 3 == 0 and x % 5 == 0 else 'Buzz' if x % 5 == 0 else 'Fizz' if x % 3 == 0 else x
    for x in range(1,101) 
    
]


print(list)
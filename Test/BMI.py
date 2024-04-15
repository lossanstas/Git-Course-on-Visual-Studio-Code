mass = float(input('Введите свой вес: '))
height = float(input('Введите свой рост в см.:'))/100
bmi = mass/height*2
print(mass)
print(height)
print(f'Ваш индекс массы тела: {bmi}')

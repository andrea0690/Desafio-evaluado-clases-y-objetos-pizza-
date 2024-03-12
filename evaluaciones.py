from pizza import Pizza
#  4.a
print(Pizza.proteina)
print(Pizza.vegetal_1)
print(Pizza.vegetal_2)
print(Pizza.masa)

#  4.b
print(Pizza.validar_opcion('salsa de tomate', ['salsa de tomate', 'salsa bbq'] ))

# 4.c
nueva_pizza = Pizza()
nueva_pizza.pedido()

#  4.d
print(f'La proteina elegida es: {nueva_pizza.proteina}')
print(f'Su primera opcion de vegetal es: {nueva_pizza.vegetal_1}')
print(f'Su segunda opcion de vegetal es: {nueva_pizza.vegetal_2}')
print(f'El tipo de masa de su pizza es: {nueva_pizza.masa}')

if nueva_pizza.valido :
    print('Su pizza es valida')
else:
    print('Su pizza no es valido')

# 4.e
print(Pizza.valido)
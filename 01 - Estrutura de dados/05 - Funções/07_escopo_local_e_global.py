salario = 1000


def salario_bonus(bonus, lista): 
    global salario 

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista_aux={lista_aux}")
    
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(50, lista)  #Escopo Global não é uma boa prática de programação, evite sempre que possível.

print(salario_com_bonus)
print(lista)
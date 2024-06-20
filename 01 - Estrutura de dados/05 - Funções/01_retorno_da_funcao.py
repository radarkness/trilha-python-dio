def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


def func_3():
    print("Oi Amiguinho") 
    return None 

print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(40))  # 39 e 41
print(func_3()) # Por padrão o Return é None

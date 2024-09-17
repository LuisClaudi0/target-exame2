def inverter_string(s):
    # Converta a string em uma lista de caracteres
    lista_caracteres = list(s)
    
    # Inicialize os índices de início e fim
    inicio = 0
    fim = len(lista_caracteres) - 1
    
    # Enquanto o índice de início for menor que o índice de fim
    while inicio < fim:
        # Troque os caracteres nos índices de início e fim
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        
        # Mova os índices em direção ao centro
        inicio += 1
        fim -= 1
    
    # Converta a lista de volta para uma string
    return ''.join(lista_caracteres)

# Teste a função
entrada = "teste"
resultado = inverter_string(entrada)
print("String original:", entrada)
print("String invertida:", resultado)

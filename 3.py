import json

def calcular_faturamento():
    # Lendo o arquivo JSON
    with open('C:/Users/Pc/Documents/Teste - Estágio Target 2/3/faturamento.json', 'r') as file:
        dados = json.load(file)
    
    # Filtrando e extraindo faturamentos válidos
    faturamentos = [item['faturamento'] for item in dados if item['faturamento'] > 0]

    if not faturamentos:
        print("Não há dados de faturamento válido para calcular.")
        return

    # Calculando o menor e o maior valor de faturamento
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    # Calculando a média mensal
    media_mensal = sum(faturamentos) / len(faturamentos)

    # Contando o número de dias com faturamento superior à média
    dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)

    # Exibindo os resultados
    print(f"Menor valor de faturamento: {menor_faturamento}")
    print(f"Maior valor de faturamento: {maior_faturamento}")
    print(f"Número de dias com faturamento superior à média: {dias_acima_media}")

# Chamada da função
calcular_faturamento()

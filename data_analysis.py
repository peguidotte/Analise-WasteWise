import time

def calcular_media_soma(lista):
    if len(lista) == 0:
        return 0
    else:
        soma = 0
        for elemento in lista:
            soma += elemento
        media = soma / len(lista)
        return media, soma
    
def identificar_maior(lista):
    maior_chave = None
    maior_valor = None
    for chave, valor in lista.items():
        if maior_valor is None or valor > maior_valor:
            maior_chave = chave
            maior_valor = valor
    return maior_chave, maior_valor

def obter_acesso(mensagem, mensagem_erro, *mensagens_acesso):
    acesso = input(mensagem)
    while acesso.lower() not in (mensagem.lower() for mensagem in mensagens_acesso):
        acesso = input(mensagem_erro)
    return acesso

# Considerando que receberiamos dados das lixeiras inteligentes feitas pela WasteWise usando Arduino para a matéria de Edge Computing.
# E que esses dados seriam usados para análise de impacto de campanhas de conscientização da população sobre reciclagem.
# Considere que o mapeamento dos dados seria feito por zonas da cidade de São Paulo.

# Dados fictícios para exemplo. (anual) 
total_lixo_zonas = {
    'norte': 1850000, 
    'sul': 2050000, 
    'oeste': 1400000,    
    'leste': 1700000 
}

lixo_reciclado_zonas = {
    'norte': 0.01, 
    'sul': 0.01, 
    'oeste': 0.02,    
    'leste': 0.01 
}

# Números aproximados. Fontes usadas:
# https://blog.brkambiental.com.br/descarte-de-lixo-2/
# https://eccaplan.com.br/blog/2021/03/03/27-mil-toneladas-dia-lixo-grande-sp/
# https://www1.folha.uol.com.br/cotidiano/2019/07/contra-tendencia-mundial-coleta-de-lixo-reciclavel-recua-14-em-sao-paulo.shtml
# https://g1.globo.com/globo-reporter/noticia/2022/03/19/sao-paulo-e-a-cidade-que-mais-produz-residuos-no-pais-12-mil-toneladas-por-dia-veja-dados.ghtml

total_lixo_cidade = calcular_media_soma(list(total_lixo_zonas.values()))[1] # 7 milhões de toneladas no ano de 2023 na cidade de sp
lixo_reciclado = total_lixo_cidade * calcular_media_soma(list(lixo_reciclado_zonas.values()))[1]  # % do total produzido que é reciclado
impacto_conscientizacao = 0.10 # 10% de lixo a menos produzido após campanha de conscientização por ano (um dos máximos atingido, segundo pesquisas.)
media_lixo_zonas = calcular_media_soma(list(total_lixo_zonas.values()))[0] # Média por zona

#Para essa analise de caso consideraremos os valores anuais de 2023 como base. Pegando somente a cidade de São Paulo.
total_lixo_zonas_inicial = dict(total_lixo_zonas)
total_reciclando_zonas_inicial = dict(lixo_reciclado_zonas)
total_lixo_cidade_incial = total_lixo_cidade
inicio = 2023
atual = 2023
cidade = "São Paulo"

print(f"\n{atual}:\n  Lixo produzido ({cidade}): {total_lixo_cidade} toneladas.")
for zona, lixo_zona in total_lixo_zonas.items():
    print(f"  Lixo produzido (Zona {zona}): {lixo_zona} toneladas. Equivale a {(lixo_zona / total_lixo_cidade)*100:.2f}% do total produzido.")    
print(f"  Lixo reciclado ({cidade}): {lixo_reciclado} toneladas.")
print(f"  Média de lixo produzido (Zonas): {media_lixo_zonas} toneladas.")

time.sleep(5)
print("\nNós da WasteWise acreditamos que a conscientização da população pode reduzir a produção de lixo em até 10% ao ano. Aumentando consequentemente a quantidade de lixo reciclado.")

acesso = obter_acesso("Digite 'avançar' para acessar o impacto da WasteWise: ", "Digite 'avançar' para acessar o impacto da WasteWise: ", "avançar")

while total_lixo_cidade > total_lixo_cidade_incial/2:
    
    #"maior chave"= [0] = zona_maior_lixo. / "maior valor"= [1] = maior_lixo.
    zona_maior_lixo, maior_lixo = identificar_maior(total_lixo_zonas)
    
    print(f"\nA região com a maior quantidade de lixo no ano de {atual} é a Zona {zona_maior_lixo} com {maior_lixo} toneladas.")
    print(f"No ano de {atual+1} será lá que focaremos as campanhas de conscientização.")
    time.sleep(3)
    
    #Guardando as variaveis para posterior comparação
    valor_anterior_zona = total_lixo_zonas[zona_maior_lixo]
    valor_anterior_cidade = total_lixo_cidade
    valor_anterior_zona_reciclado = lixo_reciclado_zonas[zona_maior_lixo]
    valor_anterior_cidade_reciclado = lixo_reciclado
    anterior = atual

    #Atualizando as variaveis
    atual += 1
    total_lixo_zonas[zona_maior_lixo] -= total_lixo_zonas[zona_maior_lixo] * impacto_conscientizacao
    total_lixo_cidade = calcular_media_soma(list(total_lixo_zonas.values()))[1]
    lixo_reciclado_zonas[zona_maior_lixo] *= 1.5
    lixo_reciclado = total_lixo_cidade * calcular_media_soma(list(lixo_reciclado_zonas.values()))[1]

    print(f"\nApós a campanha de conscientização do ano de {atual}:")
    print("\n Zona:")
    print(f"  A Zona {zona_maior_lixo} produziu {total_lixo_zonas[zona_maior_lixo]:.2f} toneladas de lixo.")
    print(f"  Isso é {total_lixo_zonas_inicial[zona_maior_lixo] - total_lixo_zonas[zona_maior_lixo]:.2f} toneladas a menos que em {inicio}.")
    print(f"  E reciclou {lixo_reciclado_zonas[zona_maior_lixo]*100:.2f}% do lixo produzido. Isso é {(lixo_reciclado_zonas[zona_maior_lixo] - total_reciclando_zonas_inicial[zona_maior_lixo])*100:.2f}% a mais que em {inicio}.\n")
    print("\n Cidade:")
    print(f"  O total de lixo produzido em {atual} após a campanha foi de {total_lixo_cidade:.2f} toneladas. {total_lixo_cidade_incial - total_lixo_cidade:.2f} toneladas a menos comparado a {inicio}.")
    print(f"  O total de lixo reciclado em {atual} após a campanha foi de {lixo_reciclado:.2f} toneladas. Isso é equivalente a {lixo_reciclado/total_lixo_cidade*100:.2f}% do total de lixo produzido.")
    
    acesso = obter_acesso(f"\nDigite '1' para informações mais detalhadas ou '2' para continuarmos a simulação do ano de {atual+1}: ", "Digite '1' para mais informações e '2' para simular o próximo ano.", "1", "2")
    if acesso == "1":
        print(f"\nInformações detalhadas do ano de {atual}:")
        
        #reatualizando a media de lixo produzido por zona somente caso seja necessário.
        media_lixo_zonas = calcular_media_soma(list(total_lixo_zonas.values()))[0]
        
        #Faz com que essa parte do código só seja executada se não for o primeiro ano
        if atual != inicio+1:
            print(f"\n  A Zona {zona_maior_lixo} produziu {total_lixo_zonas[zona_maior_lixo]:.2f} toneladas de lixo. {valor_anterior_zona - total_lixo_zonas[zona_maior_lixo]:.2f} toneladas a menos que em {anterior}.")
            print(f"  A Zona {zona_maior_lixo} recicla {lixo_reciclado_zonas[zona_maior_lixo]*100:.2f}% do lixo produzido. {(lixo_reciclado_zonas[zona_maior_lixo] - valor_anterior_zona_reciclado)*100:.2f}% a mais que em {anterior}.\n")
        
        print(f"  A media de lixo produzido por zona é de {media_lixo_zonas:.2f} toneladas.")
        print(f"  A Zona {zona_maior_lixo} produz {total_lixo_zonas[zona_maior_lixo] - media_lixo_zonas:.2f} toneladas a mais que a média de produção de todas as zonas.\n")
        
        for zona, lixo_zona in total_lixo_zonas.items():
            print(f"  Lixo produzido (Zona {zona}): {lixo_zona} toneladas.Equivale a {(lixo_zona / total_lixo_cidade)*100:.2f}% do total produzido.")
            print(f"  Percentual de reciclagem (Zona {zona}): {lixo_reciclado_zonas[zona]*100:.2f}%")

        acesso = obter_acesso(f"\nDigite 'avançar' para simular o próximo ano: ", "Digite 'avançar' para simular o próximo ano: ", "avançar")
        


        
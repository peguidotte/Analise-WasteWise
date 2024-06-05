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

# Dados fictícios para exemplo.
total_lixo_zonas = {
    'norte': 1000000, 
    'sul': 1500000, 
    'oeste': 500000,    
    'leste': 500000 
}

lixo_reciclado_zonas = {
    'norte': 0.01, 
    'sul': 0.01, 
    'oeste': 0.02,    
    'leste': 0.01 
}

# Números aproximados. Fontes usadas:
# https://www1.folha.uol.com.br/cotidiano/2019/07/contra-tendencia-mundial-coleta-de-lixo-reciclavel-recua-14-em-sao-paulo.shtml
# https://g1.globo.com/globo-reporter/noticia/2022/03/19/sao-paulo-e-a-cidade-que-mais-produz-residuos-no-pais-12-mil-toneladas-por-dia-veja-dados.ghtml

total_lixo_sp = calcular_media_soma(list(total_lixo_zonas.values()))[1] # 3.5 milhões de toneladas/ cidade
lixo_reciclado = total_lixo_sp * calcular_media_soma(list(lixo_reciclado_zonas.values()))[1]  # % do total produzido que é reciclado

media_lixo_zonas = calcular_media_soma(list(total_lixo_zonas.values()))[0] # Média por zona

print(f"No primeiro mês {total_lixo_zonas} de lixo foram produzidos em cada zona da cidade de São Paulo." 
      f"Fazendo com que a cidade produzisse um total de {total_lixo_sp} toneladas de lixo."
      f"A média de lixo produzido por zona foi de {media_lixo_zonas} toneladas."
      f"O total de lixo reciclado foi de {lixo_reciclado} toneladas.")

#"maior chave"= [0] = zona_maior_lixo. / "maior valor"= [1] = maior_lixo.
zona_maior_lixo, maior_lixo = identificar_maior(total_lixo_zonas)
print(f"A região com a maior quantidade de lixo é a Zona {zona_maior_lixo} com {maior_lixo} toneladas.")
print("Vamos começar a campanha de conscintização por lá!")

print(f"O lixo total de lixo reciclado foi {lixo_reciclado} toneladas. Isso é equivalente a {lixo_reciclado/total_lixo_sp*100:.2f}% do total de lixo produzido na cidade.")
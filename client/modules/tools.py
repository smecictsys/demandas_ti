def compilar_dados(dados):
    dados_compilados = []
    for dado in dados:
        if not dado[1] == None:
            if not dado[1] in dados_compilados:
                dados_compilados.append(dado[1])
    return dados_compilados

def list_to_dict(dados):
    lista_de_dicts = []
    for idx, dado in enumerate(dados):
        entrada, solicitante, tipo, direct, desc, status, data_final, atendido_por, tempo_finalizacao, obs = dado
        dados_temp = {
            "id":idx,
            "entrada":entrada,
            "solicitante":solicitante,
            "tipo":tipo,
            "direct":direct,
            "desc":desc,
            "status":status,
            "data_final":data_final,
            "atendido_por":atendido_por,
            "tempo_finalizacao":tempo_finalizacao,
            "obs":obs
        }
        lista_de_dicts.append(dados_temp)
    return lista_de_dicts

def list_format(dados:list)-> dict:
    dados_temp = {
            "entrada":dados[0],
            "solicitante":dados[1],
            "tipo":dados[2],
            "direct":dados[3],
            "desc":dados[4],
            "status":dados[5]
        }
    return dados_temp
import bcrypt

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

def hash_do_token(string_input:str)-> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(string_input.encode('utf-8'), salt)
    return hashed

def checar_token(token_reg, token_input):
    token_inserido = token_input.encode('utf-8')
    res = bcrypt.checkpw(token_inserido, token_reg)
    return res

def colab_format(colab:list)->dict:
    return {
        "nome":colab[1],
        "email":colab[2],
        "sala":colab[3],
        "numero_demandas":colab[4]
    }

def auth_error() -> str:
    msg = "Você não está autorizado a acessar esta área do sistema."
    return msg
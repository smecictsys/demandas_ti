class GSheetManager:
    _nome_planilha = None
    _nome_pagina = None
    def __init__(self, nome_da_planilha:str, nome_da_pagina:str, cliente_gspread:object) -> None:
        self._nome_planilha = nome_da_planilha
        self._nome_pagina = nome_da_pagina
        self._definir_cliente(cliente_gspread)
        self._ativar_planilha()

    def _definir_cliente(self, cliente_gspread:object):
        self._cliente = cliente_gspread
    
    def _ativar_planilha(self):
        self._planilha_ativa = self._cliente.open(self._nome_planilha).worksheet(self._nome_pagina)

    def obter_dados(self) -> list:
        return self._planilha_ativa.get_all_values()
    
    def inserir_dados(self, dados:list) -> bool:
        try:
            self._planilha_ativa.append_row(dados)
            return True
        except Exception as e:
            print(e)
            return False
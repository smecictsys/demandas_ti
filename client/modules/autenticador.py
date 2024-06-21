import json, os, gspread
from oauth2client.service_account import ServiceAccountCredentials

class Autenticador:
    _ESCOPOS = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive']
    _NOME_PLANILHA = "demandas"
    _file_path = "controledemandasti.json"

    def __init__(self) -> None:
        self._root_path = os.getcwd()
        self._ler()
        self.conectar()
        self.ativar_planilha(self._NOME_PLANILHA)

    def _ler(self) -> dict:
        with open(self._file_path, 'r', encoding='utf-8') as arquivo:
            self._credenciais_dict = json.load(arquivo)

    def obter_credenciais(self) -> dict:
        return self._credenciais_dict
    
    def conectar(self):
        self._credenciais = ServiceAccountCredentials.from_json_keyfile_name(self._file_path, self._ESCOPOS)
        self._cliente = gspread.authorize(self._credenciais)

    def ativar_planilha(self, nome_da_planilha):
        self._planilha_ativa = self._cliente.open(nome_da_planilha).worksheet('demandas')

    def obter_dados(self) -> list:
        return self._planilha_ativa.get_all_values()
    
    def inserir_dados(self, dados:list) -> bool:
        try:
            self._planilha_ativa.append_row(dados)
            return True
        except Exception as e:
            print(e)
            return False
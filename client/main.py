from modules.autenticador import Autenticador

auth = Autenticador()
dados = auth.obter_dados()
novos_dados = ['Thyéz de Oliveira', 'sala 15B', 'Troca de teclado']
res = auth.inserir_dados(novos_dados)
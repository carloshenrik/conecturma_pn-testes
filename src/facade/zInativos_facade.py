from model.zInativos_model import DbCemiterio

class ZinativosFacade:

    def __init__(self):

        self.inativos = DbCemiterio()

    def create_zInativos_atores_facade(self,desativados_atores):
        return self.inativos.fazer_os_de_cima(desativados_atores)

    def create_zInativos_estrutura_facade(self,desativado_estrutura):
        return self.inativos.inativos_estrutura(desativado_estrutura)

    def pesquisa_inativos_facade(self,nome):
        return self.inativos.pesquisa_inativo(nome)

    def reativar_usuario_facade(self,cem_id):
        return self.inativos.ressucitar_usuario(cem_id)

    def read_inativos_facade(self):

        return self.inativos.read_cemiterio()
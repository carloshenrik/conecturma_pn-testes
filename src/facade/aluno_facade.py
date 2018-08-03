from model.aluno_model import DbAluno


class AlunoFacade:

    def __init__(self):
        self.aluno = DbAluno()


    def create_aluno_facade(self, **kwargs):
        return self.aluno.create_aluno(**kwargs)


    def read_aluno_facade(self):
        return self.aluno.read_aluno()


    def update_aluno_facade(self, id, nome , senha):
        return self.aluno.update_aluno(update_id=id, nome=nome, senha=senha)


    def delete_aluno_facade(self, deletar_ids):
        return self.aluno.aluno_delete(deletar_ids)

    def search_aluno_id_facade(self, id_aluno):
        return self.aluno.search_aluno_id(id_aluno=id_aluno)

    def search_aluno_escola_facade(self, vinculo_escola):
        return self.aluno.search_aluno_by_escola(escola=vinculo_escola)


    def search_aluno_nome_facade(self, nome):
        return self.aluno.search_aluno_nome(nome)


    def search_aluno_nome_login_facade(self, nome_login):
        return self.aluno.search_aluno_nome_login(nome_login)


    def search_aluno_nome_objeto_facade(self, nome):
        return self.aluno.pesquisa_aluno_objeto(nome)


    def aluno_in_turma_facade(self, id_aluno, vinculo_turma):
        return self.aluno.alunos_in_turma(id_aluno=id_aluno, vinculo_turma=vinculo_turma)


    def compra_item_facade(self, id_usuario, id_item):
        return self.aluno.comprar_item(id_usuario=id_usuario, id_item=id_item)


    def ver_item_comprado_facade(self, id_usuario):
        return self.aluno.ver_itens_comprados(id_usuario)


    def equipar_item_facade(self, id, itens):
        return self.aluno.equipar_item(id_usuario=id, itens=itens)


    def avatar_facade(self, id):
        return self.aluno.avatar(id)


    def anotacoes_aluno_facade(self, usuario_id, mensagem):
        return self.aluno.anotacoes_do_aluno(usuario_id, mensagem)


    def read_anotacoes_aluno_facade(self, usuario_id):
        return self.aluno.ver_anotacoes_aluno(usuario_id)


    def search_aluno_by_rede_facade(self, vinculo_rede):
        return self.aluno.search_aluno_by_rede(vinculo_rede=vinculo_rede)


    def search_aluno_by_turma_facade(self, vinculo_turma):
        return self.aluno.search_aluno_by_turma(vinculo_turma=vinculo_turma)

    def gravar_premiacao(self,user_id,premiacao):
        return self.aluno.gravar_premiacao(user_id,premiacao)

    def armazenar_ultimo_jogo_jogado(self, id_aluno, jogo):
        return self.aluno.armazenar_ultimo_jogo_jogado(id_aluno, jogo)

    def ultimo_oa_jogado_facade(self, id_aluno):
        return self.aluno.ultimo_oa_jogado(id_aluno)

    def get_medalhas_facade(self, id_aluno):
        return self.aluno.get_medalhas(id_aluno=id_aluno)

    def apagartudo(self):
        return self.aluno.apagartudo()


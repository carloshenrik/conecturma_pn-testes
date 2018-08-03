from walrus import *
from control.dicionarios import TIPO_ESTRUTURA

db = Database(host='localhost', port=6379, db=0)


class DbEstrutura(Model):
    __database__ = db
    id = AutoIncrementField(primary_key=True)
    nome = TextField(index=True)
    tipo_estrutura = TextField(fts=True, index=True)
    telefone = TextField(default='0')

    vinculo_rede = TextField(fts=True, default='0')
    vinculo_escola = TextField(fts=True, default='0')
    vinculo_professor_turma = TextField(fts=True, default='0')
    cnpj = TextField(default='0')

    logradouro = TextField(default='0')
    bairro = TextField(default='0')
    municipio = TextField(default='0')
    cep = TextField(default='0')
    endereco = TextField(default='0')
    numero = TextField(default='0')
    estado = TextField(default='0')
    uf = TextField(default='0')
    complemento = TextField(default='0')

    sigla_oa = TextField(fts=True, default='0')
    unidade=TextField(fts=True, default='0')

    tipo_oa=TextField(fts=True, default='0')

    sigla_descritor = TextField(fts=True, default='0')
    nome_descritor = TextField(fts=True, default='0')
    descricao_descritor = TextField(fts=True, default='0')

    disciplina = TextField(fts=True, default='0')
    aventura = TextField(fts=True, default='0')

    quem_criou = TextField(default='0')
    serie = TextField(default='0')

    tipo_item = TextField(default='0')
    preco = IntegerField(default=0)

    tipo_medalha = TextField(default='0')
    descricao = TextField(default='0')
    descricao_completa = TextField(default='0')

    nome_usuario = TextField(default='0')
    tipo_usuario = TextField(default='0')
    data_acesso = DateTimeField(default=datetime.datetime.now)

    anotacoes_observador_turma = ListField()
    anotacoes_observador_escola = ListField()
    anotacoes_observador_rede = ListField()


    def create_estrutura(self, **kwargs):
        return self.create(**kwargs)

    def read_estrutura(self, tipo_estrutura):
        listas = []

        for lista in DbEstrutura.query((DbEstrutura.tipo_estrutura == tipo_estrutura), order_by=DbEstrutura.id):
            listas.append(vars(lista)["_data"])

        return listas

    def ja_possui_item(self, usuario_logado):
        from model.aluno_model import DbAluno

        usuario = DbAluno()
        # [x.decode('utf-8') for x in usuario.i]
        itens_usuario = usuario.ver_itens_comprados(id_usuario=int(usuario_logado))
        itens = [str(y['id']) for y in self.read_estrutura(tipo_estrutura=TIPO_ESTRUTURA['item'])]
        lista_teste = [z for z in itens if z not in itens_usuario]
        return lista_teste

    def search_estrutura(self, tipo_estrutura, nome):

        lista_dic={}

        for lista in DbEstrutura.query((DbEstrutura.tipo_estrutura == tipo_estrutura) and (DbEstrutura.nome == nome)):
            lista_dic=vars(lista)["_data"]

        return lista_dic

    def search_estrutura_id(self, id):
        if id != '0':
            lista = DbEstrutura.load(int(id))
            lista_dic = vars(lista)["_data"]
        else:
            lista_dic = dict(
                nome=" "
            )

        return lista_dic

    def search_escola_by_rede(self, vinculo_rede):
        escola = []
        for lista in DbEstrutura.query((DbEstrutura.tipo_estrutura == '2') and (DbEstrutura.vinculo_rede == vinculo_rede),
                                       order_by=self.nome):
            escola.append(vars(lista)["_data"])

        return escola

    def search_turma_by_rede(self, vinculo_rede):
        turma = []
        for lista in self.query((DbEstrutura.tipo_estrutura == '3') and (DbEstrutura.vinculo_rede == vinculo_rede),
                                order_by=DbEstrutura.nome):
            turma.append(vars(lista)["_data"])

        return turma

    def search_turma_by_escola(self, vinculo_escola):
        turma = []
        for lista in self.query((DbEstrutura.tipo_estrutura == '3') and (DbEstrutura.vinculo_escola == vinculo_escola),
                                order_by=DbEstrutura.nome):
            turma.append(vars(lista)["_data"])

            return turma

    def search_oa_by_type_and_aventura(self, aventura ,disciplina):
        oas = []
        for i in self.query((DbEstrutura.tipo_estrutura == '7') & (DbEstrutura.disciplina == disciplina) &
                            (DbEstrutura.aventura == aventura), order_by=DbEstrutura.sigla_oa):
            oas.append(vars(i)["_data"])

        return oas

    def update_estrutura(self, update_id, nome='0', telefone='0', vinculo_rede='0', cep='0', endereco='0',
                         numero='0', cidade='0',
                         estado='0', uf='0', serie='0', tipo_item='0', preco=None, tipo_medalha=None,
                         descricao=None,
                         descricao_completa=None, nome_usuario=None, tipo_usuario=None, vinculo_escola=None,
                         vinculo_professor_turma="0"):
        estrutura = self.load(update_id)
        [setattr(estrutura, parametro, valor) for parametro, valor in locals().items() if valor]
        estrutura.save()

    def func_anotacoes_estrutura_turma(self, id_estrutura, mensagem):
        estrutura = self.load(id_estrutura)
        estrutura.anotacoes_estrutura_turma.append(mensagem)
        estrutura.save()

    def func_anotacoes_estrutura_escola(self, id_estrutura, mensagem):
        estrutura = self.load(id_estrutura)
        estrutura.anotacoes_estrutura_escola.append(mensagem)
        estrutura.save()

    def func_anotacoes_estrutura_rede(self, id_estrutura, mensagem):
        estrutura = self.load(id_estrutura)
        estrutura.anotacoes_estrutura_rede.append(mensagem)
        estrutura.save()

    # def delete_estrutura_test(self, deletar_ids):
    #
    #     for deletar_ids in deletar_ids:
    #         usuario = self.load(deletar_ids)
    #         usuario.delete(deletar_ids)

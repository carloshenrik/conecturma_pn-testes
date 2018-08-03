from walrus import *
from model.estrutura_model import *
from model.aluno_model import DbAluno
from model.observador_model import *

# from facade.Facade_main import *
db = Database(host='localhost', port=6379, db=0)
# aluno = DbAluno()
# observador = DbObservador()
# facade=Facade()
"""lista de informaçoes
tipos :
0-adm
1-gestor
2-diretor
3-professor
4-responsavel
5-responvadel
6-aluno
7-aluno varejo

tipo_estrutura:
1-rede
2-escola
3-turma
4-item
5-medalha

tipo_itens :
1-cores
2-rosto
3-acessorio
4-corpo"""


class DbCemiterio(Model):
    __database__ = db
    id = AutoIncrementField(primary_key=True)
    matricula = TextField()

    nome = TextField(fts=True, index=True)
    senha = TextField(fts=True)

    tipo_usuario = TextField(default='0')
    tipo_aluno = TextField(default='0')

    itens_comprados = ListField()

    cor = TextField(default='0')
    rosto = TextField(default='0')
    acessorio = TextField(default='0')
    corpo = TextField(default='0')

    tipo_item = TextField(fts=True, default='0')
    preco = TextField(default='0')

    pontos_de_vida = IntegerField(default='0')
    pontos_de_moedas = IntegerField(default='0')

    anotacoes_aluno = ListField()

    vinculo_rede = TextField(default='0')
    vinculo_escola = TextField(default='0', fts=True)
    vinculo_turma = TextField(fts=True, index=True, default='0')
    tipo_estrutura = TextField(fts=True, index=True)

    telefone = TextField(default='0')
    cep = TextField(default='0')
    endereco = TextField(default='0')
    numero = TextField(default='0')
    estado = TextField(default='0')
    uf = TextField(default='0')

    quem_criou = TextField(default='0')
    serie = TextField(default='0')

    tipo_medalha = TextField(default='0')
    descricao = TextField(default='')
    descricao_completa = TextField(default='0')
    nome_usuario = TextField(default='0')

    data_acesso = DateTimeField(default=datetime.datetime.now)
    anotacoes_estrutura = ListField()

    cpf = TextField(default='0')
    email = TextField(default='0')

    data_ultimo_login = TextField(default='')
    anotacoes_observador = ListField()

    def desativar_atores(self, atores_id):
        for atores_id in atores_id:
            self.desativar_um_objeto(vars(atores_id)['_data'])

    def complemento_create(self, ator, cemiterio_nome):
        usuario = ator

        inativar = self.pesquisa_inativo(cemiterio_nome)
        inativado = self.load(inativar.id)

        try:
            if usuario.anotacoes_aluno is not None:
                for x in range(0, len(usuario.anotacoes_aluno)):
                    inativado.anotacoes_aluno.append(usuario.anotacoes_aluno[x])
            else:
                pass
            if usuario.itens_comprados is not None:
                for y in range(0, len(usuario.itens_comprados)):
                    inativado.itens_comprados.append(usuario.itens_comprados[y])
            else:
                pass

            """nao esquecer de acrescentar as pontuaçoes dos jogos"""
            if inativar.all() == usuario.all():
                    # matricula == usuario.matricula and inativar.nome == usuario.nome and \
                    # inativar.senha == usuario.senha and inativar.tipo_aluno == usuario.tipo_aluno and inativar.tipo_aluno == usuario.tipo_aluno and \
                    # inativar.cor == usuario.cor and inativar.rosto == usuario.rosto and \
                    # inativar.acessorio == usuario.acessorio and inativar.corpo == usuario.corpo and \
                    # inativar.pontos_de_vida == usuario.pontos_de_vida and \
                    # inativar.pontos_de_moedas == usuario.pontos_de_moedas and \
                    # inativar.vinculo_escola == usuario.vinculo_escola \
                    # and inativar.vinculo_turma == usuario.vinculo_turma:

                inativar.save()
                usuario.delete(usuario.id)

            else:
                print("L134-161 CEMITERIO", inativar.nome, usuario.nome,
                      inativar.vinculo_turma, usuario.vinculo_turma, usuario.tipo_aluno)
                print("vish , n foi ")
                return False
        except AttributeError:
            print('inativar', inativar, usuario)
            if inativar.nome == usuario.nome and inativar.senha == usuario.senha and inativar.telefone == usuario.telefone and \
                    inativar.cpf == usuario.cpf and inativar.email == usuario.email and inativar.tipo_usuario == usuario.tipo and \
                    inativar.vinculo_rede == usuario.vinculo_rede and inativar.vinculo_escola == usuario.vinculo_escola and \
                    inativar.data_ultimo_login == usuario.data_ultimo_login:
                usuario.delete(usuario.id)
                print("deletou usuario")
                return True
            else:
                # print("L163 cemiterio", inativar.data_ultimo_login, usuario.data_ultimo_login)
                print("n deletou usuario L163 cem",inativar.tipo_usuario, usuario.tipo ,
                      inativar.vinculo_rede, usuario.vinculo_rede and inativar.vinculo_escola == usuario.vinculo_escola ,
                      inativar.data_ultimo_login == usuario.data_ultimo_login)
                return False

    def fazer_os_de_cima(self, lista_inativados):
        self.desativar_atores(lista_inativados)
        x = len(lista_inativados)
        while lista_inativados:
            x = 0
            paradas = lista_inativados[x]
            self.complemento_create(paradas, paradas.nome)
            lista_inativados.pop(0)

    def pesquisa_inativo(self, nome_cem):

        usuario = []
        for pesquisa in DbCemiterio.query(DbCemiterio.nome == nome_cem):
            usuario = pesquisa
        return usuario

    def deletar_cem(self, nome):
        pessoa = self.pesquisa_inativo(nome)
        isto = self.aluno.pesquisa_aluno(nome)
        if isto == []:
            isto = self.observador.search_observador_inativos(nome)
            fenix = self.observador.load(isto.id)
        else:
            fenix = self.aluno.load(isto.id)
        antigo_morto = self.load(pessoa.id)
        try:
            if fenix.matricula == antigo_morto.matricula and fenix.nome == antigo_morto.nome and \
                    fenix.senha == antigo_morto.senha and fenix.tipo_aluno == antigo_morto.tipo_usuario and \
                    fenix.cor == antigo_morto.cor and fenix.rosto == antigo_morto.rosto and \
                    fenix.acessorio == antigo_morto.acessorio and fenix.corpo == antigo_morto.corpo and \
                    fenix.pontos_de_vida == antigo_morto.pontos_de_vida and \
                    fenix.pontos_de_moedas == antigo_morto.pontos_de_moedas and \
                    fenix.vinculo_escola == antigo_morto.vinculo_escola \
                    and fenix.vinculo_turma == antigo_morto.vinculo_turma:
                print("aluno morto deletado L204")
                antigo_morto.delete(antigo_morto.id)
                pessoa.delete(pessoa.id)
                return True
            else:
                print("algo de errado nao esta certo")
        except AttributeError:
            if fenix.nome == antigo_morto.nome and fenix.senha == antigo_morto.senha and fenix.telefone == antigo_morto.telefone and \
                    fenix.cpf == antigo_morto.cpf and fenix.email == antigo_morto.email and fenix.tipo == antigo_morto.tipo_usuario and \
                    fenix.vinculo_rede == antigo_morto.vinculo_rede and fenix.vinculo_escola == antigo_morto.vinculo_escola and \
                    fenix.data_ultimo_login == antigo_morto.data_ultimo_login:
                antigo_morto.delete(antigo_morto.id)
                print("sucesso,obs")
                return True
            else:
                print("nao deletou o antigo morto")
                return False

    def ressucitar_usuario(self, user):
        """USER SERIA EM FORMATO <Dbcemiterio: x >"""
        zumbi = user.load(user.id)
        atores_id = user.load(user.id)
        # if DbAluno.create(**{k: getattr(zumbi, k) for k in dir(zumbi)}):
        if atores_id.tipo_usuario == "6" or atores_id.tipo_usuario == "7":
            if self.aluno.restaurar_aluno(matricula=atores_id.matricula, nome=atores_id.nome, senha=atores_id.senha,
                                          tipo_aluno=atores_id.tipo_usuario, cor=atores_id.cor,
                                          rosto=atores_id.rosto, acessorio=atores_id.acessorio, corpo=atores_id.corpo,
                                          pontos_de_vida=atores_id.pontos_de_vida,
                                          pontos_de_moedas=atores_id.pontos_de_moedas,
                                          desempenho_aluno_j1=atores_id.desempenho_aluno_j1,
                                          desempenho_aluno_j2=atores_id.desempenho_aluno_j2,
                                          vinculo_escola=atores_id.vinculo_escola,
                                          vinculo_turma=atores_id.vinculo_turma):
                self.deletar_cem(atores_id.nome)
                return True
            else:

                return False
        else:
            if self.observador.recriar_observador(atores_id.nome, atores_id.senha, atores_id.tipo_usuario,
                                                  atores_id.vinculo_escola,
                                                  atores_id.data_ultimo_login, atores_id.telefone, atores_id.cpf,
                                                  atores_id.email, atores_id.vinculo_rede):
                self.deletar_cem(zumbi.nome)
                return True
            else:
                return False

    def inativos_estrutura(self, estruturi):
        estrutura = self.load(estruturi.id)
        self.create(tipo_estrutura=estrutura.tipo_estrutura, telefone=estrutura.telefone,
                    vinculo_rede=estrutura.vinculo_rede, vinculo_escola=estrutura.vinculo_escola, cep=estrutura.cep,
                    endereco=estrutura.endereco, numero=estrutura.numero, estado=estrutura.estado, uf=estrutura.uf,
                    quem_criou=estrutura.quem_criou, serie=estrutura.serie, tipo_item=estrutura.tipo_item,
                    preco=estrutura.preco, tipo_medalha=estrutura.tipo_medalha, descriçao=estrutura.descricao,
                    descricao_completa=estrutura.descricao_completa, nome_usuario=estrutura.nome_usuario,
                    tipo_usuario=estrutura.tipo_usuario, data_acesso=estrutura.data_acesso,
                    anotacoes_estrutura=estrutura.anotacoes_estrutura)

    def read_cemiterio(self):
        inativos = []
        for read in DbCemiterio.all():
            inativos.append(dict(id=read.id, nome=read.nome, senha=read.senha, tipo_usuario=read.tipo_usuario,
                                 itens_comprados=len(read.itens_comprados), cor=read.cor, rosto=read.rosto,
                                 acessoio=read.acessorio, corpo=read.corpo,
                                 pontos_de_vida=read.pontos_de_vida, pontos_de_moedas=read.pontos_de_moedas,
                                 vinculo_escola=read.vinculo_escola,tipo_aluno=read.tipo_aluno,
                                 anotaçoes_aluno=len(read.anotacoes_aluno), vinculo_turma=read.vinculo_turma,
                                 tipo_estrutura=read.tipo_estrutura, telefone=read.telefone,
                                 vinculo_rede=read.vinculo_rede, cep=read.cep, endereco=read.endereco,
                                 numero=read.numero, estado=read.estado, uf=read.uf, quem_criou=read.quem_criou,
                                 serie=read.serie, tipo_item=read.tipo_item, preco=read.preco,
                                 tipo_medalha=read.tipo_medalha, descricao=read.descricao,
                                 descricao_completa=read.descricao_completa, nome_usuario=read.nome_usuario,
                                 data_acesso=read.data_acesso
                                 , anotacoes_estrutura=len(read.anotacoes_estrutura), cpf=read.cpf, email=read.email,
                                 data_ultimo_login=read.data_ultimo_login,
                                 anotacoes_observador=len(read.anotacoes_observador)))

        return inativos

    def desativar_ator(self, nome, matricula='0', senha='0', tipo_usuario='0', cor='0', rosto='0', acessorio='0',
                       corpo='0',
                       pontos_de_vida='0', pontos_de_moedas='0', vinculo_escola='0', vinculo_turma='0',
                       tipo_estrutura='0', telefone='0', vinculo_rede='0', cep='0', endereco='0', numero='0',
                       estado='0', uf='0', quem_criou='0', serie='0', tipo_item='0', preco='0', tipo_medalha='0',
                       descricao='0', descricao_completa='0', nome_usuario='0', data_acesso=datetime.datetime.now,
                       cpf='0', email='0', tipo='0', data_ultimo_login='0'):
        [setattr(self.create(), parametro, valor) for parametro, valor in locals().items()]
        print("quee")

    def desativar_um_objeto(self, objetoo):
        print('CMl311', objetoo)
        if self.create(**objetoo):
            print("sucesso")
        else:
            print('nao foi')
            return False

# def deletar_estrutura(self,estrutura_nome,tipo):
#
#     morto=self.pesquisa_inativo(estrutura_nome)
#     vivo=DbEstrutura.search_estrutura()
#     if morto.tipo_estrutura == vivo.tipo_estrutura, morto.telefone == vivo.telefone,
#     morto.vinculo_rede == vivo.vinculo_rede, morto.vinculo_escola == vivo.vinculo_escola, morto.cep == vivo.cep,
#     morto.endereco == vivo.endereco, morto.numero == vivo.numero, morto.estado == vivo.estado, morto.uf == vivo.uf,
#     morto.quem_criou == vivo.quem_criou, morto.serie == estrutura.serie, tipo_item == estrutura.tipo_item,
#     preco = estrutura.preco, tipo_medalha = estrutura.tipo_medalha, descriçao = estrutura.descricao,
#     descricao_completa = estrutura.descricao_completa, nome_usuario = estrutura.nome_usuario,
#     tipo_usuario = estrutura.tipo_usuario, data_acesso = estrutura.data_acesso,
#     anotacoes_estrutura = estrutura.anotacoes_estrutura:

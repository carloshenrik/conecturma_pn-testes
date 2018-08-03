from bottle import redirect, response, request
from datetime import datetime
from control.dicionarios import *
from facade.facade_main import Facade
from passlib.hash import sha512_crypt

"""Constante para a key de hash temporariamente"""

KEY_HASH = 'gu3 j0st0çur4'


class Login_Observador(object):

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def login(self):
        facade = Facade()

        hash = self.gerar_hash()
        response.set_cookie("KIM", hash, path='/', secret=KEY_HASH)

        observador_logado = facade.search_observador_email_facade(email=self.email)
        if observador_logado != None:
            if observador_logado['email'] == self.email:
                if sha512_crypt.verify(self.senha, observador_logado['senha']):
                    response.set_cookie("BUMBA", observador_logado, path='/', secret=hash)
                    now = datetime.now()
                    facade.login_date_facade(observador_logado['id'], now)
                    facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['historico'],
                                                   nome_usuario=observador_logado['nome'],
                                                   tipo_usuario=observador_logado['tipo'])
                    return PAGINA_INICIAL[tipo_observador(observador_logado['tipo'])]
                else:
                    return '/'
            else:
                return '/'
        else:
            print("Usuario não encontrado !")

    def gerar_hash(self):
        """
        Usa um algoritmo aleatório para criar um numero de matricula de 5 números

        :return: O numero da matricula do aluno
        """
        from random import randrange

        hash = []
        for i in range(0, 5):
            hash.append(randrange(1, 9))
        matricula = ''.join(str(x) for x in hash)
        return matricula


class Login_Aluno(object):
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def login(self):
        facade = Facade()
        hash = self.gerar_hash()
        aluno = facade.search_aluno_nome_login_facade(nome_login=self.nome)
        response.set_cookie("KIM", hash, path='/', secret=KEY_HASH)
        if aluno['nome_login'] == self.nome:
            if aluno['senha'] == self.senha:
                aluno_logado = dict(
                    id=aluno['id'],
                    nome=aluno['nome'],
                    tipo=aluno['tipo_aluno'],
                    vinculo_rede=aluno['vinculo_rede'],
                    vinculo_escola=aluno['vinculo_escola'],
                    vinculo_turma=aluno['vinculo_turma'],
                    # ultimo_oa = aluno['ultimo_objeto_aprendizagem'],
                    ultima_unidade= aluno['ultima_unidade'],
                    ultima_aventura= aluno['ultima_aventura'],
                    moeda=aluno['pontos_de_moedas'],
                    xp=aluno['pontos_de_vida']
                )
                response.set_cookie("BUMBA", aluno_logado, path='/', secret=hash)
                return PAGINA_INICIAL[tipo_observador(aluno_logado['tipo'])]
        else:
            return '/'


    def gerar_hash(self):
        """
        Usa um algoritmo aleatório para criar um numero de matricula de 5 números

        :return: O numero da matricula do aluno
        """
        from random import randrange

        hash = []
        for i in range(0, 5):
            hash.append(randrange(1, 9))
        matricula = ''.join(str(x) for x in hash)
        return matricula

def update_cookie(premio):
    banana = request.get_cookie("KIM", secret=KEY_HASH)
    que = request.get_cookie("BUMBA", secret=banana)

    que['moeda'] = premio['moedas']
    que['xp'] = premio['xp']
    return PAGINA_INICIAL[tipo_observador(que['tipo'])]

def usuario_logado():
    banana = request.get_cookie("KIM", secret=KEY_HASH)
    que = request.get_cookie("BUMBA", secret=banana)

    return que


def algum_usuario_logado(function):
    def decorator(*args, **kwargs):
        banana = request.get_cookie("KIM", secret=KEY_HASH)
        que = request.get_cookie("BUMBA", secret=banana)
        if que and banana:
            redirect(PAGINA_INICIAL[tipo_observador(que['tipo'])])
        else:
            return function(*args, **kwargs)

    return decorator


def permissao(quem_tem_permissao):
    def observador(function):
        def decorator(*args, **kwargs):
            banana = request.get_cookie("KIM", secret=KEY_HASH)
            que = request.get_cookie("BUMBA", secret=banana)
            if banana and que:
                if int(TIPO_USUARIOS[quem_tem_permissao]) >= int(que['tipo']):
                    return function(*args, **kwargs)
                else:
                    redirect('/error403')
            else:
                redirect('/')

        return decorator

    return observador


def tipo_observador(tipo):
    # return {
    #     '0': 'administrador',
    #     '1': 'gestor',
    #     '2': 'diretor',
    #     '3': 'professor',
    #     '4': 'responsavel',
    #     '5': 'responsavel_varejo',
    #     '6': 'aluno',
    #     '7': 'aluno_varejo',
    # }
    if tipo == '0':
        return 'administrador'
    elif tipo == '6':
        return 'aluno'
    elif tipo == '7':
        return 'aluno_varejo'
    elif tipo == '3':
        return 'professor'
    elif tipo == '5':
        return 'responsavel_varejo'
    elif tipo == '4':
        return 'responsavel'
    elif tipo == '2':
        return 'diretor'
    elif tipo == '1':
        return 'gestor'

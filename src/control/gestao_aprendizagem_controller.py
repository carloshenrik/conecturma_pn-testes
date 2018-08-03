from bottle import route, view, request, redirect, get, template
from facade.facade_main import Facade
from passlib.hash import sha512_crypt
import random


from control.classes.permissao import usuario_logado, permissao
from control.dicionarios import PAGINA_DE_CADASTRO_POR_TIPO, TIPO_USUARIOS_ID, TIPO_USUARIOS, TIPO_ESTRUTURA, SERIE

facade = Facade()


@permissao('responsavel_varejo')
def view_gestao_aprendizagem():
    observador = usuario_logado()
    return dict(usuario=observador['nome'], tipo=observador['tipo'])

@permissao('professor')
def view_usuario_index():
    """
    mostra todos os usuarios , escolas e redes cadastradas
    :return:
    """
    observador = usuario_logado()
    usuario = controller_index_usuario(observador)
    rede = facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['rede'])
    escola = facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['escola'])
    turma = facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['turma'])

    return dict(observador_tipo=observador['tipo'], usuarios=usuario, redes=rede, escolas=escola, turmas=turma)


@permissao('professor')
def controller_index_usuario(observador):
    if observador['tipo'] == TIPO_USUARIOS['administrador']:
        return lista_de_usuarios_caso_observador_for_administrador()
    elif observador['tipo'] == TIPO_USUARIOS['professor']:
        return lista_de_usuarios_caso_observador_for_professor(observador['vinculo_turma'])
    elif observador['tipo'] == TIPO_USUARIOS['diretor']:
        return lista_de_usuarios_caso_observador_for_diretor(observador['vinculo_escola'])
    elif observador['tipo'] == TIPO_USUARIOS['gestor']:
        return lista_de_usuarios_caso_observador_for_gestor(observador['vinculo_rede'])


@permissao('administrador')
def lista_de_usuarios_caso_observador_for_administrador():
    usuario = []
    aluno = facade.read_aluno_facade()
    observador = facade.read_observador_facade()
    for a in aluno:
        a['email'] = ''
        a['vinculo_rede'] = get_nome_rede(a['vinculo_rede'])
        a['vinculo_escola'] = get_nome_escola(a['vinculo_escola'])
        a['vinculo_turma'] = get_nome_turma(a['vinculo_turma'])
        a['tipo'] = TIPO_USUARIOS_ID[a['tipo']]
        usuario.append(a)

    for o in observador:
        if o['tipo'] != '0':
            o['vinculo_rede'] = get_nome_rede(o['vinculo_rede'])
            o['vinculo_escola'] = get_nome_escola(o['vinculo_escola'])
            o['vinculo_turma'] = get_nome_turma(o['vinculo_turma'])
            o['tipo'] = TIPO_USUARIOS_ID[o['tipo']]
            usuario.append(o)
    return usuario


@permissao('gestor')
def lista_de_usuarios_caso_observador_for_gestor(vinculo_rede):
    usuario = []

    aluno = facade.search_aluno_by_rede_facade(vinculo_rede)
    observador = facade.search_observador_by_rede_facade(vinculo_rede=vinculo_rede)

    for a in aluno:
        a['email'] = ""
        a['vinculo_rede'] = get_nome_rede(a['vinculo_rede'])
        a['vinculo_escola'] = get_nome_escola(a['vinculo_escola'])
        a['vinculo_turma'] = get_nome_turma(a['vinculo_turma'])
        a['tipo'] = TIPO_USUARIOS_ID[a['tipo']]
        usuario.append(a)
    for o in observador:
        if o['tipo'] != '0':
            o['vinculo_rede'] = get_nome_rede(o['vinculo_rede'])
            o['vinculo_escola'] = get_nome_escola(o['vinculo_escola'])
            o['vinculo_turma'] = get_nome_turma(o['vinculo_turma'])
            o['tipo'] = TIPO_USUARIOS_ID[o['tipo']]
            usuario.append(o)
    return usuario


@permissao('diretor')
def lista_de_usuarios_caso_observador_for_diretor(vinculo_escola):
    usuario = []
    aluno = facade.search_aluno_escola_facade(vinculo_escola=vinculo_escola)
    observador = facade.search_observador_escola(vinculo_escola=vinculo_escola)

    for a in aluno:
        a['email'] = ""
        a['vinculo_rede'] = get_nome_rede(a['vinculo_rede'])
        a['vinculo_escola'] = get_nome_escola(a['vinculo_escola'])
        a['vinculo_turma'] = get_nome_turma(a['vinculo_turma'])
        a['tipo'] = TIPO_USUARIOS_ID[a['tipo']]
        usuario.append(a)
    for o in observador:
        if o['tipo'] != '0':
            o['vinculo_rede'] = get_nome_rede(o['vinculo_rede'])
            o['vinculo_escola'] = get_nome_escola(o['vinculo_escola'])
            o['valuno_facadeinculo_turma'] = get_nome_turma(o['vinculo_turma'])
            o['tipo'] = TIPO_USUARIOS_ID[o['tipo']]
            usuario.append(o)
    return usuario


@permissao('professor')
def lista_de_usuarios_caso_observador_for_professor(vinculo_turma):
    usuario = []
    aluno = facade.search_aluno_by_turma_facade(vinculo_turma=vinculo_turma)

    for a in aluno:
        a['email'] = ""
        a['vinculo_rede'] = get_nome_rede(a['vinculo_rede'])
        a['vinculo_escola'] = get_nome_escola(a['vinculo_escola'])
        a['vinculo_turma'] = get_nome_turma(a['vinculo_turma'])
        a['tipo'] = TIPO_USUARIOS_ID[a['tipo']]
        usuario.append(a)

    return usuario


@permissao('professor')
def get_nome_rede(vinculo_rede):
    rede_nome = facade.search_estrutura_id_facade(vinculo_rede)['nome']

    return rede_nome


@permissao('professor')
def get_nome_escola(vinculo_escola):
    escola_nome = facade.search_estrutura_id_facade(vinculo_escola)
    return escola_nome['nome']


@permissao('professor')
def get_nome_turma(vinculo_turma):
    turma_nome = facade.search_estrutura_id_facade(vinculo_turma)['nome']

    return turma_nome



def verificar_nome_login(nome_login):

    existe_usuario = facade.search_aluno_nome_login_facade(nome_login)
    if existe_usuario != None:

        if existe_usuario['nome_login'] == nome_login and existe_usuario['nome_login'].isalpha():
            nome_login = nome_login + '1'
        else:
            x = '2'
            mesmo_login = facade.search_aluno_nome_login_facade(nome_login)
            while mesmo_login != None and nome_login == mesmo_login['nome_login']:
                nome_login = [letter for letter in nome_login]
                y = len(nome_login)
                nome_login[y - 1] = x
                x = str(int(x) + 1)
                nome_login = ''.join(nome_login)
    else:
        return nome_login

    return nome_login


def controller_redirect_cadastro():
    tipo_usuario = request.params['tipo_usuario']
    redirect(PAGINA_DE_CADASTRO_POR_TIPO[tipo_usuario])


def create_aluno():
    let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l']
    nome = request.forms['aluno_nome']
    nome_separado=nome.split()
    nome_login1=nome_separado[0]
    presenha = random.sample(let, 4)
    escola = request.forms['escola']
    data_nascimento=request.params['data_nascimento']
    matricula=request.params['matricula']
    sexo=request.params['sexo']
    vinculo_rede = facade.search_estrutura_id_facade(int(escola))
    nome_login=verificar_nome_login(nome_login1)
    presenha.sort()
    senha = ''.join(presenha)
    facade.create_aluno_facade(nome=nome, tipo_aluno='6',matricula=matricula, vinculo_escola=escola, nome_login=nome_login,
                               vinculo_rede=vinculo_rede['vinculo_rede'], senha=senha, data_nascimento=data_nascimento,sexo=sexo)

    redirect('/gestao_aprendizagem/usuario')


def view_observador_cadastro():
    tipo_observador = request.params['tipo_observador']

    if tipo_observador == TIPO_USUARIOS['administrador']:
        return template('observador/create_observador', tipo=tipo_observador)
    elif tipo_observador == TIPO_USUARIOS['gestor']:
        return template('observador/create_observador', tipo=tipo_observador, rede=filtro_vinculo_cadastro_rede())
    elif tipo_observador == TIPO_USUARIOS['diretor']:
        return template('observador/create_observador', tipo=tipo_observador, escola=filtro_vinculo_cadastro_escola())
    elif tipo_observador == TIPO_USUARIOS['professor']:
        return template('observador/create_observador', observador_logado=usuario_logado()['tipo'],
                        tipo=tipo_observador, escola=filtro_vinculo_cadastro_escola(),
                        turma=filtro_vinculo_cadastro_turma())
    elif tipo_observador == TIPO_USUARIOS['responsavel']:
        return template('observador/create_observador' ,tipo=tipo_observador)
    else:
        redirect('/observador')


def controller_observador_cadastro():
    tipo = request.params['tipo']
    nome = request.params['nome']
    senha1 = request.params['senha']
    telefone = request.params['telefone']
    cpf = request.params['cpf']
    email = request.params['email']
    escola = request.params['escola']
    rede = request.params['rede']
    # logradouro = request.params['logradouro']
    # numero = request.params['numero']
    # complemento = request.params['complemento']
    # bairro = request.params['bairro']
    # cep = request.params['cep']
    # Uf=request.params['uf']
    turma = request.params['turma']
    # data = request.params['data_nascimento']


    senha = sha512_crypt.hash(senha1)

    if tipo != '1':
        vinculo_rede = facade.search_estrutura_id_facade(int(escola))
        facade.create_observador_facade(nome=nome, senha=senha, telefone=telefone, cpf=cpf, email=email, tipo=tipo,
                                        escola=escola, rede=vinculo_rede['vinculo_rede'], vinculo_turma=turma)
    else:
        facade.create_observador_facade(nome=nome, senha=senha, telefone=telefone, cpf=cpf, email=email, tipo=tipo,
                                        escola=escola, rede=rede, vinculo_turma=turma)


def view_observador_update():
    nome = request.params['nome']
    observador = facade.search_observador_facade(nome)
    return template('observador/update_observador', id=observador['id'], nome=observador['nome'],
                    telefone=observador['telefone'], cpf=observador['cpf'], email=observador['email'])


def controller_observador_update():
    facade.update_observador_facade(id=request.params['id'], nome=request.params['nome'],
                                    telefone=request.params['telefone'], cpf=request.params['cpf'],
                                    email=request.params['email'])
    redirect('/observador/read_observador')


def controller_checar_se_email_existe():
    email = request.params['teste_email']
    verificacao = facade.search_observador_email_facade(email=email)
    if verificacao is not None:
        return verificacao['email']
    else:
        return None


def controller_medalha_cadastro():
    nome = request.params['nome']
    tipo = request.params['tipos']
    facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['medalha'],nome=nome, tipo_item=tipo)
    redirect('/gestao_aprendizagem')


def read_de_medalha():
    medalhas = []

    for medalha in facade.read_estrutura_facade(TIPO_ESTRUTURA['medalha']):
        medalhas.append(medalha)

    return dict(medalhas=medalhas)


def view_index_rede():
    """
    pagina inicial de rede , que mostra , tambem , as redes disponiveis no banco
    metodos usados: controller_read_rede :interno:
    :return: Dicionario de redes
    """
    return dict(redes=facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['rede']))


def controller_create_rede():
    """
    Cria rede com os parametros de nome da rede e o telefone da mesma
    metodos usados:create rede facade
    :return:
    """
    nome = request.params['nome_rede']
    telefone = request.params['telefone']
    facade.create_estrutura_facade(nome=nome, telefone=telefone, tipo_estrutura="1")
    redirect('/rede')


def view_escola_index():
    """
    view inicial de escola, mostrando as escolas cadastradas no sistema
    usa o metodo: controller_escola_read :interno:
    :return:dicionario com os valores da escola a serem mostrados
    """
    escola = []
    for e in facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['escola']):
        e['vinculo_rede'] = get_nome_rede(e['vinculo_rede'])
        escola.append(e)
    return dict(escola=escola)



def cadastro_escola():
    return dict(rede=filtro_vinculo_cadastro_rede())


def controller_escola_cadastro():
    facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['escola'], nome=request.params['nome'],
                                   telefone=request.params['telefone'], cnpj=request.params['cnpj'],
                                   cep=request.params['cep'],
                                   estado=request.params['estado'], uf=request.params['uf'],
                                   logradouro=request.params['logradouro'],
                                   numero=request.params['numero'], vinculo_rede=request.params['rede'],
                                   bairro=request.params['bairro'], complemento=request.params['complemento']
                                   , municipio=request.params['municipio'])
    redirect("/escola")


def view_turma():
    """
    Pagina inicial de turmas e q mostra as turmas ja cadastradas
    metodos utilizados : controller_read_ turma :interno dessa pagina:
    :return: dicionario com os parametros da turma a serem mostrados
    """
    turma = []
    for t in facade.read_estrutura_facade(TIPO_ESTRUTURA['turma']):
        t['serie'] = SERIE[t['serie']]
        t['vinculo_escola'] = get_nome_escola(t['vinculo_escola'])
        turma.append(t)
    return dict(turma=turma)


def view_cadastrar_turma():
    """
    Pagina de cadastro de turma , mostra as escolas ja cadastradas no banco de dados
    metodos usados: read_escola_facade
    :return:o dicionario com as escolas
    """
    return dict(escolas=filtro_vinculo_cadastro_escola())


def controller_create_turma():
    """
    """
    turma = request.forms['turma_nome']
    serie = request.forms['serie']
    escola = request.forms['escola']
    vinculo_rede = facade.search_estrutura_id_facade(request.forms['escola'])

    facade.create_estrutura_facade(nome=turma, tipo_estrutura='3', quem_criou=usuario_logado()['nome'], serie=serie,
                                   vinculo_escola=escola, vinculo_rede=vinculo_rede['vinculo_rede'])
    redirect('/turma')


def view_update_turma():
    """
    Pagina de cadastro de turma , mostra as escolas ja cadastradas no banco de dados
    metodos usados: read_escola_facade
    :return:o dicionario com as escolas
    """
    id = request.forms['id_turma']
    turma = facade.search_estrutura_id_facade(int(id))
    return template('turma/turma_update', turma=turma, aluno=alunos_na_escola_sem_turma(turma['vinculo_escola']),
                    professor=professor_na_escola_sem_turma(
                        turma['vinculo_escola']))


def controller_update_turma():
    teste = request.forms

    turma = request.forms['turma']
    alunos = [aluno.split('_')[1] for aluno in teste if 'aluno' in aluno]
    professores = [professor.split('_')[1] for professor in teste if 'professor' in professor]

    if alunos is not '' or alunos is not []:
        for a in alunos:
            facade.aluno_in_turma_facade(id_aluno=a, vinculo_turma=turma)

    if professores is not '' or professores is not []:
        for p in professores:
            facade.observador_in_turma_facade(id_observador=p, vinculo_turma=turma)

    redirect('/turma')


def descritores():
    return


def relatorio_aluno_view():
    todos_alunos_da_mesma_turma = trazer_todos_alunos_da_mesma_turma()
    observador = usuario_logado()

    return dict(alunos=todos_alunos_da_mesma_turma, tipo=observador['tipo'])

def relatorio_aluno():
    observador = usuario_logado()
    aluno = facade.search_aluno_id_facade(id_aluno=request.params['aluno'])
    aluno['vinculo_turma'] = get_nome_turma(vinculo_turma=aluno['vinculo_turma'])
    descritores = facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['objeto_de_aprendizagem'])
    oa = []
    vezes_jogada = []
    porcentagem_aluno = []

    for i in descritores:
        if 'VC' not in i['sigla_oa'] and 'CN' not in i['sigla_oa']:
            desempenho = facade.search_oa_facade(id_aluno=str(aluno['id']), objeto_aprendizagem=i['sigla_oa'])
            oa.append(i)
            if desempenho != None:
                porcentagem_aluno.append(cor_desempenho(desempenho=desempenho))
            else:
                porcentagem_aluno.append(None)

    return template('gestao_aprendizagem/relatorios/aluno/relatorio_aluno_detalhe', oa=oa,
                    porcentagem=porcentagem_aluno, aluno=aluno, tipo=observador['tipo'])


def relatorio_oa_aluno():
    id_aluno = request.params['aluno']
    oa = request.params['oa']

    aluno = facade.search_aluno_id_facade(id_aluno=id_aluno)
    desempenho = facade.search_oa_facade(id_aluno=str(id_aluno), objeto_aprendizagem=oa)
    pontuacao = checar_pontuiacao(desempenho=desempenho)
    vezes_jogada = len(desempenho['jogo_jogado'])
    porcentagem_aluno = porcentagem_pontuacao(pontuacao, vezes_jogada)

    return template('gestao_aprendizagem/relatorios/aluno/relatorio_oa_aluno', aluno=aluno,
                    vezes_jogas=vezes_jogada, porcentagem_do_aluno=porcentagem_aluno)


def levar_oas_matematica():
    aluno = facade.search_aluno_id_facade(id_aluno=request.params['aluno'])
    descritores = facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['objeto_de_aprendizagem'])
    oa = []
    porcentagem_aluno = []
    diciplina = request.params['diciplina']

    if diciplina != '0':
        for i in descritores:
            if i['disciplina'] == diciplina and 'VC' not in i['sigla_oa'] and 'CN' not in i['sigla_oa']:
                desempenho = facade.search_oa_facade(id_aluno=str(aluno['id']), objeto_aprendizagem=i['sigla_oa'])
                oa.append(i)
                if desempenho != None:
                    porcentagem_aluno.append(cor_desempenho(desempenho=desempenho))
                else:
                    porcentagem_aluno.append(None)
    else:
        for i in descritores:
            if 'VC' not in i['sigla_oa'] and 'CN' not in i['sigla_oa']:
                desempenho = facade.search_oa_facade(id_aluno=str(aluno['id']), objeto_aprendizagem=i['sigla_oa'])
                oa.append(i)
                if desempenho != None:
                    porcentagem_aluno.append(cor_desempenho(desempenho=desempenho))
                else:
                    porcentagem_aluno.append(None)

    return template('gestao_aprendizagem/relatorios/aluno/teste_table.tpl', oa=oa, aluno=aluno,
                    porcentagem=porcentagem_aluno)


def filtro_vinculo_cadastro_rede():
    observador_logado = usuario_logado()
    if observador_logado['tipo'] == TIPO_USUARIOS['administrador']:
        return facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['rede'])
    elif observador_logado['tipo'] == TIPO_USUARIOS['gestor']:
        return facade.search_estrutura_id_facade(observador_logado['vinculo_rede'])


def filtro_vinculo_cadastro_escola():
    observador_logado = usuario_logado()
    if observador_logado['tipo'] == TIPO_USUARIOS['administrador']:
        return facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['escola'])
    elif observador_logado['tipo'] == TIPO_USUARIOS['gestor']:
        return facade.search_estrutura_escola_by_rede_facade(observador_logado['vinculo_rede'])
    elif observador_logado['tipo'] == TIPO_USUARIOS['diretor'] or observador_logado['tipo'] == TIPO_USUARIOS[
        'professor']:
        return facade.search_estrutura_id_facade(observador_logado['vinculo_escola'])


def filtro_vinculo_cadastro_turma():
    observador_logado = usuario_logado()
    if observador_logado['tipo'] == TIPO_USUARIOS['administrador']:
        return facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['turma'])
    elif observador_logado['tipo'] == TIPO_USUARIOS['gestor']:
        return facade.search_estrutura_turma_by_rede_facade(observador_logado['vinculo_rede'])
    elif observador_logado['tipo'] == TIPO_USUARIOS['diretor']:
        return facade.search_estrutura_turma_by_escola_facade(observador_logado['vinculo_escola'])



def alunos_na_escola_sem_turma(vinculo_escola):
    alunos = []
    for a in facade.search_aluno_escola_facade(vinculo_escola):
        if a['vinculo_turma'] == '0':
            alunos.append(a)

    return alunos

def professor_na_escola_sem_turma(vinculo_escola):
    professores = []
    for p in facade.search_observador_escola(vinculo_escola=vinculo_escola):
        if p['vinculo_turma'] == '0' and p['tipo'] == TIPO_USUARIOS['professor']:
            professores.append(p)

    return professores


def trazer_todos_alunos_da_mesma_turma():
    usuario = usuario_logado()
    tipo_usuarios = {
        '0': facade.read_aluno_facade(),
        '1': facade.search_aluno_by_rede_facade(vinculo_rede=usuario['vinculo_rede']),
        '2': facade.search_aluno_escola_facade(vinculo_escola=usuario['vinculo_escola']),
        '3': facade.search_aluno_by_turma_facade(vinculo_turma=usuario['vinculo_turma'])
    }

    alunos = tipo_usuarios[usuario['tipo']]

    for i in alunos:
        i['vinculo_turma'] = get_nome_turma(i['vinculo_turma'])

    return alunos



def checar_pontuiacao(desempenho):

    niveis_pontuação={
        'dificil': 2,
        'medio': 1,
        'facil': 0
    }
    pontuacao = 0
    for i in desempenho['jogo_jogado']:
        dict_dado_jogo = convertendo_str_in_dict(i)
        if dict_dado_jogo['termino'] == True:
            pontuacao += niveis_pontuação[dict_dado_jogo['nivel']]

    return pontuacao

def media_pontuacao(pontuacao, vezes_jogada):
    media = pontuacao/vezes_jogada

    return media

def porcentagem_pontuacao(pontuacao,vezes_jogada):
    maximo_pontos = vezes_jogada * 2
    porcentagem = (pontuacao * 100)//maximo_pontos

    return str(porcentagem)



def cor_desempenho(desempenho):
    pontuacao = checar_pontuiacao(desempenho=desempenho)
    vezes_jogada = len(desempenho['jogo_jogado'])
    porcentagem_aluno = porcentagem_pontuacao(pontuacao, vezes_jogada)

    return int(porcentagem_aluno)


def convertendo_str_in_dict(str):
    from ast import literal_eval

    python_dict = literal_eval(str)

    return python_dict
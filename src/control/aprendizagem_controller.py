import json
from bottle import route, view, request, redirect, response, get, template
from facade.facade_main import Facade
from control.classes.permissao import permissao, usuario_logado
from control.dicionarios import *

facade = Facade()


def qual_tipo_usuario_logado():
    from control.dicionarios import TIPO_USUARIOS

    usuario = usuario_logado()
    if int(usuario['tipo']) >= int(TIPO_USUARIOS['aluno']):
        usuario = facade.search_aluno_nome_facade(usuario['nome'])
        avatar = facade.avatar_facade(usuario['id'])
    else:
        usuario = facade.search_observador_facade(usuario['nome'])

    return usuario, avatar

def pecas_avatar(avatar):

    avatar_pecas = {
        'cor': facade.search_estrutura_id_facade(avatar['cor'])['nome'],
        'rosto': facade.search_estrutura_id_facade(avatar['rosto'])['nome'],
        'acessorio': facade.search_estrutura_id_facade(avatar['acessorio'])['nome'],
        'corpo': facade.search_estrutura_id_facade(avatar['corpo'])['nome']
    }

    return avatar_pecas



def itens_cadastrados_sistema():
    itens = facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'])
    return itens


def itens_usuario_tem():
    itens = facade.ver_item_comprado_facade(id_usuario=usuario_logado()['id'])
    return itens


def obterUltimaConclusao():
    usuario = usuario_logado()
    # ultimo_oa_jogado=facade.ultimo_oa_jogado_facade(usuario_logado()['id'])

    retorno = {
        'objetoAprendizagem': '',
        'unidade': '',
        'aventura': '',
        'universo': 'UV1'
    }
    return retorno


def verificarAcessoObjetoAprendizagem():
    usuario = usuario_logado()
    parametros = parametros_json_jogos(request.params.items())
    if int(usuario['tipo']) < 6:
        retorno = {'objetosAprendizagemAcessiveis': parametros['objetosAprendizagem']}
    else:
        cn_final = facade.oa_teste_facade(id_aluno=str(usuario['id']), oa='{}CN02'.format(parametros['objetosAprendizagem'][0:9]))
        if cn_final != []:
            retorno = {'objetosAprendizagemAcessiveis': parametros['objetosAprendizagem']}
        else:
            teste = []
            for i in parametros['objetosAprendizagem']:
                desempenho_oa = facade.oa_teste_facade(id_aluno=str(usuario['id']), oa=i)
                if desempenho_oa == []:

                    teste.append(i)
                    break
                else:
                    teste.append(i)
            retorno = {'objetosAprendizagemAcessiveis': teste}
    return retorno


def verificarConclusoesObjetosAprendizagem():
    usuario = usuario_logado()
    parametros = parametros_json_jogos(request.params.items())
    if int(usuario['tipo']) < 6:
        retorno = {'objetosConcluidos': parametros['objetosAprendizagem']}
    else:
        cn_final = facade.oa_teste_facade(id_aluno=str(usuario['id']),
                                          oa='{}CN02'.format(parametros['objetosAprendizagem'][0:9]))
        if cn_final != []:
            retorno = {'objetosConcluidos': parametros['objetosAprendizagem']}
        else:
            teste = []
            for i in parametros['objetosAprendizagem']:
                desempenho_oa = facade.oa_teste_facade(id_aluno=str(usuario['id']), oa=i)
                if desempenho_oa == []:
                    pass
                else:
                    teste.append(i)

            retorno = {'objetosConcluidos': teste}

    return retorno


def registrarConclusao():
    premios={
        'OA': is_oa,
        'VC': is_vc_or_cn,
        'CN': is_vc_or_cn
    }

    return premios[parametros_json_jogos(request.params.items())['objetoAprendizagem'][9:11]]\
        (aluno=usuario_logado()['id'],parametros=parametros_json_jogos(request.params.items()),
         oa=parametros_json_jogos(request.params.items())['objetoAprendizagem'])


def obterPremiacao():
    parametros = parametros_json_jogos(request.params.items())
    aluno1 = usuario_logado()
    aluno = facade.search_aluno_nome_facade(nome=aluno1['nome'])
    retorno = {
        'moedas': int(aluno['pontos_de_moedas']),
        'xp': int(aluno['pontos_de_vida'])
    }

    return retorno

def verificarAcessoUnidade():
    usuario = usuario_logado()
    parametros = parametros_json_jogos(request.params.items())
    if int(usuario['tipo']) < 6:
        retorno = {'unidadesAcessiveis': parametros['unidades']}
    else:
        desempenho_aluno = facade.search_desempenho_concluido_id_aluno_facade(id_aluno=str(usuario['id']))
        if desempenho_aluno == []:
            retorno = {'unidadesAcessiveis': [parametros['unidades'][0]]}
        else:
            acesso_unidade = []
            for i in parametros['unidades']:
                desempenho_unidade = facade.unidade_teste_facade(id_aluno=str(usuario['id']), unidade=i)
                if desempenho_unidade == []:
                    acesso_unidade.append(i)
                    break
                else:
                    desempenho_oa = facade.oa_teste_facade(id_aluno=str(usuario['id']), oa='{}OA06'.format(i))
                    if desempenho_oa == []:
                        acesso_unidade.append(i)

                        break
                    else:
                        acesso_unidade.append(i)
            retorno = {'unidadesAcessiveis': acesso_unidade}
    return retorno

def verificarAcessoUnidade():
    usuario = usuario_logado()
    parametros = parametros_json_jogos(request.params.items())
    if int(usuario['tipo']) < 6:
        retorno = {'unidadesAcessiveis': parametros['unidades']}
    else:
        desempenho_aluno = facade.search_desempenho_concluido_id_aluno_facade(id_aluno=str(usuario['id']))
        if desempenho_aluno == []:
            retorno = {'unidadesAcessiveis': [parametros['unidades'][0]]}
        else:
            acesso_unidade = []
            for i in parametros['unidades']:
                desempenho_unidade = facade.unidade_teste_facade(id_aluno=str(usuario['id']), unidade=i)
                if desempenho_unidade == []:
                    acesso_unidade.append(i)
                    break
                else:
                    desempenho_oa = facade.oa_teste_facade(id_aluno=str(usuario['id']), oa='{}OA06'.format(i))
                    if desempenho_oa == []:
                        acesso_unidade.append(i)

                        break
                    else:
                        acesso_unidade.append(i)
            retorno = {'unidadesAcessiveis': acesso_unidade}
    return retorno

def verificarAcessoAventura():
    usuario = usuario_logado()

    for i in facade.search_desempenho_concluido_id_aluno_facade(id_aluno=str(usuario['id'])):

    if int(usuario['tipo']) < 6:
        parametros = parametros_json_jogos(request.params.items())
        return {'aventurasAcessiveis': parametros['aventuras']}
    else:
        from control.dicionarios import AVENTURAS_CONECTURMA
        serie_turma = facade.search_estrutura_id_facade(int(usuario['vinculo_turma']))
        return AVENTURAS_CONECTURMA[serie_turma['serie']]

def is_oa(aluno, parametros, oa):
    from control.classes.permissao import update_cookie
    gamificacao = gamificacao_moeda_xp(parametros)

    premios = {
        'medalhas': gamificacao_medalha(aluno, oa=oa),
        'moedas': gamificacao['moedas'],
        'xp': gamificacao['xp']
    }

    create_or_update_oa(id_aluno=aluno, unidade=oa[0:9], objeto_aprendizagem=oa,
                        parametros=parametros['niveis'])

    facade.gravar_premiacao(aluno, premios)
    update_cookie(premios)

    return premios

def is_vc_or_cn(aluno, parametros, oa):
    create_or_update_oa(id_aluno=aluno, unidade=oa[0:9], objeto_aprendizagem=oa,
                        parametros=parametros['niveis'])

    premios = {
        'medalhas': [],
        'moedas': [],
        'xp': []
    }

    return premios

def gamificacao_moeda_xp(parametros):
    from control.dicionarios import PREMIO_JOGOS

    ponto = pegar_maior_pontuacao(parametros['niveis'])
    if ponto:
        return PREMIO_JOGOS[ponto['nivel']]
    else:
        return PREMIO_JOGOS['0']


def gamificacao_medalha(usuario_id, oa):

    medalhas = []
    oa_concluidos = facade.search_desempenho_concluido_id_aluno_facade(id_aluno=str(usuario_id))
    medalhas.append(primeiro_jogo(facade.oa_teste_facade(id_aluno=str(usuario_id),oa='UV1AV1UD1OA01')))
    if len(oa_concluidos) >= 10:
        medalhas.append(dose_dupla(oa_concluidos))
    medalhas.append(dezena(usuario_id=str(usuario_id), oa=oa))
    medalhas.append(fera_da_Matemática(oa=oa))
    medalhas.append(fera_da_lingua_portuguesa(oa=oa))
    medalhas.append(musical(id_aluno=str(usuario_id),oa=oa))
    if 'OA' in oa:
        medalhas.append(de_novo(id_aluno=str(usuario_id), oa=oa))

    medalhas.append(magia_da_matematica(id_aluno=str(usuario_id), aventura=oa[0:6]))
    medalhas.append(magia_da_lingua_portuguesa(id_aluno=str(usuario_id), aventura=oa[0:6]))
    return testa_medalha_false(medalhas)

def testa_medalha_false(medalhas):
    retorno = []
    for i in medalhas:
        if i != False and i != None:
            retorno.append(i)

    return retorno

def testar_se_ja_medalha(id_usuario, medalha):
    pass

def primeiro_jogo(oa_concluido):

    if oa_concluido == []:
        return '11'
    else:
        return False


def dose_dupla(oa_concluido):

    medalha = 0

    for i in oa_concluido:
        if len(i['jogo_jogado']) > 1:
            medalha += 1
    if medalha == 10:
        return '12'
    else:
        return False


def dezena(usuario_id, oa):
    oas = facade.oa_teste_facade(id_aluno=usuario_id, oa=oa)
    if oas != None:
        for oa in oas :
            teste = len(oa['jogo_jogado'])
            if teste == 10:
                return '13'
            else:
                return False
    else:
        return False


def fera_da_Matemática(oa):
    if oa == 'UV1AV1UD1OA05' or oa == 'UV1AV2UD1OA05' or oa == 'UV1AV3UD1OA05':
        return '14'
    else:
        return False


def fera_da_lingua_portuguesa(oa):
    if oa == 'UV1AV1UD1OA06' or oa == 'UV1AV2UD1OA06' or oa == 'UV1AV3UD1OA06':
        return '15'
    else:
        return False


def musical(id_aluno,oa):
    aluno=facade.oa_teste_facade(id_aluno=id_aluno,oa='{}VC01'.format(oa[0:9]))
    if aluno != []:
        return '16'
    else:
        return False


def de_novo(id_aluno,oa):
    aluno = facade.oa_teste_facade(id_aluno=id_aluno,oa='{}VC01'.format(oa[0:9]))
    for i in aluno:

        if len(i['jogo_jogado']) >= 3:
            return '17'
        else:
            return False

def magia_da_matematica(id_aluno, aventura):
    oa = facade.search_oa_by_type_and_aventura_facade(aventura='UV1AV1', disciplina=DICIPLINA_NOME['matematica'])
    oas_terminandos_dificel = 0
    for i in oa:
        oa_terminados = facade.oa_teste_facade(id_aluno=id_aluno, oa =i)
        for z in oa_terminados:
            dificuldade = z['jogo_jogado'][len(z['jogo_jogado'])-1]
            if dificuldade['nivel'] == 'dificil':
                oas_terminandos_dificel += 1
            else:
                oas_terminandos_dificel = 0

    if oas_terminandos_dificel == 5:
        return '19'
    else:
        return False

def magia_da_lingua_portuguesa(id_aluno, aventura):
    oa = facade.search_oa_by_type_and_aventura_facade(aventura='UV1AV1', disciplina=DICIPLINA_NOME['lingua Portuguesa'])
    oas_terminandos_dificel = 0
    for i in oa:
        oa_terminados = facade.oa_teste_facade(id_aluno=id_aluno, oa=i)
        for z in oa_terminados:
            dificuldade = z['jogo_jogado'][len(z['jogo_jogado']) - 1]
            if dificuldade['nivel'] == 'dificil':
                oas_terminandos_dificel += 1
            else:
                oas_terminandos_dificel = 0

    if oas_terminandos_dificel >= 5:
        return '20'
    else:
        return False



def create_or_update_oa(id_aluno, unidade, objeto_aprendizagem, parametros):
    oa_existe = facade.objeto_concluido_facade(id_aluno=str(id_aluno), objeto_aprendizagem=objeto_aprendizagem)
    if oa_existe == None:

        facade.create_oa_concluido_facade(id_aluno=str(id_aluno), unidade=unidade,
                                          objeto_aprendizagem=objeto_aprendizagem)

        create_or_update_oa(id_aluno=str(id_aluno), unidade=unidade, objeto_aprendizagem=objeto_aprendizagem,
                            parametros=parametros)
    else:
        ponto = pegar_maior_pontuacao(parametros)
        if ponto != False:
            facade.armazenar_dados_jogos_facade(oa_existe['id'], ponto)
        else:
            facade.armazenar_dados_jogos_facade(oa_existe['id'], parametros)


def pegar_maior_pontuacao(parametros):
    teste = False
    for i in parametros:
        if i['termino'] == True:
            teste = i

    return teste


def parametros_json_jogos(parametro):
    for p in parametro:
        parametros = list(p)[0]
    parametros = json.loads(parametros)

    return parametros



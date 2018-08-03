# coding: utf-8
import unittest


from src.facade.facade_main import Facade
from control.dicionarios import TIPO_ESTRUTURA

facade = Facade()


class FacadeTest(unittest.TestCase):
    def setUp(self):
        self.facade = Facade()

    """TESTE ALUNO"""

    def _create_aluno(self):

        aluno1 = self.facade.create_aluno_facade(nome="egg", vinculo_escola="Escola Conecturma", matricula="123",
                                                 vinculo_rede="0")
        self.assertEqual(aluno1, True)
        aluno2 = self.facade.create_aluno_facade(nome="dickens silverio", matricula="matri", nome_login="dickens",
                                                 senha="abcd", email="henrique_boladao@bol.com", tipo_aluno="6",
                                                 cpf_responsavel="123594847-42", vinculo_rede="Rede Conecturma",
                                                 vinculo_escola="Escola Conecturma", vinculo_serie="1o ano")
        self.assertEqual(aluno2,True)

    def test_create_aluno(self):
        self._create_aluno()

    def _read_aluno(self):
        self.facade.apagartudo()
        self._create_aluno()
        aluno4 = self.facade.search_aluno_nome_facade("egg")
        self.assertIn(aluno4['id'], self.facade.read_aluno_facade()[-1].values())

    def test_read_aluno(self):
        self._read_aluno()

    def _update_aluno(self):
        self._create_aluno()
        aluno1 = self.facade.search_aluno_nome_facade("dickens silverio")
        x = aluno1['id']
        self.facade.update_aluno_facade(aluno1['id'], "knight", senha="321",turma="do bairro",escola="conectreutrma",rede="de pesca")
        aluno2 = self.facade.search_aluno_nome_facade("knight")
        y = aluno2['id']
        self.assertEqual(x, y)

    def test_update_aluno(self):
        self._update_aluno()

    def _search_aluno_id_facade(self):
        self.facade.apagartudo()
        self._create_aluno()
        aluno=self.facade.search_aluno_id_facade('1')
        self.assertEqual(aluno['nome'],'egg')
        self.assertEqual(aluno['vinculo_escola'],'Escola Conecturma')

    def test_pesquisa_aluno_id(self):
        self._search_aluno_id_facade()

    def _search_aluno_escola_facade(self):
        self._create_aluno()
        aluno=self.facade.search_aluno_escola_facade('Escola Conecturma')
        self.assertEqual(aluno[0]['nome'],'dickens silverio')

    def test_search_aluno_escola(self):
        self._search_aluno_escola_facade()


    def _pesquisa_aluno(self):
        aluno = self.facade.search_aluno_nome_facade("egg")
        print('eg',aluno)
        self.assertEqual(aluno['matricula'], '123')
        aluno1 = self.facade.search_aluno_nome_facade("dickens silverio")
        self.assertEqual(aluno1['email'],'henrique_boladao@bol.com')

    def test_pesquisa_aluno(self):
        self._pesquisa_aluno()
    def _anotacoes_no_aluno(self):
        self._create_aluno()
        mensagem2 = "tetativa..."
        mensagem = "Isto é uma mensagem de teste"
        aluno1 = self.facade.search_aluno_nome_objeto_facade("egg")
        self.facade.anotacoes_aluno_facade(aluno1.id, mensagem)
        self.facade.anotacoes_aluno_facade(aluno1.id, mensagem2)
        self.assertEqual(aluno1.anotacoes_aluno[0], mensagem.encode('utf-8'))
        self.assertEqual(aluno1.anotacoes_aluno[1], mensagem2.encode('utf-8'))

    def _read_anotacoes_no_aluno(self):
        self._anotacoes_no_aluno()
        aluno1 = self.facade.search_aluno_nome_facade("egg")
        read = self.facade.read_anotacoes_aluno_facade(aluno1.id)
        self.assertIn("Isto é uma mensagem de teste", read)

    def _aluno_in_turma(self):
        self._create_turma()
        aluno1 = self.facade.create_aluno_facade(matricula="0", nome="egg", escola="Escola Conecturma", senha="123",
                                                 vinculo_rede='0')
        alunoer1 = self.facade.search_aluno_nome_facade("egg")
        self.facade.create_aluno_facade(nome="Ni", senha="123", escola="Escola Conecturma", rede="0")
        aluno2 = self.facade.search_aluno_nome_facade("Ni")
        escolhidos = [alunoer1['id'], aluno2['id']]
        turma1 = self.facade.search_estrutura_facade("3", "Knight")
        self.facade.aluno_in_turma_facade(escolhidos, turma1['id'])
        aluntest2 = self.facade.search_aluno_nome_facade('Ni')
        aluntest = self.facade.search_aluno_nome_facade('egg')
        self.assertEqual(aluntest['vinculo_turma'], str(turma1['id']))
        self.assertEqual(aluntest2['vinculo_turma'], str(turma1['id']))

    def _comprar_item(self):
        self._create_item()
        self._create_aluno()
        aluno1 = self.facade.search_aluno_nome_objeto_facade("egg")
        item1 = self.facade.search_estrutura_facade(nome="burroquandofoge", tipo_estrutura="4")

        self.facade.compra_item_facade(aluno1.id, item1['id'])
        self.assertIn(str(item1['id']), aluno1.itens_comprados[-1].decode('utf-8'))

    def _ver_iten_comprado(self):
        self._comprar_item()
        aluno1 = self.facade.search_aluno_nome_objeto_facade("egg")
        iten = self.facade.ver_item_comprado_facade(aluno1.id)
        self.assertEqual([(aluno1.itens_comprados[0].decode('utf-8'))], iten)

    def _equipar_item_facade(self):
        self._comprar_item()
        aluno1 = self.facade.search_aluno_nome_facade("egg")
        iten = self.facade.search_estrutura_facade(tipo_estrutura='5', nome="burroquandofoge")
        self.facade.equipar_item_facade(aluno1['id'], iten)
        aluno2 = self.facade.search_aluno_nome_facade("egg")
        self.assertEqual(aluno2['cor'], str(iten['id']))

    def _mostrar_avatar(self):
        self._equipar_item_facade()
        aluno1 = self.facade.search_aluno_nome_facade("egg")
        self.facade.avatar_facade(aluno1.id)
        iten1 = self.facade.search_estrutura_facade("burroquandofoge")
        self.assertEqual(self.facade.avatar_facade(aluno1.id)['cor'], str(iten1['id']))
        self._delete_item()
        self._delete_alunos()



    def test_anotacoes_no_aluno(self):
        self._create_aluno()
        self._anotacoes_no_aluno()

    def _test_read_anotacoes_aluno(self):
        self._read_anotacoes_no_aluno()

    def test_aluno_in_turma(self):
        self._aluno_in_turma()
        self._delete_turma()

    def test_compra_item(self):
        self._comprar_item()

    def test_ver_itens_comprados(self):
        self._ver_iten_comprado()

    def test_equipar_item(self):
        self._equipar_item_facade()

    def _test_ver_avatar(self):
        self._mostrar_avatar()

    def _test_create_update_aluno(self):
        self._update_aluno()

    def _test_pesquisa_aluno(self):
        self._pesquisa_aluno()

    def _test_pontos_jogo(self):
        self._pontos_jogo()

    def _test_delete_alunos(self):

        self._delete_alunos()

    def _test_all_aluno(self):
        self._create_aluno_fail()
        self._update_aluno()
        self._pesquisa_aluno()
        self._pontos_jogo()
        self._delete_alunos()

    """FIM TESTE USUARIO/ALUNO"""

    """INICIO TESTE OBSERVADOR"""

    def _create_observador(self):
        observador1 = self.facade.create_observador_facade(nome='Egg', senha='span', telefone='(21)9999-9999',
                                                           cpf='123456789', email='egg@span.com.br', rede=0, escola=0,
                                                           tipo='ADMINISTRADOR')

        observador_professor = self.facade.create_observador_facade(nome='Monty', senha='python',
                                                                    telefone='(21)9999-9999',
                                                                    cpf='123456789', email='Monty@python.com.br',
                                                                    tipo='3', rede="0", escola="1", vinculo_turma="1")
        observador_diretor = self.facade.create_observador_facade(nome="diretor", senha="123", telefone="21 2569 6969",
                                                                  email="tent@cool.os", tipo="2", rede=0, escola=0)

        self.assertIs(observador1, True)
        self.assertIs(observador_professor, True)

    def _update_observador(self):
        observador1 = self.facade.search_observador_facade('Monty')
        observador_update = self.facade.update_observador_facade(id=observador1['id'], nome='Knight',
                                                                 telefone='(11)8888-8888', cpf='999999999',
                                                                 email='knight@ni.com', vinculo_turma="2",
                                                                 vinculo_escola="2")
        observador2 = self.facade.search_observador_tipo_nome_facade('3', 'Knight')
        self.assertEqual(observador2['nome'], 'Knight')
        self.assertEqual(observador2['telefone'], '(11)8888-8888')
        self.assertEqual(observador2['cpf'], '999999999')
        self.assertEqual(observador2['email'], 'knight@ni.com')
        self.assertEqual(observador2['vinculo_turma'], "2")
        self.assertEqual(observador2['vinculo_escola'], "2")

    def _search_observador(self):
        observador1 = self.facade.search_observador_facade('Egg')
        self.assertEqual(observador1['nome'], 'Egg')
        self.assertEqual(observador1['senha'], 'span')
        self.assertEqual(observador1['telefone'], '(21)9999-9999')
        self.assertEqual(observador1['cpf'], '123456789')
        self.assertEqual(observador1['email'], 'egg@span.com.br')
        self.assertEqual(observador1['tipo'], 'ADMINISTRADOR')
        observador2 = self.facade.search_observador_facade('Ni')
        self.assertIs(observador2, None)

    def _delete_observador(self):
        observador1 = self.facade.read_observador_facade()
        escolhidos = []
        for observados in observador1:
            escolhidos.append(observados['id'])
        self.facade.delete_observador_facade(escolhidos)

    def _anotacoes_estrutura(self):
        self._create_escola()
        self._pesquisa_escola()
        mensagem2 = "Gosto dessa escola"
        mensagem = "Nossa escola deve melhorar"
        observador1 = self.facade.search_observador_inativos_facade("egg")
        gestor = self.facade.search_observador_inativos_facade("")
        self.facade.anotacoes_estrutura_baixo_facade(observador1.id, mensagem)
        self.facade.anotacoes_estrutura_cima_facade(gestor.id, mensagem2)
        self.assertEqual(observador1.anotacoes_estrutura_baixo[0], mensagem.encode('utf-8'))
        # self.assertEqual(gestor.anotacoes_estrutura_cima[0],mensagem2.encode('utf-8'))

    def test_create_delete_observador(self):
        self._create_observador()
        self._delete_observador()

    def test_create_search_delete_observador(self):
        self._create_observador()
        self._search_observador()
        self._delete_observador()

    def test_create_update_delete_observador(self):
        self._create_observador()
        self._update_observador()
        self._delete_observador()

    def _test_anotacoes(self):
        self._anotacoes_estrutura()

    """FIM TESTE OBSERVADOR"""

    """TESTE REDE"""

    def _create_rede(self):
        rede = self.facade.create_estrutura_facade(tipo_estrutura='1', nome="egg", telefone="(21)9999-9999")
        rede2 = self.facade.search_estrutura_facade("1", "egg")
        self.assertIsNot(rede, None)
        self.assertIsNot(rede2, None)

    def _update_rede(self):
        rede = self.facade.create_estrutura_facade(nome="egg", telefone="(21)9999-9999")
        self.assertIsNot(rede, None)
        rede1 = self.facade.search_estrutura_facade(tipo_estrutura="1", nome="egg")
        self.assertIsNot(rede1, None)

        rede_up = self.facade.update_estrutura_facade(rede.id, nome="Ni", telefone="(11)8888-8888")
        rede = self.facade.search_estrutura_facade(tipo_estrutura="1", nome="Ni")
        self.assertEqual(rede['nome'], "Ni")
        self.assertEqual(rede['telefone'], "(11)8888-8888")

    def _pesquisa_rede(self):
        rede = self.facade.search_estrutura_facade(tipo_estrutura="1", nome="Ni")
        self.assertIs(rede, rede)
        rede1 = self.facade.search_estrutura_facade(tipo_estrutura="1", nome="Sily walk")
        self.assertIs(rede1, None)

    def _delete_rede(self):
        rede = self.facade.read_estrutura_facade(tipo_estrutura="1")
        escolhidos = []
        for redes in rede:
            escolhidos.append(redes['id'])
        self.facade.delete_rede_facade(escolhidos)

    def test_create_rede(self):
        self._create_rede()

    def test_update_rede(self):
        self._update_rede()

    def _test_pesquisa_rede(self):
        self._pesquisa_rede()

    def _test_delete_rede(self):
        self._update_rede()
        self._delete_rede()

    """FIM TESTE REDE"""

    """TESTE FACADE ESCOLA"""

    def _create_escola(self):
        escola = self.facade.create_estrutura_facade(nome='Do bairro', bairro='de baixo', telefone='2266 6622',
                                                     numero='21 ', UF='RJ', cidade='Pindamonhagaba',
                                                     cep='22287111')
        self.assertIsNot(escola, None)

    def _update_escola(self):
        escola = self.facade.search_escola_facade("Do bairro")
        self.facade.update_escola_facade(escola['id'], nome="Ni", telefone="33355567", vinculo_rede="abelhinha",
                                         cep="22270 999", endereco="rua do teste ", numero='666',
                                         cidade="RIO DE JANEIRO",
                                         estado='RJ')
        escola2 = self.facade.search_escola_facade("Ni")
        self.assertEqual(escola2['nome'], "Ni")
        self.assertEqual(escola2['endereco'], "rua do teste ")
        self.assertEqual(escola2['numero'], '666')
        self.assertEqual(escola2['vinculo_rede'], "abelhinha")
        self.assertEqual(escola2['telefone'], "33355567")

    def _pesquisa_escola(self):
        escola = self.facade.search_estrutura_facade(tipo_estrutura="2", nome="Do bairro")
        self.assertIs(escola, escola)
        escola1 = self.facade.search_estrutura_facade(tipo_estrutura="2", nome="Sily walk")
        self.assertIs(escola1, {})

    def _delete_escola(self):
        escola = self.facade.read_estrutura_facade("2")
        escolhidos = []
        for escola in escola:
            escolhidos.append(escola['id'])
        self.facade.delete_estrutura_facade("2", escolhidos)

    def _test_create_delete_escola(self):
        self._create_escola()
        self._delete_escola()

    def _test_pesquisa_escola(self):
        self._create_escola()
        self._pesquisa_escola()
        self._delete_escola()

    def _test_update_escola(self):
        self._create_escola()
        self._update_escola()
        self._delete_escola()

    def _test_pesquisa_escola(self):
        self._pesquisa_escola()

    def _test_delete_escola(self):
        self._update_rede()
        self._delete_rede()

    """FIM TESTE ESCOLA"""
    """TESTE TURMA"""

    def _create_turma(self):
        turma1 = self.facade.create_estrutura_facade(nome="Knight", tipo_estrutura="3", serie="1", vinculo_escola="1",
                                                     quem_criou="Ni")
        self.assertIsNot(turma1, None)

    def _search_turma(self):
        turma1 = self.facade.search_estrutura_facade(tipo_estrutura="3", nome="Knight")
        self.assertIn(turma1['nome'], "Knight")
        self.assertIn(turma1['quem_criou'], "Ni")

    def _vincular_professor_turma(self):
        turma = self.facade.search_turma_facade("Knight")
        professor = self.facade.search_observador_facade("Monty")
        self.facade.vincular_professor_turma_facade(turma['id'], professor['id'])

    def _ver_professor_turma(self):
        turma = self.facade.search_turma_facade("Knight")
        professor_vinculado = self.facade.ver_professor_turma_facade(turma['id'])
        for p in professor_vinculado:
            prof = p
        professor = self.facade.search_observador_id_facade(prof)

        self.assertEqual(professor.nome, 'Monty')
        self.assertEqual(professor.email, 'Monty@python.com.br')

    def _delete_turma(self):
        turmas = self.facade.read_estrutura_facade("3")
        escolhidos = []
        for turmas in turmas:
            escolhidos.append(turmas['id'])
        # self.facade.delete_turma_facade_test(escolhidos)

    def test_create_delete_turma(self):
        self._create_turma()
        self._delete_turma()

    def _test_vincular_professor_turma(self):
        self._create_turma()
        self._create_observador()
        self._vincular_professor_turma()
        self._ver_professor_turma()
        self._delete_observador()
        self._delete_turma()

    def test_create_search_delete_turma(self):
        self._create_turma()
        self._search_turma()
        # self._delete_turma()

    """FIM TESTE TURMA """

    """TESTE FACADE HISTORICO"""

    def _create_historico(self):
        self.facade.create_estrutura_facade("Egg", "ADMINISTRADOR")

    def _read_historico(self):
        historico = self.facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['historico'])
        self.assertIsNot(historico, [])

    def test_create_historico(self):
        self._create_aluno()

    def test_read_historico(self):
        self._read_historico()

    """FIM TESTE FACADE HISTORICO"""

    """TESTE FACADE MEDALHAS"""

    def _create_medalha(self):
        medalha = self.facade.create_estrutura_facade(tipo_estrutura='5', nome='cheese', tipo_medalha="1")
        self.assertIsNot(medalha, None)

    def _read_medalha(self):
        medalha = self.facade.read_estrutura_facade(tipo_estrutura='5')
        medalha1 = self.facade.search_estrutura_facade(tipo_estrutura='5', nome='cheese')
        self.assertIn(medalha1['id'], medalha[-1].values())

    def _delete_medalha(self):
        '''teste de inativos '''
        escolhidos = []
        for medalhas in medalhas:
            escolhidos.append(medalhas['id'])
        self.facade.delete_medalha_facade(escolhidos)

    def test_create_delete_medalha(self):
        self._create_medalha()
        # self._delete_medalha()

    def test_read_medalha(self):
        self._create_medalha()
        self._read_medalha()
        # self._delete_medalha()

    """FIM DE TESTE FACADE MEDALHAS"""

    """INICIO DE TESTE FACADE DE LOJA"""

    def _create_item(self):
        iten1 = self.facade.create_estrutura_facade(nome="burroquandofoge", tipo_estrutura='4', tipo_item='1', preco=0)
        self.assertIsNot(iten1, None)

    def _read_item(self):
        self._create_item()
        item1 = self.facade.read_estrutura_facade(tipo_estrutura='4')

    def _delete_item(self):

        itens = self.facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'])

        escolhidos = []
        for itens in itens:
            escolhidos.append(itens['id'])
        self.facade.delete(escolhidos)

    """def test_create_delete_iten(self):
        self._create_item()
        self._delete_item()"""

    def test_read_item(self):
        self._read_item()

    """TESTE INATIVOS"""

    def _transferir_atores_inativos(self):
        self._anotacoes_no_aluno()
        self._create_observador()

        # iten1 = self.facade.create_estrutura_facade(nome="burroquandofoge", '1', preco=0)
        # self.assertIsNot(iten1, None)

        aluno1 = self.facade.create_aluno_facade(nome="thanos", escola="Estalo", senha="123", vinculo_rede="0",
                                                 matricula='2929')
        # item2 = self.facade.search_estrutura_facade("burroquandofoge")
        self.assertEqual(aluno1, True)
        # self.assertIsNot(item2,None)

        alunoer1 = self.facade.search_aluno_nome_objeto_facade("egg")
        self.assertIsNot(alunoer1, None)

        aluno2 = self.facade.search_aluno_nome_objeto_facade("thanos")
        self.assertIsNot(aluno2, None)

        aluno2_pos = self.facade.search_aluno_nome_objeto_facade("thanos")
        self.assertIsNot(aluno2_pos, None)

        observador1 = self.facade.search_observador_inativos_facade("Monty")
        self.assertIsNot(observador1, None)

        inativados = [alunoer1, aluno2_pos, observador1]
        self.facade.create_zInativos_atores_facade(inativados)

        ovo_morto = self.facade.pesquisa_inativos_facade("egg")
        self.assertIsNot(ovo_morto, None)

        mensagem = "Isto é uma mensagem de teste"
        mensagem2 = "tetativa..."
        ovo_falecido = self.facade.pesquisa_aluno_nome_objeto_facade("egg")
        self.assertEqual(ovo_falecido, [])
        self.assertEqual(ovo_morto.nome, alunoer1.nome)
        self.assertEqual(ovo_morto.anotacoes_aluno[0], mensagem.encode('utf-8'))
        self.assertEqual(ovo_morto.anotacoes_aluno[1], mensagem2.encode('utf-8'))

        thanos_morto = self.facade.pesquisa_inativos_facade("thanos")
        self.assertEqual(thanos_morto.nome, aluno2_pos.nome)
        self.assertEqual(thanos_morto.senha, aluno2_pos.senha)
        self.assertEqual(thanos_morto.tipo_usuario, aluno2_pos.tipo_aluno)
        self.assertEqual(thanos_morto.cor, aluno2.cor)
        self.assertEqual(thanos_morto.rosto, aluno2.rosto)
        self.assertEqual(thanos_morto.acessorio, aluno2.acessorio)
        self.assertEqual(thanos_morto.corpo, aluno2.corpo)
        self.assertEqual(thanos_morto.pontos_de_vida, aluno2.pontos_de_vida)
        self.assertEqual(thanos_morto.pontos_de_moedas, aluno2.pontos_de_moedas)
        self.assertEqual(thanos_morto.vinculo_escola, aluno2.vinculo_escola)
        self.assertEqual(thanos_morto.vinculo_turma, aluno2.vinculo_turma)
        self.assertEqual(aluno2.itens_comprados[-1], thanos_morto.itens_comprados[0])

        observador1_morto = self.facade.pesquisa_inativos_facade("Monty")
        self.assertIsNot(observador1_morto, None)
        observador1_inexistente = self.facade.search_observador_inativos_facade("Monty")
        self.assertEqual(observador1_inexistente, [])

    def _inativar_estruturas(self):
        self._create_escola()
        self.facade.search_escola_facade()
        self.facade.create_zInativos_estrutura_facade()

    def _ressuscitar_usuarios(self):
        self._transferir_atores_inativos()
        ovo_morto = self.facade.pesquisa_inativos_facade("egg")
        self.assertIsNot(ovo_morto, None)

        ovo_vivo = self.facade.reativar_usuario_facade(ovo_morto)
        self.assertEqual(ovo_vivo, True)

        fenix = self.facade.search_aluno_nome_facade("egg")
        self.assertIsNot(fenix, None)

        aluno1 = self.facade.search_aluno_nome_facade("egg")
        self.assertEqual(fenix.senha, aluno1.senha)

        cem_observador1 = self.facade.pesquisa_inativos_facade("Monty")
        self.assertIsNot(cem_observador1, None)

        observador1 = self.facade.search_observador_inativos_facade("Monty")
        self.assertIsNot(observador1, None)

        observador = self.facade.reativar_usuario_facade(cem_observador1)
        self.assertEqual(observador, True)

        cem_observador_pos = self.facade.pesquisa_inativos_facade("Monty")
        self.assertEqual(cem_observador_pos, [])

    def _read_inativados(self):
        self._transferir_atores_inativos()
        read_cem = self.facade.read_inativos_facade()
        self.assertIsNot(read_cem, None)

    def _test_create_atores_inativos(self):
        self._transferir_atores_inativos()

    def _test_create_estruturas_inativas(self):
        self._inativar_estruturas()

    def _test_reativar_usuario(self):
        self._ressuscitar_usuarios()

    def _test_read_inativos(self):
        self._read_inativados()

    def tearDown(self):
        self.facade.apagartudo()

    # def test_substituto_de_webtest(self):
    #     self._create_observador()


if __name__ == '__main__':
    unittest.main()

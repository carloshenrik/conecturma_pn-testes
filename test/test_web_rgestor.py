from index import application
import unittest
from webtest import TestApp, TestResponse
import sys
from http.cookiejar import CookieJar

test_app = TestApp(application, cookiejar=CookieJar())
test_response = TestResponse()

sys.path.append('../')


class BlackBoxTest(unittest.TestCase):
    def setUp(self):
        # test_app.post('/escola/create_escola', dict(nome="Escola Conecturma",telefone="21 99445732", cep=""))
        test_app.post('/observador/create_observador_gestor',
                      dict(nome='smoketoomuch', senha='bat', telefone="(21) 22134562",
                           cpf="0",email="tent@c.ul.os",tipo_observador="1",rede="3"))
        """rede =1 (smoketoomuch)
        rede=2 (Ironside e Malone)
        rede=3 (confuse-a-cat)"""

        test_app.post('/login_observador', dict(usuario='smoketoomuch', senha='bat'))

    def _fixgestor(self):
        res = test_app.post('/rede/criar_rede',dict(nome_rede="Ironside e Malone", telefone="(21) 2233-2649"))
        res1 = test_app.post('/escola/criar_escola',
                             dict(vinculo_rede="3", nome="confuse-a-cat", telefone="159874365", cep="22298111",
                                  estado="Solido meio liquido", uf="AC",
                                  numero="42"))
        res2 = test_app.post('/turma/cadastro_turma', dict(turma_nome="cheese shop", serie="2", escola="4", ))
        """escola=1 da o nome da escola como "smoketoomuch"
           escola=2 da nome da escola como "cheese shop"
           escola=3 da o nome da escola como "confuse-a-cat"
        """
        res3 = test_app.post('/observador/create_observador_professor',
                             dict(nome='theLarch', senha="spam", telefone="21 99887342", email="teste@teste.test.te",
                                  tipo_observador="3", escola="4", vinculo_rede="3"))
        res4 = test_app.post('/aluno_cadastro', dict(aluno_nome='Wizzo', escola="4", senha='naosei'))


    def test_escola(self):
        self._fixgestor()
        res = test_app.get('/escola')
        self.assertEqual(res.status_int, 200)
        self.assertIn('''<a href="/">
                <button>Voltar</button>
            </a>''', res.text, res.text)
        self.assertIn('''<a href="/escola/escola_cadastro">
                <button>criar escola</button>
            </a>''', res.text, res.text)
        self.assertIn("confuse-a-cat", res.text, res.text)
        self.assertIn("Ironside e Malone", res.text,res.text)

    def test_cadastro_escola(self):
        self._fixgestor()
        res = test_app.get('/escola/escola_cadastro')
        self.assertEqual(res.status_int,200)
        self.assertIn('<form action="/escola/criar_escola" method="post">',res.text,res.text)
        self.assertIn('<button type="submit">Enviar</button>',res.text,res.text)
        self.assertIn('<select name = "rede">', res.text, res.text)
        self.assertIn('Ironside e Malone', res.text,res.text)
        self.assertIn('''<a href="/escola"><button>Voltar</button></a>''',res.text,res.text)

    def test_turma(self):
        self._fixgestor()
        res = test_app.get('/turma')
        self.assertEqual(res.status_int,200)
        self.assertIn('''<a href="/turma/turma_cadastro"><button>Cadastro turma</button></a>''', res.text, res.text)
        self.assertIn('''<a href="/"><button>Voltar</button></a>''', res.text, res.text)
        self.assertIn('''cheese shop''', res.text, res.text)
        self.assertIn('''confuse-a-cat''',res.text,res.text)

    def test_usuario(self):
        self._fixgestor()
        res = test_app.get('/usuario')
        self.assertEqual(res.status_int, 200)
        self.assertIn('''<form action="usuario/redirect_cadastro">''', res.text, res.text)
        self.assertIn('''<button type="submit" >+ Usuário</button>''', res.text, res.text)
        self.assertIn("Wizzo", res.text, res.text)
        self.assertIn("theLarch", res.text, res.text)

    def test_aluno_cadastro(self):
        res = test_app.get('/aluno/cadastro_aluno')
        self.assertEqual(res.status_int, 200)
        self.assertIn('''<form action="/aluno_cadastro" method="post">''', res.text, res.text)
        self.assertIn('''</select><br>
            <button type="submit">Enviar</button>
        </form>
        <a href="/usuario"><button>Voltar</button></a>''', res.text, res.text)

    def test_professor_cadastro(self):
        res=test_app.get('/observador/cadastro?tipo_observador=3')
        self.assertEqual(res.status_int,200)
        self.assertIn('''<form action="/observador/create_observador_professor" method="post"> <br>''', res.text,res.text)
        self.assertIn(' <button type="submit">Enviar</button>', res.text, res.text)
        self.assertIn('''<a href="/usuario"><button>Voltar</button></a>''', res.text, res.text)

    def test_diretor_cadastro(self):
        res=test_app.get('/observador/cadastro?tipo_observador=2')
        self.assertEqual(res.status_int,200)
        self.assertIn('<form action="create_observador_diretor" method="post"> <br>',res.text,res.text)
        self.assertIn('<input type="hidden" name="tipo_observador" value="2">',res.text,res.text)
        self.assertIn('<option value="4">confuse-a-cat</option>',res.text,res.text)
        self.assertIn('''<button type="submit">Enviar</button>
        </form>
        <a href="/usuario"><button>Voltar</button></a>''',res.text,res.text)
    
if __name__ == '__main__':
    unittest.main()

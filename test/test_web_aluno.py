from index import application
import unittest
from webtest import TestApp, TestResponse
import sys
from http.cookiejar import CookieJar

test_app = TestApp(application, cookiejar=CookieJar())
test_response = TestResponse()

sys.path.append('../')


# os.environ['WEBTEST_TARGET_URL'] = 'http://localhost:8888'

# test_app.set_cookie('login', '2524')
# test_app.authorization()


class BlackBoxTest(unittest.TestCase):
    def setUp(self):
        test_app.post('/aluno_cadastro', dict(aluno_nome='eric', escola="Escola conecturma", senha='idle'))
        test_app.post('/login_aluno', dict(usuario='eric', senha='idle'))

    def _fixaluno(self):

        # res2 = test_app.post('/turma_cadastro', dict(turma_nome='ni'))
        # res3 = test_app.post('/turma_cadastro', dict(turma_nome='parrot'))
        res4 = test_app.post('/cadastro_item' , dict(nome='burro quando foge',tipo='3',preco='0'))

        """ INICIO TESTE PASTA ALUNO"""

    """Pagina aluno.tpl"""

    def test_aluno_inicio(self):
        res = test_app.get('/jogar_conecturma')
        self.assertEqual(res.status_int, 200)
        self.assertIn('''<form action="/jogos" method="get">''', res.text, res.text)
        self.assertIn('''<a href="/loja"><button>Loja</button></a>''', res.text, res.text)
        self.assertIn('''<a href="/aluno/ver_itens_comprados"><button>Ver Itens</button></a>''', res.text, res.text)
        self.assertIn('''<a href="/sair"><button>Sair</button></a>''', res.text, res.text)

    def test_acesso_loja(self):
        self._fixaluno()
        res= test_app.get('/loja')
        self.assertEqual(res.status_int,200)
        self.assertIn('<form action="/compras_loja">', res.text, res.text)
        self.assertIn('''<button type="submit" name="id" value=''', res.text, res.text)
        self.assertIn('''Comprar</button>''',res.text,res.text)

    def test_ver_itens(self):
        res= test_app.get('/aluno/ver_itens_comprados')
        self.assertEqual(res.status_int, 200)
        # self.assertIn('<form action="/equipar_item" method="post">', res.text, res.text)
        self.assertIn('<a href="/aluno"><button>Voltar</button></a>', res.text, res.text)


test_app.reset()
if __name__ == '__main__':
    unittest.main()

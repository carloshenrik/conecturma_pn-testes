import webob
import webtest

from index import application
import unittest
from webtest import TestApp, TestResponse
import sys
from http.cookiejar import CookieJar

# from webob import Response
#
#
# response =TestResponse(webob.Response)

test_app = TestApp(application, cookiejar=CookieJar())
test_response = TestResponse()
sys.path.append('../')


class BlackBoxTest(unittest.TestCase):
    def setUp(self):
        # test_app.post('/login_observador',dict(usuario= 'administrator', senha="@onde2929"))
        test_app.post('/observador/create_observador',
                      dict(nome='proof', senha="spam", telefone="21 99887342",cpf="0", email="teste@teste.test.te",
                           tipo="3", escola="2",rede="0",vinculo_turma="2"))
        test_app.post('/login_observador', dict(usuario='proof', senha='spam'))

    def _fixprof(self):
        res =test_app.post('/create_medalha', dict(nome="Medalha0",tipos="1"))
    # res1 = test_app.post('/observador/create_observador_gestor',)

    def test_pagina_inicial(self):
        res = test_app.get('/gestao_aprendizagem')
        self.assertEqual(res.status_int, 200)
        self.assertIn('<a href="/usuario">USUÁRIOS</a><br>', res.text, res.text)
        self.assertIn('<a href="/medalha_cadastro">Criar medalha</a><br>', res.text, res.text)
        self.assertIn('<a href="/ler_medalha">Ler medalhas criadas</a><br>', res.text, res.text)

    def test_medalha_cadastro(self):
        res = test_app.get('/medalha_cadastro')
        self.assertEqual(res.status_int, 200)
        self.assertIn('<form action="/create_medalha" method="post" >', res.text, res.text)
        self.assertIn('<button type="submit">Enviar</button>', res.text, res.text)
        self.assertIn('''<a href="/gestao_aprendizagem">
            <button>voltar</button>
        </a>''', res.text, res.text)

    def test_ler_medalha(self):
        self._fixprof()
        res = test_app.get('/ler_medalha')
        self.assertEqual(res.status_int, 200)
        self.assertIn('Medalha0',res.text,res.text)


if __name__ == '__main__':
    unittest.main()

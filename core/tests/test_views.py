from model_mommy import mommy
from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.views import IndexView


class IndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.nome = 'Wesley Gurgel'
        self.email = 'wesleygurgel27@gmail.com'
        self.assunto = 'Um Assunto Qualquer'
        self.mensagem = 'Uma mensagem qualquer'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': self.nome,
            'assunto': self.assunto
        }

        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
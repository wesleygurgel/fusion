from model_mommy import mommy
from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):
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

        self.form = ContatoForm(data=self.dados)

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()
        print(f'{res1} - {str(res1)}')

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()
        print(f'{res2} - {str(res2)}')

        self.assertEquals(res1, res2)
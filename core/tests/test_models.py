from model_mommy import mommy
import uuid
from django.test import TestCase
from core.models import get_file_path


class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):

    def setUp(self) -> None:
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):

    def setUp(self) -> None:
        self.cargo = mommy.make('Cargo')
        print(type(self.cargo))

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):

    def setUp(self) -> None:
        self.funcionario = mommy.make('Funcionario')
        print(type(self.funcionario))

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)


class FeaturesTestCase(TestCase):

    def setUp(self) -> None:
        self.features = mommy.make('Features')
        print(type(self.features))

    def test_str(self):
        self.assertEquals(str(self.features), self.features.titulo)

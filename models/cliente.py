from datetime import date
from util.helper import str_para_date, valida_cpf, date_para_str


class Cliente:
    contador = 100

    def __init__(self, nome: str, sobrenome: str, cpf: str, data_nascimento: str, senha: str):
        self._nome: str = nome
        self._sobrenome: str = sobrenome
        self._cpf: str = valida_cpf(cpf)
        self._data_nascimento: date = str_para_date(data_nascimento)
        self._data_cadastro: date = date.today()
        self._idade = date.today().year - str_para_date(data_nascimento).year
        self._senha = senha
        self._codigo = Cliente.contador
        Cliente.contador += 1

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def sobrenome(self) -> str:
        return self._sobrenome

    @property
    def idade(self) -> int:
        return self._idade

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def data_cadastro(self):
        return self._data_cadastro

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self: object, nova_senha: str):
        self.senha = nova_senha

    @property
    def codigo(self):
        return self._codigo

    def __str__(self):
        return f'Nome: {self.nome}\n' \
               f'Sobrenome: {self.sobrenome}\n' \
               f'Idade: {self.idade}\n' \
               f'Data Nascimento: {date_para_str(self.data_nascimento)}\n' \
               f'Data Cadastro: {date_para_str(self.data_nascimento)}'

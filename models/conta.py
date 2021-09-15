from models.cliente import Cliente
from util.helper import formata_float_moeda


class Conta:
    codigo = 1001

    def __init__(self, cliente: Cliente):
        self._numenro: int = Conta.codigo
        self._senha: str = cliente.senha
        self._cliente: Cliente = cliente
        self._saldo: float = 0
        self._limite_fixo: float = 0
        self._limite: float = 100
        self._saldo_total = self.calcula_saldo_total
        Conta.codigo += 1

    @property
    def numero(self: object) -> int:
        return self._numenro

    @property
    def senha(self: object) -> str:
        return self._senha

    @senha.setter
    def senha(self: object, nova_senha: str):
        self.senha = nova_senha

    @property
    def cliente(self: object) -> Cliente:
        return self._cliente

    @property
    def saldo(self: object) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        self._saldo = valor

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor: float):
        self._limite = valor

    @property
    def limite_fixo(self):
        return self._limite_fixo

    @limite_fixo.setter
    def limite_fixo(self, valor: float):
        self._limite_fixo = valor

    @property
    def saldo_total(self: object) -> float:
        return self._saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self._saldo_total = valor

    @property
    def calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float):
        if valor > 0:
            restante = valor
            self.saldo += valor
            self.saldo_total = self.calcula_saldo_total
            print(f'Deposito de {formata_float_moeda(valor)} efetuado com sucesso. ')
        else:
            print('Erro ao efetuar o depósito, tente novamente.')

    def sacar(self: object, valor: float):
        if 0 < valor <= self.saldo_total:
            if valor <= self.saldo:
                self.saldo -= valor
                self.saldo_total = self.calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite += restante
                self.saldo = 0
                self.saldo_total = self.calcula_saldo_total
            print(f'Saque de {formata_float_moeda(valor)} efetuado com sucesso. ')
        else:
            print('Erro ao efetuar o saque, verifique o valor e o saldo.')

    def transferir(self: object, destino: object, valor: float):
        if 0 < valor <= self.saldo_total:
            if valor <= self.saldo:
                self.saldo -= valor
                self.saldo_total = self.calcula_saldo_total
                destino.saldo += valor
                destino.saldo_total = self.calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite += restante
                self.saldo = 0
                self.saldo_total = self.calcula_saldo_total
                destino.saldo += valor
                destino.saldo_total = self.calcula_saldo_total
            print(f'Transferência de {formata_float_moeda(valor)} efetuada com sucesso.')
        else:
            print('Erro ao efetuar a transferência, verifique valor e saldo.')

    def alterar_limite(self: object, valor: float):
        self.limite_fixo = valor
        if 0 < valor <= 2500:
            self.limite = valor
            self.saldo_total = self.calcula_saldo_total
            print('Limite alterado com sucesso\n'
                  f'Novo limite de {formata_float_moeda(valor)}')
        else:
            print('Erro ao alterar o liminte, verifique o valor')

    def pagar_limite(self: object):
        if self.limite < self.limite_fixo:
            divida = self.limite_fixo - self.limite
            if divida <= self.saldo:
                self.saldo -= divida
                self.limite += divida
                self.saldo_total = self.calcula_saldo_total
                print(f'Valor de {formata_float_moeda(divida)} pago com sucesso!')
            else:
                print('Saldo insuficiente')
        else:
            print('Você não usou o valor do limite')

    def __str__(self):
        return f'Numero conta: {self.numero} \nNome: {self.cliente.nome} {self.cliente.sobrenome} \n' \
               f'Saldo: {formata_float_moeda(self.saldo)} \nSaldo Total: {formata_float_moeda(self.saldo_total)}' \
               f'\nLimite: {formata_float_moeda(self.limite)}'

from typing import List
from time import sleep


from models.conta import Conta, Cliente
from util.helper import cabecalho, valida_cpf, formata_float_moeda

contas: List[Conta] = []


def main():
    menu()


def menu():
    cabecalho('Banco Ouro Cred')
    print('Selecione uma opção:\n'
          '1 -> Criar Conta\n'
          '2 -> Entrar Conta\n'
          '3 -> Deposito sem Cartão\n'
          '4 -> Listar Contas\n'
          '5 -> Sair do Sistema')
    print()
    try:
        opc = int(input('Escolha um opção: '))

        if opc == 1:
            criar_conta()
        elif opc == 2:
            menu_conta()
        elif opc == 3:
            deposito_sem_cartao()
        elif opc == 4:
            listar_contas()
        elif opc == 5:
            print('Saindo do sistema...')
            sleep(2)
            print('Volte Sempre!')
            exit(0)
        else:
            print('Opção inválida')
    except ValueError:
        print('Opção inválida')

    sleep(2)
    menu()


def criar_conta():
    cabecalho('cadastro cliente')
    print('Informe os dados do cliente')
    nome = str(input('Nome: '))
    sobrenome = str(input('Sobrenome: '))
    cpf = ' '
    while cpf:
        cpf = str(input('CPF: '))
        if valida_cpf(cpf):
            break
        else:
            print('CPF inválido')
    nasc = str(input('Data Nascimento [dd/mm/yyyy]: '))
    senha = ''
    while len(senha) != 4:
        senha = str(input('Informe sua senha: '))
        if len(senha) != 4:
            print('Senha precisa ter 4 digitos!')
    confirma_senha = ''
    while confirma_senha != senha:
        confirma_senha = str(input('Confirma a senha: '))
        if confirma_senha != senha:
            print('Senha não confere!')

    cliente: Cliente = Cliente(nome, sobrenome, cpf, nasc, senha)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Cadastro Realizado com sucesso!')
    print(conta)
    sleep(2)
    menu()


def menu_conta():
    if len(contas) > 0:
        numero = int(input('Infomre o numero da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            senha = str(input('Informe sua senha: '))
            if senha == conta.senha:
                conta_cliente(conta)
            else:
                print('Senha não confere')
        else:
            print(f'Conta com o numero: {numero} não foi encontrada.')
    else:
        print('Não existem contas cadastradas.')
    sleep(2)
    menu()


def conta_cliente(conta:Conta):
    cabecalho('conta')
    print(f'Bem Vindo {conta.cliente.nome} !')
    print()
    print('Selecione uma opção:\n'
          '1 -> Efetuar depósito\n'
          '2 -> Efetuar saque\n'
          '3 -> Efetuar Tranferência\n'
          '4 -> Mudar Senha\n'
          '5 -> Extrato\n'
          '6 -> Alterar Limite\n'
          '7 -> Pagar Limite\n'
          '8 -> Sair da Conta')
    try:
        opc = int(input('Escolha uma opção: '))

        if opc == 1:
            efetuar_deposito(conta)
        elif opc == 2:
            efetuar_saque(conta)
        elif opc == 3:
            efetuar_transferencia(conta)
        elif opc == 4:
            mudar_senha(conta)
        elif opc == 5:
            extrato(conta)
        elif opc == 6:
            alterar_limite(conta)
        elif opc == 7:
            pagar_limite(conta)
        elif opc == 8:
            print('Saindo da Conta!')
            sleep(2)
            menu()
        else:
            print('Opção Inválida!')
    except ValueError:
        print('Opção inválida')


def deposito_sem_cartao():
    if len(contas) > 0:
        cabecalho('deposito')
        numero = int(input('Informe o numero da conta: '))

        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor = float(input('Informe o valor de depósito: '))
            conta.depositar(valor)

        else:
            print(f'Conta com o numero: {numero} não foi encontrada.')
    else:
        print('Não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito(conta: Conta):
    cabecalho('deposito')
    valor = float(input('Informe o valor para depósito: '))
    conta.depositar(valor)
    sleep(2)
    conta_cliente(conta)


def efetuar_saque(conta: Conta):
    cabecalho('saque')
    valor = float(input('Informe o valor para saque: '))
    conta.sacar(valor)
    sleep(2)
    conta_cliente(conta)


def efetuar_transferencia(conta: Conta):
    cabecalho('transferência')
    numero = int(input('Informe o numero da conta para transferência: '))

    conta_d: Conta = buscar_conta_por_numero(numero)
    if conta:
        valor = float(input('Informe o valor para transferir: '))
        conta.transferir(conta_d, valor)
    else:
        print(f'Conta com numero {numero} não foi encontrada.')
    sleep(2)
    conta_cliente(conta)


def mudar_senha(conta: Conta):
    cabecalho('alterar senha')
    senha = str(input('Informe a senha atual: '))
    if conta.senha == senha:
        nova_senha = ''
        while len(nova_senha) != 4:
            nova_senha = str(input('Insira sua nova senha [4 - digitos]: '))
            if len(nova_senha) != 4:
                print('Senha presisa ter 4 digitos')
        confirma_senha = ''
        while confirma_senha != nova_senha:
            confirma_senha = str(input('Confirme senha: '))
            if confirma_senha != nova_senha:
                print('Senha não confere.')
        conta.senha = nova_senha
        print('Senha alterada com sucesso!')
    else:
        print('Senha não confere')
    sleep(2)
    conta_cliente(conta)


def extrato(conta: Conta):
    cabecalho('extrato')
    print(conta)
    sleep(2)
    conta_cliente(conta)


def alterar_limite(conta: Conta):
    cabecalho('alterar limite')
    print('Limite disponivel R$ 00,00 a R$ 2.500,00')
    print(f'Limite atual: {formata_float_moeda(conta.limite)}')
    novo_limite = float(input('informe o novo limite: '))
    conta.alterar_limite(novo_limite)
    sleep(2)
    conta_cliente(conta)


def pagar_limite(conta: Conta):
    cabecalho('pagar limite')
    conta.pagar_limite()
    sleep(2)
    conta_cliente(conta)


def listar_contas():
    if len(contas) > 0:
        for conta in contas:
            print(conta)
            print()
            sleep(1)
    else:
        print('Não existem contas cadastradas.')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    for conta in contas:
        if conta.numero == numero:
            c = conta
    return c


if __name__ == '__main__':
    main()

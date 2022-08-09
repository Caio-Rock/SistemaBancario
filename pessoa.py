class Pessoa:

    __slots__ = ['_nome', '_cpf', '_endereco', '_telefone', '_usuario', '_senha', '_numero_conta', '_saldo']

    def __init__(self, nome, cpf, endereco, telefone, usuario, senha, numero_conta, saldo=0.0):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._telefone = telefone
        self._usuario = usuario
        self._senha = senha
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor):
        self._endereco = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    @property
    def usuario(self):
        return self._usuario

    @property
    def senha(self):
        return self._senha

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo
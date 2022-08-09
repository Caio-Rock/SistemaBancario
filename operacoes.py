from pessoa import Pessoa

class Operacoes():

    __slots__ = ['_lista_pessoas']

    def __init__(self):
        self._lista_pessoas = []

    @property
    def lista_pessoas(self):
        return self._lista_pessoas

    def verifica_login(self, usuario, senha):
        if( self._lista_pessoas == [] ):
            return False

        else:
            for objeto in self._lista_pessoas:
                if( objeto.usuario == usuario and objeto.senha == senha ):
                    return True
                
            return False

    def cadastrar(self, pessoa):
        existe_cpf = self.verificar_cpf(pessoa.cpf)
        existe_usuario = self.verificar_cpf(pessoa.usuario)
        existe_numero_conta = self.verificar_numero_conta(pessoa.numero_conta)

        if( existe_cpf == None and existe_usuario == None and existe_numero_conta == None ):
            self._lista_pessoas.append(pessoa)
            return True
        else:
            return False

    def buscar(self, cpf):
        for valor in self._lista_pessoas:
            if ( valor.cpf == cpf ):
                return valor

        return None

    def verificar_cpf(self, cpf):
        for valor in self._lista_pessoas:
            if ( valor.cpf == cpf ):
                return True

        return None

    def verificar_usuario(self, usuario):
        for valor in self._lista_pessoas:
            if ( valor.usuario == usuario ):
                return True

        return None

    def verificar_numero_conta(self, numero_conta):
        for valor in self._lista_pessoas:
            if ( valor.numero_conta == numero_conta ):
                return True

        return None

    def verificar_tranferencia(self, usuario_logado, conta_destino, valor_saque):
        for objeto in self._lista_pessoas:
            if( objeto.usuario == usuario_logado ):
                if( objeto.numero_conta == conta_destino ):
                    return False
                else:
                    verifica_conta = self.verificar_numero_conta(conta_destino)

                    if( verifica_conta == True ):
                        if( objeto._saldo >= valor_saque ):
                            return True
                        else:
                            return False
        
        return False

    def depositar(self, usuario_logado, valor):
        if( valor > 0 ):
            for pessoa in self._lista_pessoas:
                if( pessoa.usuario == usuario_logado ):
                    pessoa._saldo += valor
                    return True
        else:
            return False

    def sacar(self, usuario_logado, valor):
        if( valor > 0.0 ):
            for pessoa in self._lista_pessoas:
                if( pessoa.usuario == usuario_logado ):
                    if( valor <= pessoa._saldo ):
                        pessoa._saldo -= valor
                        return True

                    else:
                        return False
        else:
            return False

    def transferir(self, conta_destino, valor):
        if( valor > 0.0 ):
            retorno = self.verificar_numero_conta(conta_destino)

            if( retorno == True ):
                for objeto in self._lista_pessoas:
                    if( objeto.numero_conta == conta_destino ):
                        objeto._saldo += valor
                        return True

                return False

        else:
            return False
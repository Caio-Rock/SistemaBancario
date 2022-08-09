import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from pessoa import Pessoa
from operacoes import Operacoes

from tela_login import Tela_Login
from tela_cadastros import Tela_Cadastros
from tela_operacoes import Tela_Operacoes
from tela_buscas import Tela_Buscas
from tela_depositos import Tela_Depositos
from tela_saques import Tela_Saques
from tela_transferencias import Tela_Transferencias


class Ui_Main(QtWidgets.QWidget):

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1000, 700)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastros = Tela_Cadastros()
        self.tela_cadastros.setupUi(self.stack1)

        self.tela_operacoes = Tela_Operacoes()
        self.tela_operacoes.setupUi(self.stack2)

        self.tela_buscas = Tela_Buscas()
        self.tela_buscas.setupUi(self.stack3)

        self.tela_depositos = Tela_Depositos()
        self.tela_depositos.setupUi(self.stack4)

        self.tela_saques = Tela_Saques()
        self.tela_saques.setupUi(self.stack5)

        self.tela_transferencias = Tela_Transferencias()
        self.tela_transferencias.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)


class Main(QMainWindow, Ui_Main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.usuario_logado = ''
        self.operacoes = Operacoes()

        self.tela_login.pushButton.clicked.connect(self.encerrar_programa)
        self.tela_login.pushButton_2.clicked.connect(self.abrir_tela_operacoes)
        self.tela_login.pushButton_3.clicked.connect(self.abrir_tela_cadastros)

        self.tela_cadastros.pushButton.clicked.connect(self.botao_cadastrar)
        self.tela_cadastros.pushButton_2.clicked.connect(self.abrir_tela_login)

        self.tela_operacoes.pushButton.clicked.connect(self.abrir_tela_buscas)
        self.tela_operacoes.pushButton_2.clicked.connect(self.abrir_tela_depositos)
        self.tela_operacoes.pushButton_3.clicked.connect(self.abrir_tela_saques)
        self.tela_operacoes.pushButton_4.clicked.connect(self.abrir_tela_transferencias)
        self.tela_operacoes.pushButton_5.clicked.connect(self.abrir_tela_login)

        self.tela_buscas.pushButton.clicked.connect(self.botao_buscar)
        self.tela_buscas.pushButton_2.clicked.connect(self.voltar_buscas)

        self.tela_depositos.pushButton.clicked.connect(self.botao_depositar)
        self.tela_depositos.pushButton_2.clicked.connect(self.voltar_depositos)

        self.tela_saques.pushButton.clicked.connect(self.botao_sacar)
        self.tela_saques.pushButton_2.clicked.connect(self.voltar_saques)

        self.tela_transferencias.pushButton.clicked.connect(self.botao_transferir)
        self.tela_transferencias.pushButton_2.clicked.connect(self.voltar_transferencias)


    def encerrar_programa(self):
        sys.exit()

    def abrir_tela_login(self):
        self.usuario_logado = ''
        self.QtStack.setCurrentIndex(0)

    def abrir_tela_cadastros(self):
        self.QtStack.setCurrentIndex(1)

    def abrir_tela_operacoes(self):
        usuario = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()

        retorno = self.operacoes.verifica_login(usuario, senha)

        if( retorno ):
            self.usuario_logado = usuario
            self.QtStack.setCurrentIndex(2)

        else:
            QMessageBox.information(None, '', 'Dados não cadastrados!')

        self.tela_login.lineEdit.setText('')
        self.tela_login.lineEdit_2.setText('')

    def abrir_tela_buscas(self):
        self.QtStack.setCurrentIndex(3)

    def abrir_tela_depositos(self):
        self.QtStack.setCurrentIndex(4)

    def abrir_tela_saques(self):
        self.QtStack.setCurrentIndex(5)

    def abrir_tela_transferencias(self):
        self.QtStack.setCurrentIndex(6)

    def voltar_buscas(self):
        self.tela_buscas.lineEdit.setText('')
        self.tela_buscas.lineEdit_2.setText('')
        self.tela_buscas.lineEdit_3.setText('')
        self.tela_buscas.lineEdit_4.setText('')
        self.tela_buscas.lineEdit_5.setText('')
        self.tela_buscas.lineEdit_6.setText('')
        self.tela_buscas.lineEdit_7.setText('')
        self.QtStack.setCurrentIndex(2)

    def voltar_depositos(self):
        self.tela_depositos.lineEdit.setText('')
        self.QtStack.setCurrentIndex(2)

    def voltar_saques(self):
        self.tela_saques.lineEdit.setText('')
        self.QtStack.setCurrentIndex(2)

    def voltar_transferencias(self):
        self.tela_transferencias.lineEdit.setText('')
        self.tela_transferencias.lineEdit_2.setText('')
        self.QtStack.setCurrentIndex(2)

    def botao_cadastrar(self):
        nome = self.tela_cadastros.lineEdit.text()
        cpf = self.tela_cadastros.lineEdit_2.text()
        endereco = self.tela_cadastros.lineEdit_3.text()
        telefone = self.tela_cadastros.lineEdit_4.text()
        usuario = self.tela_cadastros.lineEdit_5.text()
        senha = self.tela_cadastros.lineEdit_6.text()
        numero_conta = self.tela_cadastros.lineEdit_7.text()

        if( nome != '' and cpf != '' and endereco != '' and telefone != '' and usuario != '' and senha != '' and numero_conta != '' ):

            pessoa = Pessoa(nome, cpf, endereco, telefone, usuario, senha, numero_conta)

            if ( self.operacoes.cadastrar(pessoa) ):
                QMessageBox.information(None, '', 'Cadastro realizado!')

                self.tela_cadastros.lineEdit.setText('')
                self.tela_cadastros.lineEdit_2.setText('')
                self.tela_cadastros.lineEdit_3.setText('')
                self.tela_cadastros.lineEdit_4.setText('')
                self.tela_cadastros.lineEdit_5.setText('')
                self.tela_cadastros.lineEdit_6.setText('')
                self.tela_cadastros.lineEdit_7.setText('')

                self.QtStack.setCurrentIndex(0)

            else:
                QMessageBox.information(None, '', 'O número de cpf, usuário ou conta já existe!')

        else:
            QMessageBox.information(None, '', 'Todos os campos devem ser preenchidos!')

    def botao_buscar(self):
        cpf = self.tela_buscas.lineEdit.text()
        pessoa = self.operacoes.buscar(cpf)

        if( pessoa != None ):
            self.tela_buscas.lineEdit_2.setText(pessoa.nome)
            self.tela_buscas.lineEdit_3.setText(pessoa.cpf)
            self.tela_buscas.lineEdit_4.setText(pessoa.endereco)
            self.tela_buscas.lineEdit_5.setText(pessoa.telefone)
            self.tela_buscas.lineEdit_6.setText(pessoa.numero_conta)
            self.tela_buscas.lineEdit_7.setText(str(pessoa.saldo))

        else:
            QMessageBox.information(None, '', 'O cpf informado é inválido!')

    def botao_depositar(self):
        texto = self.tela_depositos.lineEdit.text()
        valor = texto
        valor = float(valor)
        pessoa = self.operacoes.depositar(self.usuario_logado, valor)

        if( texto != '' ):
            if pessoa:
                QMessageBox.information(None, '', 'Depósito realizado!')
            else:
                QMessageBox.information(None, '', 'O valor é inválido!')

        else:
            QMessageBox.information(None, '', 'Todos os campos devem ser preenchidos!')

    def botao_sacar(self):
        texto = self.tela_saques.lineEdit.text()
        valor = texto
        valor = float(valor)
        pessoa = self.operacoes.sacar(self.usuario_logado, valor)

        if( texto != '' ):
            if pessoa:
                QMessageBox.information(None, '', 'Saque realizado!')
            else:
                QMessageBox.information(None, '', 'O valor é inválido!')

        else:
            QMessageBox.information(None, '', 'Todos os campos devem ser preenchidos!')

    def botao_transferir(self):
        conta_destino = self.tela_transferencias.lineEdit.text()
        texto = self.tela_transferencias.lineEdit_2.text()
        valor = texto
        valor = float(valor)

        if( conta_destino != '' and texto != '' and texto != self.usuario_logado ):
            verifica_transferencia = self.operacoes.verificar_tranferencia(self.usuario_logado, conta_destino, valor)

            if( verifica_transferencia == True ):
                saque = self.operacoes.sacar(self.usuario_logado, valor)

                if( saque == True ):
                    pessoa = self.operacoes.transferir(conta_destino, valor)

                    if( pessoa == True ):
                        QMessageBox.information(None, '', 'Transferência realizada!')
                    else:
                        QMessageBox.information(None, '', 'O valor é inválido!')

                else:
                    QMessageBox.information(None, '', 'O valor é inválido!')
            else:
                QMessageBox.information(None, '', 'O valor é inválido!')
        else:
            QMessageBox.information(None, '', 'O valor é inválido!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
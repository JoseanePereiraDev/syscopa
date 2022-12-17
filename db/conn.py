from config import create_log
from .crud import select, delete, insert, update
import tkinter as tk
from tkinter import *
#Ttk treeview não vem com Tkinter padrão
from tkinter import ttk
from tkinter import messagebox


##conexão com banco
import mysql.connector as conn

#criando conexão com o banco
def access(dbuser, dbpass):
  cnx = conn.connect(
    user = dbuser, 
    password = dbpass 
  )

  create_log.logFile('Conectando...')
  try:
    cursor = cnx.cursor()
    create_log.logFile('Verificando conexao com o banco...')
    createDb = ('create database if not exists syscopa;')
    cursor.execute(createDb)
    useDb = ('use syscopa;')
    cursor.execute(useDb)
    create_log.logFile('Banco selecionado!')
    print('\nBanco conectado com sucesso!\n')

 #Select por tabela escolhida
    try:
     print('Veja dados ')
     print('Tecle enter para pular')
     tabela = str(input('Digite tabela: '))
     coluna = str(input('Digite coluna: '))
     condicao = str(input('Qual o campo? (tecle enter para cancelar): '))
     select.selecionar(cursor,tabela,coluna,condicao)
     print()
    except Exception as error:
      create_log.logFile(f'Erro ao chamar select.selecionar:\n{error}')
      print('Erro ao chamar funcao da crud.')


  #Delete tabela por tabela escolhida
    try:
     print('Delete dados')
     print('Tecle enter para pular')
     tabela = str(input('Digite tabela: '))
     coluna = str(input('Digite coluna: '))
     condicao = str(input('Digite o id referente ao dado que deseja exluir: '))
     delete.deletar(cnx,cursor,tabela,coluna,condicao)
    except Exception as error:
      create_log.logFile(f'Erro ao chamar funcao da crud.\n{error}')
      print('Erro ao chamar funcao da crud.')

  #Insert tabela por tabela escolhida
  #insert
    try:
        print('Insira dados')
        print('tecle enter para pular')
        tabela = str(input('Digite tabela: '))
        coluna = str(input('Digite coluna: '))
        valores = str(input('Digite um dado a ser inserido: '))
        insert.inserir(cnx,cursor,tabela,coluna,valores)
    except Exception as error:
          create_log.logFile(f'Erro ao chamar funcao da crud.\n{error}')
          print('Erro ao chamar funcao da crud.')

 
  #Update tabela por tabela escolhida
    try:
      print('Atualize dados')
      print('tecle enter para pular')
      tabela = str(input('Digite tabela a ser atualizada: '))
      coluna = str(input('Digite coluna a ser atualizada: '))
      valores = str(input('Digite o item a ser atualizada (tecle enter para cancelar): '))
      condicao = str(input('Digite a condição/variavel a ser atualizada: '))
      rep_condicao = int(input('Digite o id a ser atualizado: '))
      update.atualizar(cnx,cursor,tabela,coluna,valores,condicao,rep_condicao)
    except Exception as error:
      create_log.logFile(f'Erro ao chamar funcao da crud.\n{error}')
      print('Erro ao chamar funcao da crud.')


  except Exception as error:
    create_log.logFile('Erro de conexao.')
    print('\nFalha na conexao com o banco.\n')
def closeAccess():
  conn.connect().close()

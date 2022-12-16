from config import create_log
from .crud import select
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

  # 1- abrindo conexão
  # 2- o creat_log cria o banco
  # 3- o execute, executa a variavel
  # 4- o "Use" seleciona o banco
  # 5- o segundo execute,executa a variavel
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
     print('Tabela select')
     tabela = str(input('Digite tabela: '))
     coluna = str(input('Digite coluna: '))
     condicao = str(input('Qual o campo? (tecle enter para cancelar): '))
     select.selecionar(cursor,tabela,coluna,condicao)
     print()
    except Exception as error:
      create_log.logFile(f'Erro ao chamar select.selecionar:\n{error}')
      print('Erro ao chamar funcao da crud.')


    # #Select tabela arbitro
    # try:
    #   select.selectArbitro(cursor,'','')
    #   select.selectArbitro(cursor,'Salima Mukansanga','')
    #   select.selectArbitro(cursor,'',8)
    # except Exception as error:
    #   create_log.logFile(f'Erro ao chamar funcao da crud.\n{error}')
    #   print('Erro ao chamar funcao da crud.')

    # #Select tabela tecnico
    # try:
    #   select.selectTecnico(cursor,'','')
    #   select.selectTecnico(cursor,'Paulo Bento','')
    #   select.selectTecnico(cursor,'',25)
    #   select.selectTecnico(cursor,'','')
    # except Exception as error:
    #   create_log.logFile(f'Erro ao chamar funcao da crud.\n{error}')
    #   print('Erro ao chamar funcao da crud.')

    # #Select tabela equipe
    # try:
    #     select.selectEquipe(cursor,'','')
    #     select.selectEquipe(cursor,'','')
    #     select.selectEquipe(cursor,'','')
    # except Exception as error:
    #   create_log.logFile(f'Erro ao chamar funcao da crud.\n{error}')
    #   print('Erro ao chamar funcao da crud.')
    # # Select tabela fase
    # try:
    #   select.selectFase(cursor,'','')
    #   select.selectFase(cursor,'','')
    #   select.selectFase(cursor,'','')
    #   select.selectFase(cursor,'','')
    # except Exception as error:
    #   create_log.logFile(f'Erro ao chamar funcao da crud.\n{error}')
    #   print('Erro ao chamar funcao da crud.')
    #  # Select tabela grupo
    # try:
    #   select.selectGrupo(cursor,'','')
    #   select.selectGrupo(cursor,'','')
    #   select.selectGrupo(cursor,'','')
    #   select.selectGrupo(cursor,'','')
    # except Exception as error:
    #   create_log.logFile(f'Erro ao chamar funcao da crud.\n{error}')
    #   print('Erro ao chamar funcao da crud.')

    # #Seletc tabela partidas
    # try:
    #   select.selectPartidas(cursor,'','')
    #   select.selectPartidas(cursor,'','')
    #   select.selectPartidas(cursor,'','')
    #   select.selectPartidas(cursor,'','')
    #   select.selectPartidas(cursor,'','')
    #   select.selectPartidas(cursor,'','')
    #   select.selectPartidas(cursor,'','')
    #   select.selectPartidas(cursor,'','')
    #   select.selectPartidas(cursor,'','')
    #   select.selectPartidas(cursor,'','')
    # except Exception as error:
    #   create_log.logFile(f'Erro ao chamar funcao da crud.\n{error}')
    #   print('Erro ao chamar funcao da crud.')

  #Delete tabela por tabela escolhida

  #Insert tabela por tabela escolhida
    

  #Update tabela por tabela escolhida

  except Exception as error:
    create_log.logFile('Erro de conexao.')
    print('\nFalha na conexao com o banco.\n')
def closeAccess():
  conn.connect().close()

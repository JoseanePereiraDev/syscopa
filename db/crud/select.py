#criando funçao metodo (recebendo parametros)
from config import create_log

#Select
def selecionar(cursor,tabela,coluna,condicao):
  if condicao != '':
    try:
      #
      cursor.execute(f'select * from {tabela} where {coluna} = "{condicao}";')

      exibicao = cursor.fetchall()
      create_log.logFile(f'`def selecionar` resultado:\n{exibicao}')
      print(f'O registro é: {exibicao}')
      
    except Exception as error:
      create_log.logFile(f'Erro ao executar `def selecionar`:\n{error}')
      #
      print(f'Erro ao executar `def selecionar`:\n{error}')
  else:
    create_log.logFile('Este campo nao existe.')
    #
    print('Este campo nao existe.')



#Select tabela arbitro
# def selectArbitro(cursor,condicao1,condicao2):
#   if condicao1 != '':
#     cursor.execute(f'select * from arbitro where nome_arbitro = "{condicao1}";')
#     print(cursor.fetchall())#fetchal trás tudo
#   elif condicao2 != '':
#     cursor.execute(f'select * from arbitro where id_arbitro = "{condicao2}";')
#     print(cursor.fetchall())
#   else:
#     cursor.execute('select * from arbitro;')
#     print(cursor.fetchall())

# #Select tabela tecnico
# def selectTecnico(cursor,condicao1,condicao2):
#   if condicao1 != '':
#     cursor.execute(f'select * from tecnico where nome_tecnico = "{condicao1}";')
#     print(cursor.fetchall())
#   elif condicao2 != '':
#     cursor.execute(f'select * from tecnico where id_tecnico = "{condicao2}";')
#     print(cursor.fetchall())
#   else:
#     cursor.execute('select * from tecnico;')
#     print(cursor.fetchall())

# # Select tabela equipe
# def selectEquipe(cursor,condicao1,condicao2,condicaoPk):
#   if condicao1 != '':
#     cursor.execute(f'select * from equipe where nome_equipe_pais = "{condicao1}";')
#     print(cursor.fetchall())
#   elif condicao2 != '':
#     cursor.execute(f'select * from equipe where id_equipe = "{condicao2}";')
#     print(cursor.fetchall())
#   elif condicaoPk != '':
#     cursor.execute(f'select * from equipe where id_tecnico = "{condicaoPk}";')
#     print(cursor.fetchall())
#   else:
#     cursor.execute('select * from equipe;')
#     print(cursor.fetchall())

# # Select tabela fase
# def selectFase(cursor,condicao1,condicao2,condicao3,condicao4,condicao5,condicao6,condicaoPk1,condicaoPk2,condicaoPk3):
#   if condicao1 != '':
#     cursor.execute(f'select * from fase where nome_fase = "{condicao1}";')
#     print(cursor.fetchall())
#   elif condicao2 != '':
#     cursor.execute(f'select * from fase where id_fase = "{condicao2}";')
#     print(cursor.fetchall())
#   elif condicao3 != '':
#     cursor.execute(f'select * from fase where tipo_fase = "{condicao3}";')
#     print(cursor.fetchall())
#   elif condicao4 != '':
#     cursor.execute(f'select * from fase where id_fase = "{condicao4}";')
#     print(cursor.fetchall())
#   elif condicao5 != '':
#     cursor.execute(f'select * from fase where tipo_fase = "{condicao5}";')
#     print(cursor.fetchall())
#   else:
#     cursor.execute('select * from fase;')
#     print(cursor.fetchall())

# # Select tabela Grupo
# def selectGrupo(cursor,condicao1,condicao2,condicao3):
#   if condicao1 != '':
#     cursor.execute(f'select * from grupo  where desc_grupo = "{condicao1}";')
#     print(cursor.fetchall())
#   elif condicao2 != '':
#     cursor.execute(f'select * from grupo where id_grupo  = "{condicao2}";')
#     print(cursor.fetchall())
#   elif condicao3 != '':
#     cursor.execute(f'select * from grupo where id_equipe = "{condicao3}";')
#     print(cursor.fetchall())
#   else:
#     cursor.execute('select * from grupo;')
#     print(cursor.fetchall())
  
# # Select tabela partidas
# def selectPartidas(cursor,condicao1,condicao2,condicao3,condicao4,condicao5,condicao6,condicaoPk1,condicaoPk2,condicaoPk3):
#   if condicao1 != '':
#     cursor.execute(f'select * from partidas where id_partida = = "{condicao1}";')
#     print(cursor.fetchall())
#   elif condicao2 != '':
#     cursor.execute(f'select * from partidas where local_partida = "{condicao2}";')
#     print(cursor.fetchall())
#   elif condicao3 != '':
#     cursor.execute(f'select * from partidas where data_partida = "{condicao3}";')
#     print(cursor.fetchall())
#   elif condicao4 != '':
#     cursor.execute(f'select * from partidas where hora_fim = "{condicao4}";')
#     print(cursor.fetchall())
#   elif condicao5 != '':
#     cursor.execute(f'select * from partidas where num_gol_equipe1 = "{condicao5}";')
#     print(cursor.fetchall())
#   elif condicao6 != '':
#     cursor.execute(f'select * from partidas where num_gol_equipe2 = "{condicao6}";')
#     print(cursor.fetchall())
#   elif condicaoPk1 != '':
#     cursor.execute(f'select * from partidas where id_equipe = "{condicaoPk1}";')
#     print(cursor.fetchall())
#   elif condicaoPk2 != '':
#     cursor.execute(f'select * from partidas where id_arbitro = "{condicaoPk2}";')
#     print(cursor.fetchall())
#   elif condicaoPk3 != '':
#     cursor.execute(f'select * from partidas where id_fase = "{condicaoPk3}";')
#     print(cursor.fetchall())
#   else:
#     cursor.execute('select * from partidas;')
#     print(cursor.fetchall())


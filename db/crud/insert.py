import datetime
#Insert
def inserir(cnx,cursor,tabela,coluna,valores):
  if valores != '':
    try:
      cursor.execute(f'insert into {tabela} ({coluna}) values "({valores})" ;')
      cnx.commit()
      print(f'{cursor.rowcount}, Linhas inseridas')
      print(cursor.fetchall())#fetchal trás tudo
    except Exception as error:
      print(f"Erro def inserir: {error}")
  else:
    print("Tabela esta vazia!")##tabela não está vazia, usar o try except igual as outras
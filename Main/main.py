import sqlite3
import tkinter as tk
import pandas as pd
from Services.alunoService import alunoService
from telas.login import login
def initDbDepto():
    conn = sqlite3.connect("..//bd//dados.db")
    disciplinas = pd.read_csv(".//data//2023.1//departamentos_2023-1.csv")
    for index, row in disciplinas.iterrows():
        print(f"""INSERT INTO Departamento (id,nome) values('{row['cod']}', '{row['nome']})'  """)
        conn.execute(f"""INSERT INTO Departamento (id,nome) values('{row['cod']}', '{row['nome']}')  """)
    conn.commit()
    conn.close()
def initDbDisciplina():
    conn = sqlite3.connect("..//bd//dados.db")
    disciplinas = pd.read_csv(".//data//2023.1//disciplinas_2023-1.csv")
    for index, row in disciplinas.iterrows():
        print(f"""INSERT INTO Disciplina (id,idDepartamento, nome) values('{row['cod']}', {row['cod_depto']},'{row['nome']}')  """)
        conn.execute(f"""INSERT INTO Disciplina (id,idDepartamento, nome) values('{row['cod']}', {row['cod_depto']},'{row['nome']}')  """)
    conn.commit()
    conn.close()
def professorStringCut(string):
    x =""
    for c in string:

        if c == '(':
            break
        x=x+c
    return x
def initDbTurmas():
    conn = sqlite3.connect("..//bd//dados.db")
    disciplinas = pd.read_csv(".//data//2023.1//turmas_2023-1.csv")
    listaProfessores = list()
    for index, row in disciplinas.iterrows():
        professorNome = professorStringCut(row['professor'])
        print(professorNome)
        i = 0
        if professorNome not in listaProfessores:
            listaProfessores.append(professorNome)
            i = len(listaProfessores)-1
            print(f"""INSERT INTO Professor (id,nome, idDepartamento) values({i}, '{professorNome}',{row['cod_depto']})  """)
            conn.execute(f"""INSERT INTO Professor (id,nome, idDepartamento) values({i}, '{professorNome}',{row['cod_depto']})  """)
        else:
            i = listaProfessores.index(professorNome)


        print(f"""INSERT INTO Turma (idDisciplina,idProfessor, nome, semestre) values('{row['cod_disciplina']}', {i} ,  '{row['turma']}', '{row['periodo']}')  """)
        conn.execute(f"""INSERT INTO Turma (idDisciplina,idProfessor, nome, semestre) values('{row['cod_disciplina']}', {i} ,  '{row['turma']}', '{row['periodo']}')  """)
    conn.commit()
    conn.close()

conn = sqlite3.connect("..//bd//dados.db")

lg = login()
lg.render()
al = alunoService()
print(al.getAlunosByName("scott").id)
print(conn.cursor().execute(f"""select * from turmaView""").fetchall()[0])
al.con.close()



if conn:
    conn.close()
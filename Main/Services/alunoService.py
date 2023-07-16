import sqlite3
from typing import List, Dict
import typing
from Services.strings import strings

class aluno:
    def __init__(self,id, nome, moderador, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.moderador = senha=="moderador"
    def __str__(self):
        return f"id {self.id} - nome {self.nome} - senha {self.senha} - moderador {self.moderador}"

class alunoService:
    def __init__(self):
        self.con = sqlite3.connect(strings().path)
        print(self.con)
        self.cur = self.con.cursor()
        pass
    def getAlunos(self) -> List[aluno]:
        con = sqlite3.connect(strings().path)
        cur = con.cursor()
        cur.execute("SELECT * FROM Aluno")
        rows = cur.fetchall()
        lista = list()
        for row in rows:
            lista.append( aluno(*row) )
        
        return lista
    def getAlunosByName(self,name) -> aluno:
        for x in self.getAlunos():
            if x.nome == name:
                return x

    def insertAluno(self, nome, senha):

        try:
            if not self.getAlunosByName(nome):
                self.con.execute("""INSERT INTO Aluno(nome,senha,moderador)
        VALUES (?,?,?)""", (nome, senha, int(senha=="moderador")) )
                self.con.commit()

        except sqlite3.Error as err:
            print(err)
    def login(self, nome, senha) -> aluno:
        lista = self.getAlunos()
        for x in lista:
            if x.nome == nome:
                if str(x.senha) == senha:
                    return x
                else:
                    return False
        self.insertAluno(nome, senha)
        return self.getAlunosByName(nome)
    def updateAluno(self, aluno):
        nome = aluno.nome
        senha = aluno.senha
        print(senha)
        moderador = int(aluno.senha == "moderador")
        id = aluno.id
        self.con.execute(f"""UPDATE Aluno SET nome = {self.sqlstring(nome)},
                                        senha = {self.sqlstring(senha)},
                                        moderador = {moderador}
                    where id = {id};""")
        self.con.commit()
    def sqlstring(self, string):
        return "'"+string+"'"
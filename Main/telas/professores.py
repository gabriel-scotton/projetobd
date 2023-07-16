import tkinter as tk
import typing
import sqlite3
from Services.alunoService import alunoService, aluno
from Services.strings import strings
from telas.denunciartela import denunciartela

class professor:
    def __init__(self, nome,id, idDepartamento):
        self.id = id
        self.nome = nome
        self.idDepartamento=idDepartamento
    def __str__(self):
        return f"{self.id}-{self.nome}-{self.idDepartamento}"

class professores:
    def __init__(self, aluno):
        self.aluno: aluno = aluno

    def criarAvaliacao(self, event):
        con = sqlite3.connect(strings().path)
        x = con.cursor().execute(f"""select * from Avaliacao""").fetchall()
        con.execute(f"""insert into Avaliacao (id, comentario, tipo, idAluno ) 
                    values({len(x)}, '{self.avaliarEntry.get()}', 1 , {self.aluno.id})""")
        con.execute(f"""insert into AvaliacaoProfessor (idAvaliacao, idProfessor ) 
                            values({len(x)}, {self.professorId})""")
        con.commit()
        self.VerAvaliacoes()
    def denunciarButtonPress(self,event):
        idAv = self.denunciarEntry.get()
        self.window.destroy()
        denunciartela(self.aluno).denunciarTela(avId=idAv)

    def VerAvaliacoes(self):
        self.window.destroy()
        self.window = tk.Tk()
        avaliacoes = con = sqlite3.connect(strings().path).cursor().execute("select * from avaliacaoProfessorView").fetchall()
        listbox = tk.Listbox(self.window, height=15, width=150)
        for a in avaliacoes:
            listbox.insert(0,f"id{a[0]}-comentario {a[1]}- prof{a[2]}, depto{a[3]}")
        listbox.pack()
        self.denunciarEntry = tk.Entry()
        self.denunciarEntry.pack()
        buttonDenunciar = tk.Button(text="denunciar")
        buttonDenunciar.pack()
        buttonDenunciar.bind("<Button-1>", self.denunciarButtonPress)
        self.window.mainloop()


    #o interpretador nao gostou de eu chamar essa funcao fora do button press
    def VerAvaliacoesButtonPress(self, event):
        self.VerAvaliacoes()

    def AvaliarButtonPress(self,event):
        self.professorId = self.entry.get()
        self.window.destroy()
        self.window = tk.Tk()
        self.avaliarEntry = tk.Entry()
        self.avaliarEntry.pack()
        buttonAvaliar=tk.Button(text="feito")
        buttonAvaliar.bind("<Button-1>", self.criarAvaliacao)
        buttonAvaliar.pack()
        self.window.mainloop()
    def render(self):
        con = sqlite3.connect(strings().path)
        turmasTupleList = con.cursor().execute(f"""select * from professorView""").fetchall()
        professores = list()
        for t in turmasTupleList:
            professores.append(professor(*t))
        self.window = tk.Tk()
        listbox = tk.Listbox(self.window, height=30, width=150)
        for i in range(len(professores)):
            listbox.insert(i,professores[i])
        listbox.pack()
        self.entry = tk.Entry()
        self.entry.pack()
        buttonAvaliar = tk.Button(text="Avaliar")
        buttonAvaliar.bind("<Button-1>",self.AvaliarButtonPress)
        buttonAvaliar.pack()
        buttonVerAvaliacoes = tk.Button(text="Ver Avaliacoes")
        buttonVerAvaliacoes.bind("<Button-1>", self.VerAvaliacoesButtonPress)
        buttonVerAvaliacoes.pack()
        self.window.mainloop()



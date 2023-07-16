import tkinter as tk
import typing
import sqlite3
from Services.alunoService import alunoService, aluno
from Services.strings import strings
from telas.denunciartela import denunciartela

class turma:
    def __init__(self, id, nome, nomeProf, nomeDisp):
        self.id = id
        self.nome = nome
        self.nomeprof = nomeProf
        self.nomeDisp = nomeDisp
    def __str__(self):
        return f"{self.id}-{self.nomeDisp}-{self.nome}-{self.nomeprof}"

class turmas:
    def __init__(self, aluno):
        self.aluno: aluno = aluno

    def criarAvaliacao(self, event):
        con = sqlite3.connect(strings().path)
        x = con.cursor().execute(f"""select * from Avaliacao""").fetchall()
        con.execute(f"""insert into Avaliacao (id, comentario, tipo, idAluno ) 
                    values({len(x)}, '{self.avaliarEntry.get()}', 0 , {self.aluno.id})""")
        con.execute(f"""insert into AvaliacaoTurma (idAvaliacao, idTurma ) 
                            values({len(x)}, {self.turmaId})""")
        con.commit()
        self.VerAvaliacoes()
    def denunciarButtonPress(self,event):
        idAv = self.denunciarEntry.get()
        self.window.destroy()
        denunciartela(self.aluno).denunciarTela(avId=idAv)

    def VerAvaliacoes(self):
        self.window.destroy()
        self.window = tk.Tk()
        avaliacoes = con = sqlite3.connect(strings().path).cursor().execute("select * from avaliacaoTurmaView").fetchall()
        listbox = tk.Listbox(self.window, height=15, width=150)
        for a in avaliacoes:
            listbox.insert(0,f"id{a[0]}-comentario {a[1]}-por{a[5]} -{a[3]} id{a[2]} prof{a[4]}")
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
        self.turmaId = self.entry.get()
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
        turmasTupleList = con.cursor().execute(f"""select * from turmaView""").fetchall()
        turmas = list()
        for t in turmasTupleList:
            turmas.append(turma(*t))
        self.window = tk.Tk()
        listbox = tk.Listbox(self.window, height=30, width=150)
        for i in range(len(turmas)):
            listbox.insert(i,turmas[i])
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



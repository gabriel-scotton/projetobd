import tkinter as tk
import typing
import sqlite3
from Services.alunoService import alunoService, aluno
from Services.strings import strings

class denunciartela:
    def __init__(self, aluno):
        self.aluno = aluno
    def denunciarButtonPress(self,event):
        con = sqlite3.connect(strings().path)
        con.execute(f"""INSERT INTO Denuncia (idAvaliacao, idAluno, comentario)
                    values ({self.avId}, {self.aluno.id}, '{self.denunciaEntry.get()}')""")
        con.commit()
        self.window.destroy()

    def denunciarTela(self, avId):
        self.avId = avId
        self.window = tk.Tk()
        self.denunciaEntry = tk.Entry()
        self.denunciaEntry.pack()
        buttonDenunciar = tk.Button(text='denuncia feita')
        buttonDenunciar.bind("<Button-1>",self.denunciarButtonPress)
        buttonDenunciar.pack()
        self.window.mainloop()
    def DeletarDenuncias(self,event):
        con = sqlite3.connect(strings().path)
        con.execute(f"""DELETE FROM Denuncia where idAvaliacao = {self.entry.get()}""")
        self.window.destroy()
        con.commit()
    def DeletarAvaliacoes(self,event):
        con = sqlite3.connect(strings().path)
        con.execute(f"""DELETE FROM Avaliacao where id = {self.entry.get()}""")
        con.commit()
        self.window.destroy()
    def renderDenuncias(self):
        con = sqlite3.connect(strings().path)
        denuncias = con.cursor().execute(f"""select * from denunciaView""").fetchall()
        self.window = tk.Tk()
        listbox = tk.Listbox(self.window, height=20, width=200)
        for d in denuncias:
            listbox.insert(0,f"comentario:{d[0]} sobre a avaliacao de id{d[1]}, comentario {d[2]}")
        listbox.pack()
        buttonDeletar= tk.Button(text="deletarAvaliacoes")
        buttonDeletar.pack()
        buttonDeletar.bind("<Button-1>", self.DeletarAvaliacoes)
        buttonIgnorar=tk.Button(text="deletarDenuncias")
        buttonIgnorar.bind("<Button-1>", self.DeletarDenuncias)
        buttonIgnorar.pack()
        self.entry = tk.Entry()
        self.entry.pack()
        self.window.mainloop()


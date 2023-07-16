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

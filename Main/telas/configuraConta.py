import tkinter as tk
import typing

from Services.alunoService import alunoService, aluno

class configuraConta:
    def __init__(self, aluno):
        self.aluno = aluno
    def buttonSaveClick(self, event):
        self.aluno.nome = self.entryNome.get()
        self.aluno.senha = self.entrySenha.get()
        al = alunoService()
        al.updateAluno(self.aluno)
        test = al.getAlunosByName(self.aluno.nome)
        print(test)

    def render(self):
        window = tk.Tk()
        labelNome = tk.Label(text="Nome")
        labelNome.pack()
        self.entryNome = tk.Entry()
        self.entryNome.insert(0,string=self.aluno.nome)
        self.entryNome.pack()

        labelSenha = tk.Label(text="Senha")
        labelSenha.pack()
        self.entrySenha = tk.Entry()
        self.entrySenha.insert(0,string=self.aluno.senha)
        buttonSave = tk.Button(text="<save>")
        buttonSave.bind("<Button-1>", self.buttonSaveClick)

        self.entrySenha.pack()
        buttonSave.pack()
        al = alunoService()
        alunolist=al.getAlunos()
        listbox = tk.Listbox(window, height=30,width= 50)
        for i in range(len(alunolist)):
            listbox.insert(i, alunolist[i])

        listbox.pack()
        window.mainloop()
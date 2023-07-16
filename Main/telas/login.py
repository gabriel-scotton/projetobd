import tkinter as tk
from Services.alunoService import alunoService, aluno
from telas.principal import principal


class login:
    def buttonLoginClick(self, event):
        alunos = alunoService()
        a = alunos.login(self.entryNome.get(),self.entrySenha.get())
        if a:
            p=principal()
            self.window.destroy()
            p.render(a)


    def render(self):
        self.window = tk.Tk()
        labelNome = tk.Label(text="Nome")
        labelNome.pack()
        self.entryNome = tk.Entry()
        self.entryNome.pack()
        self.entryNome.insert(0, "scott")
        labelSenha = tk.Label(text="Senha")
        self.entrySenha = tk.Entry()
        self.entrySenha.insert(0,"moderador")
        buttonLogin =  tk.Button(text="<login>")
        buttonLogin.bind("<Button-1>", self.buttonLoginClick)
        labelSenha.pack()
        self.entrySenha.pack()
        buttonLogin.pack()
        self.window.mainloop()




        
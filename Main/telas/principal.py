import tkinter as tk
import typing
from Services.alunoService import alunoService, aluno
from telas.configuraConta import configuraConta
from telas.professores import professor, professores
from telas.denunciartela import denunciartela
from telas.turmas import turmas
class principal:
    def buttonContaClick(self, event):
        self.window.destroy()
        config = configuraConta(self.aluno)

        config.render()
    def buttonTurmasClick(self,event):
        self.window.destroy()
        turmasTela = turmas(self.aluno)
        turmasTela.render()
    def buttonProfessoresClick(self,event):
        self.window.destroy()
        professoresTela = professores(self.aluno)
        professoresTela.render()
    def buttonDenunciasClick(self, event):
        self.window.destroy()
        denuncias= denunciartela(self.aluno)
        denuncias.renderDenuncias()

    def render(self, aluno):
        self.window = tk.Tk()
        self.aluno = aluno
        print(aluno.nome)
        buttonTurmas = tk.Button(text="turmas")
        buttonTurmas.bind("<Button-1>", self.buttonTurmasClick)
        buttonTurmas.pack()
        buttonProfessores = tk.Button(text="professores")
        buttonProfessores.bind("<Button-1>", self.buttonProfessoresClick)
        buttonProfessores.pack()
        buttonConta = tk.Button(text="conta")
        buttonConta.bind("<Button-1>", self.buttonContaClick)
        buttonConta.pack()
        print(self.aluno)
        if self.aluno.moderador:
            buttonDenuncias = tk.Button(text="denuncias")
            buttonDenuncias.bind("<Button-1>", self.buttonDenunciasClick)
            buttonDenuncias.pack()
        self.window.mainloop()
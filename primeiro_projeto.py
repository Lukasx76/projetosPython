class Aluno:
    def __init__(self, nome, idade, mencao):
        self.nome = nome
        self.idade = idade
        self.mencao = mencao

    def visualizar_mencao(self):
        return self.mencao

class Curso:
    def __init__(self, nome_curso, max_alunos):
        self.nome_curso = nome_curso
        self.max_alunos = max_alunos
        self.alunos = []

    def adiciona_aluno(self, aluno):
        if len(self.alunos) < self.max_alunos:
            self.alunos.append(aluno)
            return True
        return False

    def obter_media_mencao(self):
        valor = 0
        for aluno in self.alunos:
            valor += aluno.visualizar_mencao()

        return valor / len(self.alunos)

aluno1 = Aluno("Lucas", 19, 99)
aluno2 = Aluno("pessoa", 19, 99)
aluno3 = Aluno("pessoa2", 25, 97)

curso = Curso("Literatura", 2)

curso.adciona_aluno(aluno1)
curso.adciona_aluno(aluno2)
curso.adciona_aluno(aluno3)

print(curso.obter_media_mencao())

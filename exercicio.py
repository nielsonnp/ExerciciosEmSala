class Aluno:
    def __init__(self, nota1, nota2, nota3,media):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = media

    def __str__(self):
        return ("Nota1 = {0}, Nota2 = {1}, Nota3 = {2} Média = {3}".format(self.nota1,self.nota2,self.nota3,self.media))

    def get_nota1(self):
        return self.nota1

    def set_nota1(self, nova_nota):
        self.nota1 = nova_nota

    def get_nota2(self):
        return self.nota2

    def set_nota2(self, nova_nota):
        self.nota2 = nova_nota

    def get_nota3(self):
        return self.nota3

    def set_nota3(self, nova_nota):
        self.nota3 = nova_nota

    def set_media(self, nova_media):
        self.media = nova_media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a teceira nota: "))

media = (nota1+nota2+nota3)/3

a1 = Aluno(nota1,nota2,nota3,media)

print(a1)

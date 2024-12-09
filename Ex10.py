from Pilha import Pilha

class Navegador:
    def __init__(self):
        self.historico = Pilha()
        self.futuro = Pilha()

    def visitar(self, pagina):
        self.historico.push(pagina)
        self.futuro = Pilha()

    def voltar(self):
        if not self.historico.is_empty():
            self.futuro.push(self.historico.pop())

    def avancar(self):
        if not self.futuro.is_empty():
            self.historico.push(self.futuro.pop())

    def pagina_atual(self):
        return self.historico.peek()

navegador = Navegador()
navegador.visitar("home")
navegador.visitar("about")
navegador.visitar("contact")
navegador.voltar()
print(navegador.pagina_atual())
navegador.voltar()
print(navegador.pagina_atual())
navegador.avancar()
print(navegador.pagina_atual())

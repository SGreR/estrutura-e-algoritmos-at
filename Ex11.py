from Fila import Fila

class SistemaAtendimento:
    def __init__(self):
        self.chamados = Fila()

    def adicionar_chamado(self, chamado):
        self.chamados.enqueue(chamado)
        print(f"Chamado '{chamado}' adicionado.")

    def atender_chamado(self):
        chamado = self.chamados.dequeue()
        if chamado is not None:
            print(f"Atendendo chamado: {chamado}")
        else:
            print("Não há chamados para atender.")

    def mostrar_proximo(self):
        proximo = self.chamados.peek()
        if proximo is not None:
            print(f"Próximo chamado: {proximo}")

    def exibir_chamados(self):
        self.chamados.display()

sistema = SistemaAtendimento()
sistema.adicionar_chamado("Chamado 1")
sistema.adicionar_chamado("Chamado 2")
sistema.exibir_chamados()
sistema.mostrar_proximo()
sistema.atender_chamado()
sistema.atender_chamado()
sistema.atender_chamado()

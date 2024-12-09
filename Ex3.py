def busca_linear(lista_contatos, nome_procurado):
    for contato in lista_contatos:
        if contato["nome"] == nome_procurado:
            return contato["telefone"]
    return "Contato não encontrado."

from fabricas.db_create import Produto

class ProdutoQuery():
    def inserir_produto(self, novo_produto, sessao):
        sessao.add(novo_produto)

    def listar_produtos_id(self, id_produto, sessao):
        print (id_produto)
        produto = sessao.query(Produto).filter(Produto.id == id_produto).first()
        return produto
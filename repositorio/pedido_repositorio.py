from fabricas.db_create import Pedido
from repositorio import cliente_repositorio
from queries import pedido_query
from queries import produto_query

class PedidoRepositorio():
    def inserir_pedido(self, id_cliente, sessao, produtos):
        #Vamos buscar o cliente que possui o id_cliente que estamos buscando
        #Para isso vamos chamar o método listar_cliente_id. 
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        cliente = repositorio_cliente.listar_cliente_id(id_cliente, sessao)

        #Novo pedido criado a partir do codigo db_create.py
        novo_pedido = Pedido(cliente=cliente)

        #Cria uma query de produtos para listar a lista de produtos pelo id.
        query_produto = produto_query.ProdutoQuery()
        for i in produtos:
            produto = query_produto.listar_produtos_id(i, sessao)
            
            #Vamos adicionar o id de cada produto encontrado na lista de produtos.
            novo_pedido.produtos.append(produto)

        #Instancia do pedido query
        query_pedido = pedido_query.PedidoQuery()
        query_pedido.inserir_pedido(novo_pedido, sessao)

    def listar_pedidos(self, sessao):
        query_pedido = pedido_query.PedidoQuery()
        pedidos = query_pedido.listar_pedidos(sessao)
        return pedidos
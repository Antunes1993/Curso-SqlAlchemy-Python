from fabricas.db_create import Pedido
from sqlalchemy.orm import joinedload

class PedidoQuery():
    def inserir_pedido(self, pedido, sessao):
        sessao.add(pedido)

    def listar_pedidos(self, sessao):
        #Query na tabela de produtos e retornando todos os produtos atrelados a esse pedido
        pedidos = sessao.query(Pedido).options(joinedload(Pedido.produtos)).all()
        return pedidos 



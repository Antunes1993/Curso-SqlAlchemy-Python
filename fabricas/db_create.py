from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from fabricas import fabrica_conexao

#1. Obter conexão com db 
fabrica = fabrica_conexao.FabricaConexao()
engine = fabrica.conectar()

#2. Modo de criação das tabelas do banco de dados
Base = declarative_base()

#6. Definição da tabela auxiliar de produtos
produto_pedido = Table('produto_pedido', Base.metadata, 
                        Column('produto_id', Integer, ForeignKey('produto.id')),
                        Column('pedido_id', Integer, ForeignKey('pedido.id')))



#3. Definição da tabela cliente que será criada no modo declarativo
class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False)
    idade = Column(Integer, nullable=False)

    #Relacionamento com a tabela de pedidos
    pedidos = relationship("Pedido", back_populates="cliente", cascade="delete")


    #Determina como o cliente será impresso no script python
    def __repr__(self):
        return "Cliente %s ('%s','%s')" % (self.id, self.nome, self.idade)

#4. Definição da tabela Pedido que será criada no modo declarativo
class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))    
    cliente = relationship("Cliente", back_populates="pedidos")

    #Relação com a tabela auxiliar produto_pedido
    produtos = relationship("Produto", secondary="produto_pedido", back_populates="pedido")

    #Determina como o pedido será impresso no script python
    def __repr__(self):
        return "Pedido %s" % (self.id) 

#5. Definição da tabela produto que será criada no modo declarativo
class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(40), nullable=False)
    valor = Column(Float, nullable=False)

    #Relação com a tabela auxiliar produto_pedido
    pedido = relationship("Pedido", secondary="produto_pedido", back_populates="produtos")

    #Determina como o produto será impresso no script python
    def __repr__(self):
        return "Produto %s ('%s','%s')" % (self.id, self.descricao, self.valor)


Base.metadata.create_all(engine)

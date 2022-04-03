import MySQLdb
from fabricas import fabrica_conexao
from queries import cliente_query
from entidades import cliente
from fabricas import db_create

class ClienteRepositorio():
    
    def inserir_cliente(self, cliente, sessao):
        # Cria uma instância do ClienteQuery       
        query_cliente = cliente_query.ClienteQuery()

        #Cliente criado a partir da tabela desenhada no db_create.py
        novo_cliente = db_create.Cliente(nome=cliente.nome, idade=cliente.idade)
        
        #Inserindo o cliente no banco de dados
        query_cliente.inserir_cliente(novo_cliente, sessao)
    
    def atualizar_cliente(self, id_cliente, cliente, sessao):
        # Cria uma instância do ClienteQuery    
        query_cliente = cliente_query.ClienteQuery()

        #Atualizando os dados do cliente no banco de dados
        query_cliente.atualizar_cliente(id_cliente, cliente, sessao)

    def remover_cliente(self, id_cliente, sessao):
        # Cria uma instância do ClienteQuery    
        query_cliente = cliente_query.ClienteQuery()

        # Removendo cliente do banco de dados
        query_cliente.remover_cliente(id_cliente, sessao)

    def listar_clientes(self, sessao):
        # Cria uma instância do ClienteQuery    
        query_cliente = cliente_query.ClienteQuery()
        
        # Listando clientes
        clientes = query_cliente.listar_clientes(sessao)
        return clientes

    def listar_cliente_id(self, id_cliente, sessao):
        # Cria uma instância do ClienteQuery    
        query_cliente = cliente_query.ClienteQuery()

        # Listar clientes pelo Id
        cliente = query_cliente.listar_clientes_id(id_cliente, sessao)
        return cliente

    def listar_cliente_nome(self, nome_cliente, sessao):
        # Cria uma instância do ClienteQuery    
        query_cliente = cliente_query.ClienteQuery()

        # Listar clientes pelo Id
        cliente = query_cliente.listar_clientes_nome(nome_cliente, sessao)
        return cliente

    def listar_cliente_nome_ordenado_idade(self, nome_cliente, sessao):
        # Cria uma instância do ClienteQuery    
        query_cliente = cliente_query.ClienteQuery()

        # Listar clientes pelo Id
        clientes = query_cliente.listar_clientes_nome_ordenado_idade(nome_cliente, sessao)
        return clientes
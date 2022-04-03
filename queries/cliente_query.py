from fabricas.db_create import Cliente

class ClienteQuery():
    def inserir_cliente(self, cliente, sessao):
        sessao.add(cliente)

    def atualizar_cliente(self, id_cliente, cliente, sessao):
        #Buscar o cliente na nossa query de clientes e atualiza informações
        sessao.query(Cliente).filter(Cliente.id == id_cliente).update({'nome': cliente.nome, 'idade': cliente.idade})

    def remover_cliente(self, id_cliente, sessao):
        cliente = sessao.query(Cliente).filter(Cliente.id==id_cliente).first()
        sessao.delete(cliente)

    def listar_clientes(self, sessao):
        clientes = sessao.query(Cliente).all()
        return clientes

    def listar_clientes_id(self, id_cliente, sessao):
        print(id_cliente)
        cliente = sessao.query(Cliente).filter(Cliente.id == id_cliente).first()
        return cliente

    def listar_clientes_nome(self, nome_cliente, sessao):        
        cliente = sessao.query(Cliente).filter(Cliente.nome == nome_cliente).all()
        return cliente

    def listar_clientes_nome_ordenado_idade(self, nome_cliente, sessao):
        cliente = sessao.query(Cliente).filter(Cliente.nome == nome_cliente).order_by(Cliente.idade).all()
        return cliente
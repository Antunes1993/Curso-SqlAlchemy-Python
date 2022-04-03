import MySQLdb 
from entidades import cliente, produto
from repositorio import cliente_repositorio 
from repositorio import pedido_repositorio
from repositorio import produto_repositorio
from fabricas import fabrica_conexao

#Criação da fabrica de conexões para, em seguida, criar as sessões.
fabrica = fabrica_conexao.FabricaConexao()
sessao = fabrica.criar_sessao()

loop = True 
while loop:
    print(30 * "-", "MENU", 30 * "-")
    print("1. Cliente")
    print("2. Produtos")
    print("3. Pedidos")
    print("0. Sair")
    print(67 * "-")

    menu_principal = int(input("Digite a opção desejada:"))
    ################### MENU DE CLIENTES ######################
    if menu_principal == 1:
        print (30 * "-", "MENU", 30 * "-")
        print("1. Inserir Cliente")
        print("2. Atualizar Cliente")
        print("3. Remover Cliente")
        print("4. Listar Clientes")
        print("5. Listar Cliente por id")
        print("6. Listar Cliente por nome")
        print("7. Listar Cliente por nome ordenado")
        print("0. Sair")
        print(67 * "-")
  
        menu_cliente = int(input("Digite a opção desejada: "))

        if menu_cliente == 1:
           
            try:
                nome_cliente = input("nome cliente:")
                idade_cliente = int(input("idade do cliente:"))
                novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
                
                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.inserir_cliente(novo_cliente, sessao)
                sessao.commit()
            except:
                sessao.rollback()
            finally:
                sessao.close()

        elif menu_cliente == 2:
            
            try:
                id_cliente = int(input("ID do cliente a ser atualizado: "))
                nome_cliente = input("nome cliente:")
                idade_cliente = int(input("idade do cliente:"))
                novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)

                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.atualizar_cliente(id_cliente, novo_cliente, sessao)
                sessao.commit()
            except: 
                sessao.rollback()
            finally:
                sessao.close()

        elif menu_cliente == 3: 
            try:
                id_cliente = int(input("ID do cliente a ser atualizado: "))

                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.remover_cliente(id_cliente, sessao)
                sessao.commit()
            except: 
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_cliente == 4:
            try:
                repositorio = cliente_repositorio.ClienteRepositorio()
                clientes = repositorio.listar_clientes(sessao)
                for i in clientes:
                    print(i)
            except: 
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_cliente == 5:
            try:
                repositorio = cliente_repositorio.ClienteRepositorio()
                id_cliente = int(input("Id do cliente a ser exibido: "))
                cliente = repositorio.listar_cliente_id(id_cliente, sessao)
                print(cliente)
            except: 
                sessao.rollback()
                raise
            finally:
                sessao.close()
        
        elif menu_cliente == 6:
            try:
                repositorio = cliente_repositorio.ClienteRepositorio()
                nome_cliente = input("Nome do cliente a ser atualizado: ")
                cliente = repositorio.listar_cliente_nome(nome_cliente, sessao)
                for i in cliente:
                    print(i)
            except: 
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_cliente == 7:
            try:
                repositorio = cliente_repositorio.ClienteRepositorio()
                nome_cliente = input("Nome do cliente a ser atualizado: ")
                cliente = repositorio.listar_cliente_nome_ordenado_idade(nome_cliente, sessao)
                for i in cliente:
                    print(i)
            except: 
                sessao.rollback()
                raise
            finally:
                sessao.close() 


    ################### MENU DE PRODUTOS ######################
    elif menu_principal == 2:
        print (30 * "-", "MENU", 30 * "-")
        print("1. Inserir Produto")
        print("2. Listar Produto por id")
        print("0. Sair")
        print(67 * "-")

        menu_produto = int(input("Digite a opção desejada: "))

        if menu_produto == 1:
            try:
                #Dados do novo produto
                descricao_produto = input("Digite a descrição do produto: ")
                valor_produto = float(input("Digite o valor do produto: "))

                #Criação do novo produto
                novo_produto = produto.Produto(descricao_produto, valor_produto)

                #Criação do repositório de produtos
                repositorio_produto = produto_repositorio.ProdutoRepositorio()
                repositorio_produto.inserir_produto(novo_produto, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_produto == 2:
            try:
                repositorio = produto_repositorio.ProdutoRepositorio()
                id_produto = int(input("id do produto a ser buscado: "))
                produto = repositorio.listar_produto_id(id_produto, sessao)
                print(produto)
            except: 
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_produto == 0:
            continue 
        else:
            print ("Operação nao permitida.")

        

    ################### MENU DE PEDIDOS ######################
    elif menu_principal == 3: 
        print (30 * "-", "MENU", 30 * "-")
        print("1. Inserir Pedido")
        print("2. Listar Pedidos")
        print("0. Sair")
        print(67 * "-")

        menu_pedido = int(input("Digite a opção desejada: "))

        if menu_pedido == 1:
            try:
                loop_pedido = True
                lista_produtos = [] 
                while loop_pedido:
                    print ("1. Inserir produto")
                    print ("0. Voltar")
                    menu_pedido_produto = int(input("Digite a opção desejada:"))

                    if menu_pedido_produto == 1:
                        id_produto_pedido = int(input("Digite o ID do produto deste pedido: "))
                        lista_produtos.append(id_produto_pedido)

                    elif menu_pedido_produto == 0:
                        break 
                    else: 
                        print("Operação inválida. Digite 0 ou 1.")

                id_cliente = int(input("Digite o ID do cliente a ser relacionado com o novo pedido."))
                repositorio_pedido = pedido_repositorio.PedidoRepositorio()
                repositorio_pedido.inserir_pedido(id_cliente, sessao, lista_produtos)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()
        
        elif menu_pedido == 2:
            try:
                repositorio = pedido_repositorio.PedidoRepositorio()
                pedidos = repositorio.listar_pedidos(sessao)
                for i in pedidos:
                    print(i.produtos)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_pedido == 0:
            continue
        else:
            print("Opção inválida.")


    elif menu_principal == 0:
        print("Até mais!")
        break 
    else:
        print("Opção inválida.")
import MySQLdb, configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class FabricaConexao():
    def conectar(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        '''
        ### Conexão usando DB API ###
        db = MySQLdb.connect(user=config['DATABASE']['user'],
                             passwd=config['DATABASE']['passwd'],
                             db=config['DATABASE']['db'],
                             port=int(config['DATABASE']['port']),
                             autocommit=config['DATABASE']['autocommit'])
        '''
        ### Conexão com SQL Alchemy ###
        user=config['DATABASE']['user']
        passwd=config['DATABASE']['passwd']
        db=config['DATABASE']['db']
        host = config['DATABASE']['host']
        port=int(config['DATABASE']['port'])

        #Criação do create engine
        engine = create_engine(f'mysql://{user}:{passwd}@{host}:{port}/{db}')

        #return db
        return engine

    def criar_sessao(self):
        conexao = self.conectar()
        
        #Cria uma sessão em branco do Sql Alchemy
        Session = sessionmaker()

        #Confiuramos a conexão para receber a conexão
        Session.configure(bind=conexao)
        session = Session()

        return session
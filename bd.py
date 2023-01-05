import itertools
from parser import Endereco


def contatos_duplicados(cliente: int, limite: int, conexao, escolha: callable) -> list:
    '''
    Retorna os id´s dos contatos de endereço duplicados.
    ----------------------------------------------------------
    :cliente - id do cliente dono dos endereços
    :limite - número máximo de endereços a serem verificados
    :conexao - conexão com o banco de dados
    :escolha - Função para escolher entre dois endereços iguais
    ----------------------------------------------------------
    '''
    query = """
        SELECT
            c.conteudo, c.id
        FROM 
            contato c 
        WHERE 
            c.cliente = {} AND c.classtype = 'Endereço'
        LIMIT {}
    """.format(cliente, limite)
    return [
        escolha(a, b).id for a, b in itertools.combinations([
            Endereco(*db) for db in conexao.execute(query).fetchall()],
            2
        ) if a == b
    ]

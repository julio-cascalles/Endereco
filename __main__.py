import os
from bd import contatos_duplicados
from parser import Endereco


def teste_compara_enderecos():
    end1 = Endereco(
        'Av. José Cândido Simões, 666 - bl 25 CEP: 12345-678 ap.14'
    )
    end2 = Endereco(
        'Avenida Zé Candido Simoes 666 apartamento 14 bloco 25'
    )
    assert end1 == end2

def teste_duplicados_no_banco(params: dict):
    esperado = params.pop('resultado_esperado')
    PRIMEIRO = lambda a, b: a
    if 'password' in params:
        import mysql.connector
        db = mysql.connector.connect(**params)
    else:
        import sqlite3
        arquivo = '/users/{user}/endereco/{database}.db'.format(**params)
        db = sqlite3.connect(arquivo, check_same_thread=False)
    assert contatos_duplicados(2, 10, db.cursor(), PRIMEIRO) == esperado


teste_compara_enderecos()

teste_duplicados_no_banco({
    'database': 'legado', 'user': 'julio', 
    # 'password': os.environ.get('MYSQL_PASSWORD'),
    'resultado_esperado': [10, 12, 14, 16, 18]
})
print('*** Teste OK ***')
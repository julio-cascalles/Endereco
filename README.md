Imagine que existem MILHARES de endereços duplicados no banco de dados.
* Não é possível deixar o campo como UNIQUE porque o mesmo endereço pode ter diversos tipos de formatos;
* Também não é viável acessar API´s de mapas (ou dos Correios) para converter os endereços em coordenadas (ou CEP);
* Regras:
	- Remover abreviações do logradouro e complemento;
	- Usar comparação aproximada dos textos;
	- Considerar palavras fora de ordem;
	- Ignorar acentos.

> Acompanha um `banco de dados de exemplo` para usar com a função **_contatos_duplicados_**

# ANOTAÇÕES DE FUNDAMENTOS DA PROGRAMAÇÃO

## Tipos de dados em python
1. string
2. number int
3. number float
4. boolean

## Operadores matemáticos - básicos
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão

## Operadores lógicos
and -> e -> Se duas condições forem verdadeira, o resultado é verdadeiro.
or -> ou -> Se pelo menos uma condição for verdadeira, o resultado é verdadeiro.
not -> Ele altera o valor booleano da condição.

## Métodos em python
1. print() -> Exibe informações no terminal.
2. input() -> Capturar uma informação no terminal.
3. lower() -> Converte toda a string em minúscula.
4. upper() -> Converte toda a string em maiúscula.
5. isdigit() -> Verifica se o valor contém número.

## Format em python

# Estrutura condicional
``if (se)`` -> Verifica se uma condição é true(verdadeira).Se for, ele executa o código.
``elif (senão se)`` -> é usado para testar várias condições. Ele só executa se todas as condições anteriores forem falsas.
``else (senão)`` -> Executa o código se a condição if for false(falsa).

# Laços de repetição
É um recurso de programação que permite executar um conjunto de comando várias vezes. Também são chamados de Loop, Laços de repetição ou iteração.
`FOR` -> Utilizamos quando sabemos quantas vezes queremos repetir algo.
Sintax:
for variavel in range(inicio,fim):
    comandos
[range()] -> Método que aceita geração de números.
[inicio] -> É inclusivo. É o primeiro número a ser usado.
[fim] -> É exclusivo. O número utilizado é o anterior a esse.

## Escopo das Variáveis
`Escopo Local` -> A variável ela só é acessada dentro da estrutura que ela foi criada.
`Escopo Global` -> A variável pode ser acessada por todo mundo.

## Variações das variáveis
Variável em memória -> É declarada quando você não pretende utilizar essa variável em outros cenários.
Variável contadora -> É utilizada para uma lógica onde a repetição irá ser alterada.

`WHILE` -> É utilizado quando não sabemos quantas vezes o programa vai repetir. Ele repete enquanto uma condição for verdadeira.
Sintaxe:
while condicao:
    comandos

## Conversão de tipos em python
1. int() -> A gente vai incluir qual variável/dado que queremos converter para número inteiro.
2. float() -> A gente vai incluir qual variável/dado que queremos converter para número decimal.
3. str() -> A gente vai incluir qual variável/dado que queremos converter para texto.

## Boas Práticas
1. Qualquer variável em python utiliza o padrão de case snake_case ou recentemente o cammelCase.
2. Se você observar alguma estrutura tipo nome(), 90% de chance de ser uma função.
3. Python não tem constante, porém utilizamos o padrão case
UPPERCASE,para simular que aquela variável não pode ser alterada.

## Funções em Python
`def` -> Define que uma função será declarada;
`propriedade` -> Variável em memória que irá receber um argumento.
`argumento` -> [Valor] que irá preencher o espaço da propriedade.

## Estruturas de Dados
`list ou lista` -> Armazera valores avulsos e podem ser heterogênea ou homogênea. Ou seja, pode guardar valores de um mesmo tipo ou de diferentes tipos.
Ex: list = [] // Lista vazia
list = ["William", 25, 1.82]

`dict ou dicionário` -> Armazena conjuntos de valores (chave:valor). As chaves e valores podem ser heterogênea ou homogênea.
1. Para obter o valor de um conjunto em dict, você acessa pela chave.
Ex: dados_usuario = {} // Dicionário Vazio
dados_usuario = {"nome": "William", "cpf": 111456985-98, "idade": 25}
dados_usuario["nome"] => Devolve o valor, que é "William".


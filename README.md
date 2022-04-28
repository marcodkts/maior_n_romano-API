# O Problema
Dada uma palavra contínua, Joaquim precisa localizar o maior número romano dentro da palavra. Os
algarismos romanos são representados por letras maiúsculas, num total de 7 numerações: I (1), V (5), X
(10), L (50), C (100), D (500), M (1000).
Por exemplo, na palavra "AXXBLX", nós encontramos dois pares de números romanos XX (20)
e LX (60). Logo, o maior número romano presente na sequência é LX (60)

# Solução
Utilizando o padrão REST, foi construída uma API utilizando o Flask Framework para criar um método POST
em que o usuário envie o texto a ser analisado por meio de um dicionário JSON no devido padrão da API.
# Desafio
Durante o desenvolvimento um dos desafios encontrados foi entender a lógica por trás da interação entre
os algarismos romanos para que a mesma fosse reproduzida dentro de código. Tendo em vista que não se
tratava apenas de uma simples calculadora, mas também que o código deveria separar e comparar os valores
que estavam separados por caracteres que não fazem parte dos algarismos romanos.

# O Projeto
## Instalação
Após o download do projeto, certifique-se de que possui as dependências do projeto devidamente instaladas.
```
$ pip install -r requirements.txt
```
## Atenção
Caso sua porta 8080 já esteja sendo utilizada por alguma outra aplicação, fique a vontade para alterar a 
porta dentro do projeto por uma que esteja livre.
## Execução
Após as devidas preparações o projeto está pronto para ser executado.
```
$ python3 app.py
```
## Realizando Requisições
Utilizando o devido método da API, faça sua requisição passando devidamente o dicionário JSON com forme o padrão.
Para maiores praticidades, recomendo a utilização do Postman para a comunicação com a API.

URL: http://localhost:8080/search

Method: POST

INPUT:
```
{ "text": "AXXBLX" }
```
OUTPUT:
Content-Type: application/json
```
{
"number": "LX",
"value": 60
}
```

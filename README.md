# Apresentação do produto

[![Vídeo da apresentação](https://i.imgur.com/o3Ygef7.png)](https://youtu.be/ix3fNvBvvO8)

# Backend do projeto de Esteira de análise

Nesse repositório está a API e a IA.

## Ferramentas utilizadas

* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [PostgreSQL](https://www.postgresql.org/)

## Como executar

### Utilizando docker-compose

Uma forma fácil de utilizar o projeto é utilizando [docker-compose](https://docs.docker.com/compose/install/).
Para isso apenas use o comando abaixo

```bash
 docker-compose up --build
```

### Utilizando make

Para rodar localmente você só precisa ter o make, o docker e o docker-compose
instalados. A aplicação será executada dentro de um ambiente virtualizado.

Na primeira vez que for executar, é necessário rodar o seguinte comando:

```bash
 make network
```

Com isso, já pode seguir para os demais passos.

* Rodando a aplicação

```bash
 make run
```

* Parando a aplicação

```bash
 make stop
```

## Rodando em sua máquina local

Após seguir os comandos anteriores, a API estará rodando em sua máquina na porta 5000, desse modo apenas abra [http://localhost:5000](http://localhost:5000)
para poder visualizá-la em seu navegador padrão. A IA não precisa ser executada, ela está dentro da API.

## Rodando os testes

Os testes também serão executados com a ajuda do Makefile. Para isso, apenas use o comandos abaixo:

* Execute o comando

```bash
make test
```

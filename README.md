`<a name="readme-top"></a>`

# REST API Financeira

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Django&message=framework&color=green&style=for-the-badge&logo=Django"/>
  <img src="http://img.shields.io/static/v1?label=Python&message=3.10.2&color=green&style=for-the-badge&logo=Python"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
  <img src="http://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/>

| :placard: Vitrine.Dev |                                  |
| --------------------- | -------------------------------- |
| ✨ Nome               | **REST-API Financeira**    |
| 🏷 Tecnologias        | Django Rest Framework/Django-JWT |
| 🚀 Url                |                                  |

### Tópicos

🔹 [Descrição do projeto](#descrição-do-projeto)

🔹 [Acesso](#acesso)

🔹 [Funcionalidades](#funcionalidades)

🔹 [Pré-Requisitos e como Rodar o Servidor](#pré-requisitos)

🔹 [Tecnologias](#tecnologias)

🔹 [Autor](#autor)

## Descrição do projeto

<p align="justify">
  API REST desenvolvida para fornecer a configuração de back-end para o aplicativo de controle de finanças de pessoais Finanças WebFinance.<br />
  API desenvolvida em Python com o framework Django Rest, e banco de dados SQLITE3. 
</p>

### API REST

  Os endpoints da API REST estão descritos abaixo.

#### Listar todas as receitas cadastradas do usuario

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /receitas

#### Listar todas as receitas do usuário com uma descrição específica

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /receitas?descricao={descricao}

#### Listar todas as receitas do usuário de um mês específico

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /receitas/{ano}/{mes}

#### Buscar informações detalhadas de uma receita por seu id

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /receitas/{id}

#### Cadastrar nova receita

&nbsp;&nbsp;&nbsp;&nbsp;`POST` /receitas

#### Editar receita pelo id

&nbsp;&nbsp;&nbsp;&nbsp;`PUT` /receitas/{id}

#### Excluir receita pelo id

&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /receitas/{id}

#### Listar todas as despesas cadastradas do usuario

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /despesas

#### Listar todas as despesas do usuário com uma descrição específica

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /despesas?descricao={descricao}

#### Listar todas as despesas do usuário de um mês específico

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /despesas/{ano}/{mes}

#### Buscar informações detalhadas de uma despesa por seu id

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /despesas/{id}

#### Cadastrar nova despesa

&nbsp;&nbsp;&nbsp;&nbsp;`POST` /despesas

#### Editar despesa pelo id

&nbsp;&nbsp;&nbsp;&nbsp;`PUT` /despesas/{id}

#### Excluir despesa pelo id

&nbsp;&nbsp;&nbsp;&nbsp;`DELETE` /despesas/{id}

#### Exibir um resumo das despesas e receitas do mês

&nbsp;&nbsp;&nbsp;&nbsp;`GET` /resumo/{ano}/{mes}

<p align="right">(<a href="#readme-top">voltar para o início</a>)</p>

## Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

#### Tecnologias

- Django / Django Rest- Framework

#### Persistência e Deploy

- Ferramentas
- [Postman](https://www.postman.com/) - Testes de API
- [VSCode](https://code.visualstudio.com/) - Editores de código

<p align="right">(<a href="#readme-top">voltar para o início</a>)</p>

## Licença

Este projeto esta sob a licença [MIT](./LICENSE). Consulte o arquivo LICENSE.md para mais informações.

<p align="right">(<a href="#readme-top">voltar para o início</a>)</p>

## Autor

`<b>`Guilherme Castilho feitosa `</b>`🚀`<br />`
 `<img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/70145464?v=4" width="100px;" alt=""/><br />`
Projeto desenvolvido por Thomaz Machado. Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Thomaz-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/thomazcm/)](https://www.linkedin.com/in/thomazcm/)
[![Gmail Badge](https://img.shields.io/badge/-thomazcm@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:thomazcm@gmail.com)](mailto:thomazcm@gmail.com)

<p align="right">(<a href="#readme-top">voltar para o início</a>)</p>

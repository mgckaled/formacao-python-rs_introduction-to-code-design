<!-- markdownlint-disable MD033 -->

# Formação Python Rocketseat - Bloco 4: Introdução ao Design de Código

<div align="center">
  <img alt="Made by mgckaled" src="https://img.shields.io/badge/made%20by-mgckaled-darkblue">
  <img alt="GitHub Repo Size" src="https://img.shields.io/github/repo-size/mgckaled/python-rs_introduction-to-code-design">
  <img alt="pylint badge" src="https://img.shields.io/badge/linting-pylint-yellowgreen">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</div>

## Conteúdo

Este repositório reuni o conteúdo dos módulos 6 e 7 da formação Python 2023-2024 da RocketSeat Education.

**Anotações:**

- [Módulo 6](./.github/docs/m6-notes.md)
- [Módulo 7](./.github/docs/m7-notes.md)
- [Questionários Avaliativos](./.github/docs/evaluative_questionnaires.md)

### Módulo 6 - Introdução ao Design de Código

Estudamos e aplicamos inicialmente alguns conceitos básicos sobre design de código e arquitetura de software visando uma construção de projeto simples, facilmente escalavel e de facil manutenção. Explorou-se os conceitos de separação de responsabilidades, tratamento de lógicas complexas, utilização de bibliotecas terceiras, testes unitários, dependências e tratamento de erros. O objetivo final é demonstrar como o uso de boas práticas de código podem gerar um projeto sustentavel.

### Módulo 7 - Conceitos SOLID

Neste módulo foi abordado um aprofundamento nos princípios propostos contidos na palavra SOLID. Demonstrou-se em código todos os casos necessários e apresentou-se a importância desses conceitos para desenvolvedores Python.

## Tecnologias

### Linguagem de Programação

- [`python`](https://www.python.org/) (v3.12.3)

### Gerenciadores de Ambiente Virtual

- [`pyenv`](https://github.com/pyenv/pyenv)
- [`pipenv`](https://pipenv.pypa.io/en/latest/)

### Bibliotecas Instaladas (Packages)

- [`pylint`](https://pylint.pycqa.org/en/latest/index.html)
- [`pre-commit`](https://pre-commit.com/)
- [`flask`](https://flask.palletsprojects.com/en/3.0.x/)
- [`pytest`](https://docs.pytest.org/en/8.2.x/)
- [`numpy`](https://numpy.org/)

## Como clonar o projeto?

1. Certifique-se de que está usando o `pyenv` e o `pipenv` para gerenciar as dependências do projeto. Veja como instalar e configurar clicando nos respectivos links do tópico [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual).

2. Faça o clone pelo Github:

    ```shell
    git clone https://github.com/mgckaled/python-rs_introduction-to-code-design.git
    ```

3. Acesse o diretório:

    ```shell
    cd python-rs_introduction-to-code-design
    ```

4. Ative o ambiente virtual pelo terminal

    ```shell
    pipenv shell
    ```

5. Instale as dependências. (Certifique-se de estar utilzando a versão exata do python - 3.12.3)

    ```shell
    pipenv install
    ```

    ou, como um recurso de degurança,  dependências exatas do `requirements.txt`:

    ```shell
    pipenv install -r requirements.txt
    ```

6. Caso queira, ative o pylint dentro do Git com as configurações já definidas do `.pre-commit-config`:

    ```shell
    pre-commit install
    ```

## Licença

Distribuído sob a licença *MIT*. Veja [LICENSE](LICENSE) para mais informações.

---

<h5 align="center">
  2024 - <a href="https://github.com/mgckaled/">Marcel Kaled</a>
</h5>

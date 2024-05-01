# S - Single Responsability Principle

> [voltar](./m7-notes.md) para página aterior

## Definição

O Princípio da Responsabilidade Única (*Single Responsibility Principle*) é um conceito de design de software que afirma que uma classe deve ter apenas uma razão para mudar. Em outras palavras, cada classe deve ter uma única responsabilidade no sistema, e essa responsabilidade deve ser completamente encapsulada pela classe. Isso promove um código mais coeso, fácil de entender e de dar manutenção.

## Exemplos de Uso

1. **Gestão de Usuários:**
   - Uma classe `User` pode ser responsável apenas por representar um usuário no sistema, armazenando suas informações básicas e métodos relacionados à autenticação, por exemplo.
   - Uma classe `UserManager` pode ser criada para lidar com operações de criação, atualização, exclusão e pesquisa de usuários no banco de dados.

2. **Manipulação de Arquivos:**
   - Uma classe `FileManager` pode ser responsável por operações de leitura e escrita de arquivos no sistema de arquivos.
   - Uma classe `FileParser` pode ser criada para analisar e processar o conteúdo de arquivos específicos.

3. **Conexão com Banco de Dados:**
   - Uma classe `DatabaseConnector` pode ser responsável apenas por estabelecer e gerenciar a conexão com o banco de dados.
   - Uma classe `DataAccessObject` (DAO) pode ser responsável por executar operações de CRUD (Create, Read, Update, Delete) no banco de dados para uma entidade específica.

4. **Renderização de Páginas Web:**
   - Uma classe `HTMLRenderer` pode ser responsável por gerar HTML dinamicamente com base em dados fornecidos.
   - Uma classe `TemplateManager` pode ser usada para gerenciar modelos de página e sua renderização.

5. **Manipulação de Autenticação:**
   - Uma classe `Authenticator` pode ser responsável por verificar credenciais de usuário e gerar tokens de autenticação.
   - Uma classe `AuthorizationManager` pode ser responsável por verificar as permissões de acesso do usuário em determinados recursos.

6. **Processamento de Pagamentos:**
   - Uma classe `PaymentProcessor` pode ser responsável por enviar solicitações de pagamento para um serviço de gateway de pagamento e lidar com as respostas.
   - Uma classe `InvoiceGenerator` pode ser usada para gerar faturas com base em pedidos de compra.

## Exemplo em Python

```python
class Process:
    def handle(self, username: str, password: str) -> None:
        if isinstance(username, str) and isinstance(password, str):
            self.__verify_input_data(username, password)
            self.__verify_input_in_database(username)
            self.__insert_new_user(username, password)

        else:
            self.__raise_error('Dados Inválidos')

    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)

    def __verify_input_in_database(self, username: str) -> None:
        print('Acessando o banco de dados ...')
        print('Verificando a existência do usuário ...')

    def __insert_new_user(self, username: str, password: str) -> None:
        print('Cadastro de usuarios realizado com sucesso ...')

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)
```

Este código demonstra uma classe `Process` que implementa o Princípio da Responsabilidade Única ao separar claramente diferentes responsabilidades em métodos distintos.

1. **Classe `Process`:**
   - Esta é a classe principal que contém o método `handle`.
   - O método `handle` recebe dois parâmetros: `username` e `password`. Ele verifica se ambos são do tipo `str` e, em seguida, chama métodos internos para manipulação dos dados.

2. **Método `handle`:**
   - Responsável por orquestrar o processamento dos dados de entrada.
   - Verifica se os dados de entrada são do tipo `str` usando `isinstance`.
   - Chama métodos privados para verificar os dados, verificar a existência do usuário no banco de dados e inserir um novo usuário.

3. **Métodos privados:**
   - São métodos prefixados com dois sublinhados (`__`), indicando que são métodos privados e não devem ser acessados diretamente fora da classe.
   - `__verify_input_data`: Verifica se `username` e `password` são do tipo `str`. Retorna `True` se ambos são do tipo `str`.
   - `__verify_input_in_database`: Simula o acesso ao banco de dados para verificar a existência do usuário com base no `username` fornecido.
   - `__insert_new_user`: Simula a inserção de um novo usuário no banco de dados com o `username` e `password` fornecidos.
   - `__raise_error`: Levanta uma exceção com a mensagem fornecida se os dados de entrada não forem do tipo `str`.

4. **Simulação de operações:**
   - O método `__verify_input_in_database` e `__insert_new_user` imprimem mensagens simulando ações, como acessar o banco de dados e cadastrar um usuário. Isso é apenas para demonstrar as operações que seriam realizadas nessas funções em um sistema real.

Com essa estrutura, cada método tem uma única responsabilidade bem definida: verificar os dados de entrada, verificar a existência do usuário no banco de dados e inserir um novo usuário. Isso torna o código mais legível, modular e fácil de manter, seguindo o princípio da responsabilidade única.

> [retornar](#s---single-responsability-principle) para o topo da página
>
> [voltar](./m7-notes.md) a página aterior

# D - Dependency Inversion Principle

> [voltar](./m7-notes.md) para página aterior

## Definição

O Princípio da Inversão de Dependência (*Dependency Inversion Principle*) é um princípio de design de software que estabelece que módulos de alto nível não devem depender de módulos de baixo nível. Em vez disso, ambos devem depender de abstrações. Além disso, abstrações não devem depender de detalhes, mas detalhes devem depender de abstrações. Em resumo, o princípio sugere que a dependência entre classes deve ser invertida, de modo que as classes de alto nível dependam de interfaces abstratas, e não de implementações concretas de classes de baixo nível. Isso promove a flexibilidade, extensibilidade e facilita a manutenção do código.

## Exemplos de Uso

1. **Injeção de Dependência:**
   - Ao usar injeção de dependência em um projeto, as classes de alto nível dependem de interfaces abstratas em vez de classes concretas.
   - Isso permite trocar facilmente as implementações concretas das dependências sem modificar o código das classes de alto nível.
   - Por exemplo, em vez de instanciar diretamente uma classe de banco de dados em uma classe de serviço, você pode injetar uma interface de repositório e usar qualquer implementação de repositório que desejar.

2. **Frameworks de Inversão de Controle (IoC):**
   - Frameworks de IoC, como Spring Framework para Java ou AngularJS para JavaScript, facilitam a aplicação do Princípio da Inversão de Dependência.
   - Esses frameworks gerenciam as dependências e injetam as implementações corretas nas classes que precisam delas, seguindo configurações e padrões definidos pelo desenvolvedor.

3. **Padrão Strategy:**
   - O padrão Strategy envolve a definição de uma família de algoritmos, encapsulando cada um deles em uma classe separada e tornando-os intercambiáveis.
   - As classes de alto nível dependem de uma interface comum para os algoritmos, em vez de implementações concretas.
   - Isso permite que as classes de alto nível escolham dinamicamente o algoritmo a ser usado em tempo de execução, seguindo o Princípio da Inversão de Dependência.

4. **Testes Unitários:**
   - Ao escrever testes unitários, é comum usar stubs ou mocks para simular o comportamento de dependências externas.
   - Os testes unitários dependem de interfaces abstratas para as dependências em vez de classes concretas, permitindo substituir facilmente as dependências por mocks ou stubs durante os testes.

5. **Implementação de Plugins:**
   - Ao desenvolver sistemas que suportam plugins ou extensões, é importante seguir o Princípio da Inversão de Dependência.
   - As classes principais do sistema dependem de interfaces que definem os pontos de extensão, permitindo que os plugins forneçam implementações para essas interfaces sem modificar o código principal.

## Exemplo em Python

Abaixo, um sistema simples de gerenciamento de usuários, onde temos uma classe `UserService` que depende de uma interface `UserRepository`. Essa interface é implementada por diferentes repositórios concretos que interagem com diferentes tipos de armazenamento de dados, como banco de dados SQL e um serviço de API REST.

`user_repository.py`:

  ```python
  from abc import ABC, abstractmethod
  from typing import List

  class UserRepository(ABC):
      @abstractmethod
      def get_all_users(self) -> List[str]:
          pass

      @abstractmethod
      def add_user(self, user: str) -> None:
          pass

  class SqlUserRepository(UserRepository):
      def get_all_users(self) -> List[str]:
          # Lógica para recuperar usuários do banco de dados SQL
          return ['User1', 'User2', 'User3']

      def add_user(self, user: str) -> None:
          # Lógica para adicionar um usuário ao banco de dados SQL
          print(f'User {user} added to SQL database.')

  class ApiUserRepository(UserRepository):
      def get_all_users(self) -> List[str]:
          # Lógica para recuperar usuários de uma API REST
          return ['User4', 'User5', 'User6']

      def add_user(self, user: str) -> None:
          # Lógica para adicionar um usuário através de uma API REST
          print(f'User {user} added via API.')
  ```

`user_service.py`:

  ```python
  from user_repository import UserRepository
  from typing import List

  class UserService:
      def __init__(self, user_repository: UserRepository):
          self.user_repository = user_repository

      def get_all_users(self) -> List[str]:
          return self.user_repository.get_all_users()

      def add_user(self, user: str) -> None:
          self.user_repository.add_user(user)
  ```

`main.py`:

  ```python
  from user_repository import SqlUserRepository, ApiUserRepository
  from user_service import UserService

  # Utilizando o UserRepository SQL
  sql_repository = SqlUserRepository()
  user_service = UserService(sql_repository)
  users = user_service.get_all_users()
  print("Users from SQL repository:", users)

  # Utilizando o UserRepository da API
  api_repository = ApiUserRepository()
  user_service = UserService(api_repository)
  user_service.add_user("NewUser")
  ```

- **user_repository.py**: Este arquivo define a interface `UserRepository` como uma classe abstrata que contém os métodos `get_all_users()` e `add_user()`. Também implementa duas classes concretas: `SqlUserRepository` e `ApiUserRepository`, cada uma fornecendo uma implementação para os métodos da interface de acordo com o tipo de armazenamento de dados.

- **user_service.py**: Este arquivo define a classe `UserService`, que depende de uma instância de `UserRepository`. A classe `UserService` oferece métodos para obter todos os usuários e adicionar um novo usuário, delegando as operações ao `UserRepository` fornecido.

- **main.py**: Este arquivo é o ponto de entrada do programa. Ele instancia diferentes repositórios (`SqlUserRepository` e `ApiUserRepository`) e passa-os para a instância de `UserService`. Demonstramos como usar `UserService` com diferentes implementações de `UserRepository`, mostrando a flexibilidade proporcionada pela injeção de dependência.

Essa estrutura de código segue o Princípio da Inversão de Dependência, onde as classes de alto nível, como `UserService`, dependem de abstrações (interfaces), e não de implementações concretas de baixo nível. Isso torna o código mais flexível, modular e fácil de manter.

> [retornar](#d---dependency-inversion-principle) para o topo da página
>
> [voltar](./m7-notes.md) para página aterior

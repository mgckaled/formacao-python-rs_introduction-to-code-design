# I - Interface Segregation Principle

> [voltar](./m7-notes.md) para página aterior

## Definição

O Princípio da Segregação de Interfaces (*Interface Segregation Principle*) é um princípio que afirma que uma classe não deve ser forçada a depender de interfaces que ela não utiliza. Em outras palavras, é melhor ter muitas interfaces específicas do que uma única interface geral. Isso promove a coesão e evita que as classes tenham dependências desnecessárias de funcionalidades que não precisam.

## Exemplos de Uso

1. **Interfaces de Serviços:**
   - Em um sistema de e-commerce, você pode ter uma interface `PaymentService` que inclui métodos para processar pagamentos, verificar status de pagamento, reembolsar pagamentos, etc.
   - No entanto, nem todas as classes que interagem com pagamentos precisam de todos esses métodos. Por exemplo, uma classe de `OrderProcessor` pode precisar apenas do método para processar pagamentos.
   - Seguindo o Princípio da Segregação de Interfaces, é melhor criar interfaces mais específicas, como `PaymentProcessor`, `PaymentStatusChecker`, `PaymentRefunder`, para que cada classe só precise implementar o que realmente utiliza.

2. **Interfaces de Usuário:**
   - Em uma aplicação com uma interface de usuário complexa, como um sistema de gerenciamento de projetos, diferentes partes da interface podem ter diferentes requisitos.
   - Por exemplo, uma parte da interface pode ser responsável apenas pela exibição de dados, enquanto outra pode ser responsável pela interação do usuário com os dados.
   - Segregar as interfaces de usuário de acordo com essas responsabilidades pode tornar o código mais claro e modular, permitindo que partes da interface sejam modificadas sem afetar outras partes.

3. **Interfaces de APIs:**
   - Ao projetar uma API para um serviço web, é importante segmentar as interfaces de acordo com as necessidades dos clientes.
   - Por exemplo, uma API de um sistema de armazenamento em nuvem pode ter interfaces separadas para operações de upload de arquivos, download de arquivos, gerenciamento de pastas, etc.
   - Isso permite que os clientes da API usem apenas as funcionalidades de que precisam, sem serem sobrecarregados por métodos ou endpoints que não são relevantes para eles.

4. **Sistemas de Plugins ou Extensões:**
   - Em um sistema que suporta plugins ou extensões, é importante que as interfaces fornecidas para os desenvolvedores de plugins sejam específicas e focadas nas necessidades dos plugins.
   - Por exemplo, em um editor de texto com suporte a plugins, pode haver interfaces separadas para funcionalidades como verificação ortográfica, realce de sintaxe, formatação de texto, etc.
   - Isso permite que os desenvolvedores de plugins implementem apenas as funcionalidades relevantes para seus plugins, sem serem obrigados a implementar métodos ou funcionalidades adicionais desnecessárias.

## Exemplo em Python

Um exemplo simples em Python que ilustra o Princípio da Segregação de Interfaces pode envolver um sistema de gerenciamento de funcionários, onde diferentes tipos de funcionários têm diferentes responsabilidades. Vamos criar um exemplo onde temos diferentes interfaces para diferentes tipos de funcionários:

```python
from abc import ABC, abstractmethod

# Interface para funcionários que podem trabalhar
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

# Interface para funcionários que podem receber salário
class Payable(ABC):
    @abstractmethod
    def pay(self):
        pass

# Interface para funcionários que podem receber benefícios
class Benefitable(ABC):
    @abstractmethod
    def provide_benefits(self):
        pass

# Classe para um desenvolvedor
class Developer(Workable, Payable, Benefitable):
    def work(self):
        print("Developer is coding")

    def pay(self):
        print("Developer is receiving salary")

    def provide_benefits(self):
        print("Developer is receiving benefits")

# Classe para um gerente
class Manager(Workable, Payable):
    def work(self):
        print("Manager is managing")

    def pay(self):
        print("Manager is receiving salary")

# Função para processar o pagamento de um funcionário
def process_payment(employee):
    employee.pay()

# Função para fornecer benefícios a um funcionário
def provide_benefits(employee):
    if isinstance(employee, Benefitable):
        employee.provide_benefits()
    else:
        print("Employee is not eligible for benefits")

# Função para atribuir trabalho a um funcionário
def assign_work(employee):
    employee.work()

# Criando instâncias de funcionários
developer = Developer()
manager = Manager()

# Realizando operações com os funcionários
assign_work(developer)  # Saída: Developer is coding
assign_work(manager)    # Saída: Manager is managing

process_payment(developer)  # Saída: Developer is receiving salary
process_payment(manager)    # Saída: Manager is receiving salary

provide_benefits(developer)  # Saída: Developer is receiving benefits
provide_benefits(manager)    # Saída: Employee is not eligible for benefits
```

Neste exemplo:

- Criamos três interfaces (`Workable`, `Payable` e `Benefitable`) que definem métodos específicos que diferentes tipos de funcionários podem implementar.
- As classes `Developer` e `Manager` implementam diferentes combinações dessas interfaces, dependendo das responsabilidades de cada tipo de funcionário.
- Temos funções (`process_payment`, `provide_benefits`, `assign_work`) que operam em funcionários, mas cada uma usa apenas os métodos relevantes para sua operação, respeitando assim a segregação de interfaces.
- Isso garante que cada tipo de funcionário tenha apenas as funcionalidades relevantes para suas responsabilidades, seguindo o Princípio da Segregação de Interfaces.

> [retornar](#i---interface-segregation-principle) para o topo da página
>
> [voltar](./m7-notes.md) para página aterior

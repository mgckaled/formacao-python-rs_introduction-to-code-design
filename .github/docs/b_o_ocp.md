# O - Open/Closed Principle

> [voltar](./m7-notes.md) para página aterior

## Definição

O Princípio Aberto/Fechado (*Open/Closed Principle*) é um princípio de design de software que afirma que as entidades de software (como classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação. Isso significa que o comportamento de uma entidade deve ser estendido por meio de novas funcionalidades sem alterar seu código-fonte existente. Em outras palavras, você pode adicionar novos recursos sem precisar alterar o código já existente.

## Exemplos de Uso

1. **Sistema de Processamento de Pagamentos:**
   - Imagine um sistema de processamento de pagamentos que precisa lidar com diferentes tipos de métodos de pagamento, como cartão de crédito, PayPal, Bitcoin, etc.
   - Em vez de modificar o código existente toda vez que um novo método de pagamento é adicionado, você pode estender o sistema adicionando novas classes para cada método de pagamento, mantendo o código existente inalterado.
   - Por exemplo, você pode ter uma classe base `PaymentProcessor` com métodos comuns e, em seguida, criar subclasses específicas para cada tipo de pagamento, como `CreditCardPaymentProcessor`, `PayPalPaymentProcessor`, etc.

2. **Renderização de Diferentes Formatos de Documento:**
   - Suponha que você tenha um sistema que renderize documentos em diferentes formatos, como HTML, PDF, XML, etc.
   - Você pode projetar uma interface comum para os renderizadores de documento e criar implementações específicas para cada formato, seguindo o princípio Aberto/Fechado.
   - Assim, se você quiser adicionar suporte para um novo formato de documento, basta criar uma nova classe de renderização para esse formato, sem modificar o código existente.

3. **Sistema de Geração de Relatórios:**
   - Em um sistema de geração de relatórios, você pode ter diferentes tipos de relatórios, como relatórios de vendas, relatórios de estoque, etc.
   - Cada tipo de relatório pode exigir diferentes campos e formatos de saída.
   - Você pode aplicar o Princípio Aberto/Fechado criando uma estrutura flexível que permita adicionar novos tipos de relatórios sem modificar a lógica existente de geração de relatórios.

4. **Sistema de Plugins ou Extensões:**
   - Ao desenvolver sistemas que suportam plugins ou extensões, é fundamental seguir o Princípio Aberto/Fechado.
   - Os plugins podem estender a funcionalidade do sistema sem modificar o código principal.
   - Por exemplo, em um sistema de edição de imagem, os plugins podem adicionar novos filtros, ferramentas de desenho, etc., sem alterar o código-base da aplicação.

5. **Framework de Middleware:**
   - Em frameworks de middleware, como frameworks de web, é comum seguir o Princípio Aberto/Fechado.
   - Os desenvolvedores podem estender o comportamento do framework através de middleware, adicionando novas camadas de processamento sem alterar o código-fonte principal do framework.

Em todos esses exemplos, o Princípio Aberto/Fechado permite que novas funcionalidades sejam adicionadas de forma flexível e modular, mantendo o código existente estável e sem a necessidade de alterações. Isso resulta em sistemas mais extensíveis, fáceis de manter e com menor probabilidade de introduzir bugs ao fazer alterações.

## Exemplo em Python

```python
class Programer:
    def make(self):
        print("Programmer creating code")


class Seller:
    def make(self):
        print("Seller selling the product")


class RH:
    def make(self):
        print("HR hiring new devs")


class Company:
    def do_work(self, worker: any) -> None:
        worker.make()


programmer = Programer()
seller = Seller()
rh = RH()
company = Company()
company.do_work(programmer)
company.do_work(seller)
company.do_work(rh)
```

O código acima ilustra o Princípio Aberto/Fechado ao utilizar a polimorfismo para permitir que diferentes tipos de trabalhadores executem tarefas específicas sem a necessidade de modificar a classe `Company`. Aqui está uma explicação detalhada de cada ponto do código:

1. **Classes `Programmer`, `Seller` e `RH`:**
   - Cada uma dessas classes representa um tipo de trabalhador na empresa.
   - Cada classe possui um método `make()` que simula a realização de uma atividade específica relacionada ao trabalho do respectivo tipo de trabalhador.

2. **Classe `Company`:**
   - Esta classe tem um método `do_work()` que aceita um parâmetro `worker`.
   - O método `do_work()` simplesmente chama o método `make()` do trabalhador passado como argumento.

3. **Instâncias das Classes de Trabalhadores:**
   - São criadas instâncias das classes `Programmer`, `Seller` e `RH`, representando diferentes tipos de trabalhadores na empresa.

4. **Execução das Tarefas:**
   - A instância da classe `Company` é criada.
   - O método `do_work()` é chamado três vezes, cada vez com uma instância diferente de trabalhador (`programmer`, `seller` e `rh`) passada como argumento.
   - Como cada classe de trabalhador tem seu próprio método `make()`, quando o método `do_work()` é chamado para cada tipo de trabalhador, ele executa a tarefa específica relacionada ao tipo de trabalhador.

Essa implementação segue o Princípio Aberto/Fechado, pois a classe `Company` está aberta para extensão (pode trabalhar com diferentes tipos de trabalhadores), mas fechada para modificação (não é necessário alterar o código da classe `Company` sempre que um novo tipo de trabalhador for adicionado). Novos tipos de trabalhadores podem ser facilmente adicionados à empresa sem a necessidade de alterar a lógica existente na classe `Company`, garantindo assim um código mais flexível e fácil de manter.

> [retornar](#o---openclosed-principle) para o topo da página
>
> [voltar](./m7-notes.md) para página aterior

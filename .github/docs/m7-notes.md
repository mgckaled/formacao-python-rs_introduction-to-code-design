# Módulo 7 - Conceitos de SOLID

> [retornar](../../README.md) para a página anterior

## Sumário

- [Módulo 7 - Conceitos de SOLID](#módulo-7---conceitos-de-solid)
  - [Sumário](#sumário)
  - [Introdução ao SOLID](#introdução-ao-solid)
  - [Exemplos em Python](#exemplos-em-python)
  - [Questionário Avaliativo - Módulo 7](#questionário-avaliativo---módulo-7)
  - [Desafios](#desafios)
    - [Desafio SRP](#desafio-srp)
    - [Desafio OCP](#desafio-ocp)

## Introdução ao SOLID

São 5 princípios de design de classe orientado a objetos. Esses cinco princípios nos ajudam a entender a necessidade de determinados padrões de projetos de arquitetura de software em geral. SOLID foram apresentados pela primeira vez pelo famoso cientista da computação Robert J. Martin.

- **S** - *Single Responsability Principle* (Princípio da Responsabilidade Única)
- **O** - *Open/Closed Principle* (Princípio Aberto/Fechado)
- **L** - *Liskov Substitution Principle* (Princípio da Substituição de Liskov)
- **I** - *Interface Segregation Principle* (Princípio da Segregação de Interfaces)
- **D** - *Dependency Inversion Principle* (Princípio Princípio da Intversão de Depedências)

## Exemplos em Python

- [`Single Responsability Principle`](./a_s_srp.md)
- [`Open/Closed Principle`](./b_o_ocp.md)
- [`Liskov Substitution Principle`](./c_l_lsp.md)
- [`Interface Segregation Principle`](./d_i_isp.md)
- [`Dependency Inversion Principle`](./e_d_dip.md)

## Questionário Avaliativo - Módulo 7

1 - *Qual é o objetivo principal do SOLID no desenvolvimento de software?* - **Resposta:** Facilitar a manutenção e extensibilidade do código.

2 - *Quais são os cinco princípios que compõem o acrônimo SOLID?* - **Resposta:** Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.

3 - *Explique o que significa o Princípio da Responsabilidade Única (SRP) dentro do SOLID.* - **Resposta:** Classes devem ser responsáveis por um único aspecto ou funcionalidade do software.

4 - *Como o Princípio Aberto-Fechado (OCP) é aplicado no contexto do SOLID?* - **Resposta:** Classes devem ser abertas para extensão, mas fechadas para modificações.

5 - *O que o Princípio da Substituição de Liskov (LSP) busca garantir em um sistema orientado a objetos?* - **Resposta:** A garantia de que uma classe derivada possa ser substituída por sua classe base sem afetar o comportamento do programa.

6 - *Qual é a importância do Princípio da Segregação de Interfaces (ISP) no desenvolvimento de software?* - **Resposta:** Dividir interfaces grandes e monolíticas em interfaces menores e mais específicas.

7 - *Como o Princípio da Inversão de Dependência (DIP) pode melhorar a flexibilidade e a manutenibilidade de um sistema?* - **Resposta:** Invertendo o controle das dependências, permitindo que classes de alto nível não dependam de implementações específicas de classes de baixo nível.

8 - *Qual dos princípios abaixo NÃO representa princípios que compoem o SOLID?* - **Resposta:** Princípio de Pareto.

9 - *Como o uso adequado dos princípios do SOLID pode facilitar a escalabilidade e a evolução de um sistema de software ao longo do tempo?* - **Resposta:** Promovendo a modularidade e a reutilização de código, permitindo que novos recursos sejam adicionados com mais facilidade.

## Desafios

### Desafio SRP

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins. Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras classes com suas devidas responsabilidades.

```python
class TaskHandler:
    def conect_api():
        pass

    def create_task():
        pass

    def update_task():
        pass

    def remove_task():
        pass

    def send_notification():
        pass

    def generate_report():
        pass

    def send_report():
        pass
```

### Desafio OCP

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames, deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo. A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

```python
class AprovaExame:
    def aprovar_solicitacao_exame(self, exame):

        if exame_sangue.tipo == "sangue":
            if aprovador.verifica_condicoes_exame_sangue(exame_sangue):
                print("Exame sanguíneo aprovado!")

        elif exame_raio_x.tipo == "raio-x":
            if aprovador.verifica_condicoes_raio_x(exame_raio_x):
                print("Raio-X aprovado!")
                pass

    def verifica_condicoes_exame_sangue(self, exame):
        # implemente as condições específicas do exame de sangue
        pass

    def verifica_condicoes_raio_x(self, exame):
        # implemente as condições específicas do exame de raio-x
        pass

# Exemplo de uso:
class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovador = AprovaExame()
```

> [voltar](#módulo-7---conceitos-de-solid) para o topo da página
>
> [retornar](../../README.md) para a página anterior

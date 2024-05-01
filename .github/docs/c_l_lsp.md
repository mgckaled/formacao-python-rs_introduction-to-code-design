# L - Liskov Substitution Principle

> [voltar](./m7-notes.md) para página aterior

## Definição

O Princípio da Substituição de Liskov (*Liskov Substitution Principle*) é um princípio de design de software que afirma que objetos de uma classe base devem ser substituíveis por objetos de suas subclasses sem afetar a corretude do programa. Em outras palavras, se S é um subtipo de T, então os objetos do tipo T podem ser substituídos por objetos do tipo S sem alterar as propriedades do programa. Isso garante que as subclasses mantenham o comportamento esperado da classe base, promovendo a reutilização de código e a interoperabilidade entre diferentes tipos de objetos.

## Exemplos de Uso

1. **Herança em Orientação a Objetos:**
   - Suponha que você tenha uma classe base `Shape` com métodos como `area()` e `perimeter()`, e duas subclasses `Rectangle` e `Circle` que estendem `Shape`.
   - Seguindo o Princípio da Substituição de Liskov, as instâncias de `Rectangle` e `Circle` devem poder ser usadas onde instâncias de `Shape` são esperadas, sem alterar o comportamento do programa.

2. **Interfaces e Polimorfismo:**
   - Ao definir interfaces em linguagens que suportam polimorfismo, como Java ou TypeScript, você pode garantir que as classes que implementam uma interface possam ser substituídas umas pelas outras sem afetar a funcionalidade do programa.
   - Por exemplo, se você tem uma interface `Logger` com um método `log(message: string)`, qualquer classe que implemente essa interface pode ser usada onde um `Logger` é esperado.

3. **Framework de Testes:**
   - Em frameworks de teste, como o JUnit para Java ou o PyTest para Python, os testes devem ser projetados de forma que seja fácil adicionar novos casos de teste sem afetar os testes existentes.
   - Ao seguir o Princípio da Substituição de Liskov, você pode criar novos casos de teste ou estender testes existentes sem modificar a lógica principal dos testes.

4. **Implementação de Coleções:**
   - Em linguagens que suportam tipos genéricos, como Java ou C#, é comum usar coleções genéricas para armazenar objetos de diferentes tipos.
   - Ao garantir que os tipos de dados armazenados na coleção sejam substituíveis sem afetar a funcionalidade do programa, você está aplicando o Princípio da Substituição de Liskov.

5. **Sobrescrita de Métodos em Subclasses:**
   - Ao sobrescrever métodos em subclasses, é importante garantir que o comportamento do método na subclasse seja consistente com o comportamento na classe base.
   - Por exemplo, se uma classe base tem um método `calculate()` que retorna um valor, uma subclasse que sobrescreve esse método deve retornar um valor compatível sem alterar a semântica do método.

6. **Sistemas de Controle de Acesso:**
   - Em sistemas de controle de acesso, diferentes tipos de usuários podem ter permissões diferentes.
   - Ao projetar o sistema de forma que diferentes tipos de usuários possam ser substituídos uns pelos outros sem afetar as operações de controle de acesso, você está aplicando o Princípio da Substituição de Liskov.

## Exemplo em Python

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Saída: Woof!
make_animal_speak(cat)  # Saída: Meow!
```

- `Animal` é a classe base que define um método `speak()` que deve ser implementado pelas subclasses.
- `Dog` e `Cat` são subclasses de `Animal` que substituem o método `speak()` para retornar os sons de um cachorro e de um gato, respectivamente.
- A função `make_animal_speak()` aceita qualquer objeto que seja uma instância de `Animal` e chama o método `speak()` do objeto passado como argumento.
- Quando a função `make_animal_speak()` é chamada com instâncias de `Dog` e `Cat`, ela produz saídas diferentes conforme esperado, demonstrando que objetos das subclasses podem ser usados onde objetos da classe base são esperados sem afetar o comportamento do programa.

> [retornar](#l---liskov-substitution-principle) para o topo da página
>
> [voltar](./m7-notes.md) a página aterior

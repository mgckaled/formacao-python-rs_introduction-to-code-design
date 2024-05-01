from abc import ABC, abstractmethod


class Exame(ABC):
    @abstractmethod
    def verificar_condicoes(self):
        pass


class ExameSangue(Exame):
    def verificar_condicoes(self):
        # Simulação de verificação de condições para exame de sangue
        print("Verificando condições para exame de sangue")
        return True  # Simulação: sempre aprovado


class ExameRaioX(Exame):
    def verificar_condicoes(self):
        # Simulação de verificação de condições para exame de raio-x
        print("Verificando condições para exame de raio-x")
        return False  # Simulação: sempre reprovado


class AprovaExame:
    def aprovar_solicitacao_exame(self, exame):
        if isinstance(exame, Exame):
            if exame.verificar_condicoes():
                print(f"{exame.__class__.__name__} aprovado!")
            else:
                print(f"{exame.__class__.__name__} reprovado!")


exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

aprovador = AprovaExame()
aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)

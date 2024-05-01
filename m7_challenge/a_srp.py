class APIClient:
    def connect(self):
        # Simulação de conexão à API
        print("Conectado à API")


class TaskManager:
    def create_task(self, task_data):
        # Simulação de criação de uma nova tarefa
        print("Tarefa criada:", task_data)

    def update_task(self, task_id, updated_data):
        # Simulação de atualização de uma tarefa existente
        print("Tarefa atualizada:", task_id, updated_data)

    def remove_task(self, task_id):
        # Simulação de remoção de uma tarefa existente
        print("Tarefa removida:", task_id)


class NotificationManager:
    def send_notification(self, message):
        # Simulação de envio de notificação
        print("Notificação enviada:", message)


class ReportGenerator:
    def generate_report(self, tasks):
        # Simulação de geração de relatório com base nas tarefas
        report = "\n".join([f"- {task}" for task in tasks])
        return "Relatório de Tarefas:\n" + report


class ReportSender:
    def send_report(self, report):
        # Simulação de envio de relatório
        print("Relatório enviado:", report)

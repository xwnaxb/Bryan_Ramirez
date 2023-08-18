class TicketMachine:
    destinations = {
        "Destino A": 50,
        "Destino B": 75,
        "Destino C": 100
    }

    def __init__(self):
        self.user_card = None
        self.user_pin = None

    def start(self):
        print("Bienvenido al sistema de expedición de billetes de tren.")
        print("Seleccione su destino:")

        for destination in self.destinations:
            print(f"- {destination}")

        selected_destination = input("Destino seleccionado: ")
        if selected_destination in self.destinations:
            self.process_ticket(selected_destination)
        else:
            print("Destino no válido.")

    def process_ticket(self, destination):
        print(f"Ha seleccionado {destination}.")
        self.user_card = input("Introduzca el número de tarjeta de crédito: ")
        self.user_pin = input("Introduzca su número de identificación personal: ")

        if self.validate_credit_transaction():
            self.issue_ticket(destination)
            print("¡Billete emitido con éxito!")
        else:
            print("Transacción de crédito no válida. Billete no emitido.")

    def validate_credit_transaction(self):
        # Aquí podrías implementar la lógica de validación de la transacción de crédito
        # Por ejemplo, verificar la tarjeta de crédito y el PIN con una base de datos o servicio externo.
        # En este ejemplo, simplemente simularemos una validación exitosa.
        return True

    def issue_ticket(self, destination):
        ticket_price = self.destinations[destination]
        print(f"Billete emitido para {destination}. Precio: ${ticket_price}")
        # Aquí podrías implementar la lógica para cargar el monto a la tarjeta de crédito.

if __name__ == "__main__":
    ticket_machine = TicketMachine()
    ticket_machine.start()

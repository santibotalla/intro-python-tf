class Cuenta(object):

    def __init__(self, titular, monto_inicio=0, numero_de_cuenta=0):  # contructor, siempre de la misma forma
        self.titular = titular
        self.cantidad = monto_inicio
        self.numero_de_cuenta = numero_de_cuenta
        self.activa = True

    def aplicar_gasto(self, monto):  # retirar
        # TODO: Chequear si la cuenta está activa
        self.cantidad = self.cantidad - monto

    def aplicar_deposito(self, monto):  # ingresar
        # TODO: Chequear si la cuenta está activa
        self.cantidad = self.cantidad + monto

    def mostrar(self):
        # TODO: Agregar si está activa o no y numero de cuenta
        print(f"{self.titular}: {self.cantidad}")

    def cambiar_titular(self, titular_p):
        self.titular = titular_p

    def cerrar(self):
        # TODO: Solo si el saldo es cero
        self.activa = False

    def a_tupla(self):
        return self.numero_de_cuenta, self.titular, self.cantidad, self.activa


class CuentaJoven(Cuenta):

    def __init__(self, titular, bonificacion, monto_inicio=0, numero_de_cuenta=0):
        Cuenta.__init__(self, titular, monto_inicio, numero_de_cuenta)
        self.bonificacion = bonificacion

    def mostrar(self):
        print(f"CUENTA JOVEN: {self.titular}: {self.cantidad}")

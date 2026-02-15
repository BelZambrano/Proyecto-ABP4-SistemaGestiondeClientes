class Cliente:
    def __init__(self, id_cliente, nombre, email, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def tipo(self):
        return "regular"

    def get_beneficios(self):
        return "Sin beneficios especiales"

    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "categoria": self.tipo(),
        }


class ClienteRegular(Cliente):
    def tipo(self):
        return "regular"

    def get_beneficios(self):
        return "Sin beneficios especiales"


class ClientePremium(Cliente):
    def tipo(self):
        return "premium"

    def get_beneficios(self):
        return "Descuento del 10%"


class ClienteCorporativo(Cliente):
    def tipo(self):
        return "corporativo"

    def get_beneficios(self):
        return "Descuento del 20% y atención prioritaria"


def cliente_desde_dict(data: dict) -> Cliente:
    categoria = (data.get("categoria") or "regular").strip().lower()

    id_cliente = data.get("id_cliente")
    nombre = data.get("nombre")
    email = data.get("email")
    telefono = data.get("telefono")

    if categoria == "premium":
        return ClientePremium(id_cliente, nombre, email, telefono)
    if categoria == "corporativo":
        return ClienteCorporativo(id_cliente, nombre, email, telefono)
    return ClienteRegular(id_cliente, nombre, email, telefono)

class Cliente:
    def __init__(self, id_cliente, nombre, email, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def tipo(self):
        return "general"

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


class ClientePremium(Cliente):
    def tipo(self):
        return "premium"


class ClienteCorporativo(Cliente):
    def tipo(self):
        return "corporativo"


def cliente_desde_dict(data: dict) -> Cliente:
    cat = str(data.get("categoria", "")).strip().lower()

    if cat in ("premium",):
        cls = ClientePremium
    elif cat in ("corporativo", "corporate"):
        cls = ClienteCorporativo
    else:
        cls = ClienteRegular  # también cubre "normal"

    return cls(
        data.get("id_cliente"),
        data.get("nombre", ""),
        data.get("email", ""),
        data.get("telefono", ""),
    )

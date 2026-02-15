class Cliente:
    def __init__(self, id_cliente, nombre, email, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self._email = None
        self._telefono = None

        self.email = email  # pasa por setter
        self.telefono = telefono  # pasa por setter

    # --- Encapsulación email ---
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        valor = (valor or "").strip()
        if "@" not in valor:
            raise ValueError("Email inválido.")
        self._email = valor.lower()

    # --- Encapsulación telefono ---
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        valor = (valor or "").strip()
        if len(valor) < 8:
            raise ValueError("Teléfono inválido.")
        self._telefono = valor

    # --- Polimorfismo base ---
    def tipo(self):
        return "regular"

    def get_beneficios(self):
        return "Sin beneficios especiales"

    # --- Métodos especiales ---
    def __str__(self):
        return f"{self.nombre} ({self.tipo()})"

    def __eq__(self, other):
        if not isinstance(other, Cliente):
            return False
        return self.id_cliente == other.id_cliente

    # --- Persistencia ---
    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "categoria": self.tipo(),
        }


class ClienteRegular(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono):
        super().__init__(id_cliente, nombre, email, telefono)

    def tipo(self):
        return "regular"

    def get_beneficios(self):
        return "Sin beneficios especiales"


class ClientePremium(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono):
        super().__init__(id_cliente, nombre, email, telefono)

    def tipo(self):
        return "premium"

    def get_beneficios(self):
        return "Descuento del 10%"


class ClienteCorporativo(Cliente):
    def __init__(self, id_cliente, nombre, email, telefono):
        super().__init__(id_cliente, nombre, email, telefono)

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

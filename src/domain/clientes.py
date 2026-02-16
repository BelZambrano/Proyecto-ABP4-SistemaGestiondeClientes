from __future__ import annotations

from src.utils.exceptions import EmailInvalidoError, TelefonoInvalidoError


class Cliente:
    def __init__(self, id_cliente, nombre, email, telefono):
        self.id_cliente = id_cliente
        self.nombre = (nombre or "").strip()

        # “privados” (encapsulación)
        self._email = None
        self._telefono = None

        # pasan por setters (validación)
        self.email = email
        self.telefono = telefono

    # --- Encapsulación con properties (getter/setter) ---
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        valor = (valor or "").strip().lower()
        if "@" not in valor or "." not in valor:
            raise EmailInvalidoError("Email inválido. Ej: nombre@correo.com")
        self._email = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        valor = (valor or "").strip()

        # permite +56 9XXXXXXXX o 9XXXXXXXX o 8+ dígitos simples
        limpio = valor.replace(" ", "").replace("-", "")
        if limpio.startswith("+"):
            limpio = limpio[1:]

        if not limpio.isdigit() or len(limpio) < 8:
            raise TelefonoInvalidoError(
                "Teléfono inválido. Ej: +56 912345678 o 912345678"
            )
        self._telefono = valor

    # --- Polimorfismo (se sobreescribe en subclases) ---
    def tipo(self):
        return "regular"

    def get_beneficios(self):
        return "Sin beneficios especiales"

    # --- Entregable: métodos especiales ---
    def __str__(self):
        return f"{self.nombre} ({self.tipo()})"

    def __eq__(self, other):
        return isinstance(other, Cliente) and self.id_cliente == other.id_cliente

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
    def __init__(self, id_cliente, nombre, email, telefono):
        super().__init__(id_cliente, nombre, email, telefono)  # ✅ entregable super()

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

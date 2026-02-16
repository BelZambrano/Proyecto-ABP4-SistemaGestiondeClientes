import re
from src.utils.exceptions import (
    NombreInvalidoError,
    EmailInvalidoError,
    TelefonoInvalidoError,
    CategoriaInvalidaError,
)


CATEGORIAS_VALIDAS = {"regular", "premium", "corporativo"}


def validar_nombre(nombre: str) -> str:
    nombre = (nombre or "").strip()
    if len(nombre) < 2:
        raise NombreInvalidoError("Nombre inválido: mínimo 2 caracteres.")
    return nombre


def validar_email(email: str) -> str:
    email = (email or "").strip().lower()
    patron = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if not re.match(patron, email):
        raise EmailInvalidoError("Email inválido. Ej: nombre@correo.com")
    return email


def validar_telefono(telefono: str) -> str:
    telefono = (telefono or "").strip()
    patron = r"^(\+56\s?)?9\d{8}$"
    if not re.match(patron, telefono):
        raise TelefonoInvalidoError("Teléfono inválido. Ej: +56 912345678 o 912345678")
    return telefono


def validar_categoria(categoria: str) -> str:
    categoria = (categoria or "").strip().lower()
    if categoria == "":
        return "regular"
    if categoria not in CATEGORIAS_VALIDAS:
        raise CategoriaInvalidaError(
            "Categoría inválida. Usa: regular / premium / corporativo"
        )
    return categoria

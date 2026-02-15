from src.persistence.json_repo import (
    cargar_clientes,
    guardar_clientes,
    obtener_siguiente_id,
)
from src.domain.clientes import (
    ClienteRegular,
    ClientePremium,
    ClienteCorporativo,
    cliente_desde_dict,
)

from src.validators.cliente_validator import (
    validar_nombre,
    validar_email,
    validar_telefono,
    validar_categoria,
)

from src.utils.exceptions import ClienteNoEncontradoError, ArchivoDatosError


class ClienteService:
    def _instanciar_por_categoria(self, id_cliente, nombre, email, telefono, categoria):
        if categoria == "premium":
            return ClientePremium(id_cliente, nombre, email, telefono)
        if categoria == "corporativo":
            return ClienteCorporativo(id_cliente, nombre, email, telefono)
        return ClienteRegular(id_cliente, nombre, email, telefono)

    def crear_cliente(
        self, nombre: str, email: str, telefono: str, categoria: str = "regular"
    ) -> int:
        try:
            clientes_dict = cargar_clientes()
        except Exception as e:
            raise ArchivoDatosError(f"No pude leer el JSON: {e}")

        nombre = validar_nombre(nombre)
        email = validar_email(email)
        telefono = validar_telefono(telefono)
        categoria = validar_categoria(categoria)

        nuevo_id = obtener_siguiente_id(clientes_dict)

        cliente = self._instanciar_por_categoria(
            nuevo_id, nombre, email, telefono, categoria
        )
        clientes_dict.append(cliente.to_dict())

        try:
            guardar_clientes(clientes_dict)
        except Exception as e:
            raise ArchivoDatosError(f"No pude guardar el JSON: {e}")

        return nuevo_id

    def listar_clientes(self) -> list:
        try:
            clientes_dict = cargar_clientes()
        except Exception as e:
            raise ArchivoDatosError(f"No pude leer el JSON: {e}")

        return [cliente_desde_dict(d) for d in clientes_dict]

    def obtener_por_id(self, id_cliente: int):
        clientes = self.listar_clientes()
        for c in clientes:
            if c.id_cliente == id_cliente:
                return c
        raise ClienteNoEncontradoError(f"No existe cliente con ID {id_cliente}.")

    def editar_cliente(
        self,
        id_cliente: int,
        nombre: str = "",
        email: str = "",
        telefono: str = "",
        categoria: str = "",
    ) -> bool:
        try:
            clientes_dict = cargar_clientes()
        except Exception as e:
            raise ArchivoDatosError(f"No pude leer el JSON: {e}")

        encontrado = None
        for d in clientes_dict:
            if d.get("id_cliente") == id_cliente:
                encontrado = d
                break

        if not encontrado:
            raise ClienteNoEncontradoError(f"No existe cliente con ID {id_cliente}.")

        # Valores actuales
        nuevo_nombre = encontrado.get("nombre", "")
        nuevo_email = encontrado.get("email", "")
        nuevo_telefono = encontrado.get("telefono", "")
        nueva_categoria = (encontrado.get("categoria") or "regular").strip().lower()

        # Solo validar si el usuario escribió algo
        if nombre.strip():
            nuevo_nombre = validar_nombre(nombre)
        if email.strip():
            nuevo_email = validar_email(email)
        if telefono.strip():
            nuevo_telefono = validar_telefono(telefono)
        if categoria.strip():
            nueva_categoria = validar_categoria(categoria)

        cliente_obj = self._instanciar_por_categoria(
            id_cliente, nuevo_nombre, nuevo_email, nuevo_telefono, nueva_categoria
        )

        idx = clientes_dict.index(encontrado)
        clientes_dict[idx] = cliente_obj.to_dict()

        try:
            guardar_clientes(clientes_dict)
        except Exception as e:
            raise ArchivoDatosError(f"No pude guardar el JSON: {e}")

        return True

    def eliminar_cliente(self, id_cliente: int) -> bool:
        try:
            clientes_dict = cargar_clientes()
        except Exception as e:
            raise ArchivoDatosError(f"No pude leer el JSON: {e}")

        original = len(clientes_dict)
        clientes_dict = [d for d in clientes_dict if d.get("id_cliente") != id_cliente]

        if len(clientes_dict) == original:
            raise ClienteNoEncontradoError(f"No existe cliente con ID {id_cliente}.")

        try:
            guardar_clientes(clientes_dict)
        except Exception as e:
            raise ArchivoDatosError(f"No pude guardar el JSON: {e}")

        return True

    # Por si tu menú aún los usa en algún lado
    def _cargar_clientes_dict(self) -> list:
        return cargar_clientes()

    def _guardar_clientes_dict(self, clientes_dict: list) -> None:
        guardar_clientes(clientes_dict)

from src.persistence.json_repo import cargar_clientes, guardar_clientes, obtener_siguiente_id
from src.domain.clientes import ClienteRegular, ClientePremium, ClienteCorporativo, cliente_desde_dict


class ClienteService:
    def crear_cliente(self, nombre: str, email: str, telefono: str, categoria: str = "regular") -> int:
        clientes_dict = cargar_clientes()
        nuevo_id = obtener_siguiente_id(clientes_dict)

        cat = (categoria or "").strip().lower()

        if cat == "premium":
            cliente = ClientePremium(nuevo_id, nombre.strip(), email.strip(), telefono.strip())
        elif cat == "corporativo":
            cliente = ClienteCorporativo(nuevo_id, nombre.strip(), email.strip(), telefono.strip())
        else:
            cliente = ClienteRegular(nuevo_id, nombre.strip(), email.strip(), telefono.strip())

        clientes_dict.append(cliente.to_dict())
        guardar_clientes(clientes_dict)
        return nuevo_id

    def listar_clientes(self) -> list:
        clientes_dict = cargar_clientes()
        return [cliente_desde_dict(c) for c in clientes_dict]


    def _cargar_clientes_dict(self) -> list:
        return cargar_clientes()

    def _guardar_clientes_dict(self, clientes_dict: list) -> None:
        guardar_clientes(clientes_dict)

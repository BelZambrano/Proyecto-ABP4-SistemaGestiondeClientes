import json
from src.utils.exceptions import ArchivoDatosError

RUTA_JSON = "data/clientes.json"


def cargar_clientes() -> list[dict]:
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            if contenido == "":
                return []
            return json.loads(contenido)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError as e:
        raise ArchivoDatosError(f"JSON corrupto: {e}")


def guardar_clientes(lista_clientes: list[dict]) -> None:
    try:
        with open(RUTA_JSON, "w", encoding="utf-8") as f:
            json.dump(lista_clientes, f, ensure_ascii=False, indent=2)
    except OSError as e:
        raise ArchivoDatosError(f"No se pudo guardar el archivo: {e}")


def obtener_siguiente_id(lista_clientes: list[dict]) -> int:
    if not lista_clientes:
        return 1
    max_id = max(c.get("id_cliente", 0) for c in lista_clientes)
    return max_id + 1

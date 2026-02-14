import json
import os

RUTA_JSON = os.path.join("data", "clientes.json")


def cargar_clientes():
    if not os.path.exists(RUTA_JSON):
        return []

    with open(RUTA_JSON, "r", encoding="utf-8") as f:
        contenido = f.read().strip()
        if contenido == "":
            return []
        return json.loads(contenido)


def guardar_clientes(lista_clientes):
    with open(RUTA_JSON, "w", encoding="utf-8") as f:
        json.dump(lista_clientes, f, ensure_ascii=False, indent=2)


def obtener_siguiente_id(lista_clientes):
    if len(lista_clientes) == 0:
        return 1
    max_id = max(c["id_cliente"] for c in lista_clientes)
    return max_id + 1

from src.services.cliente_service import ClienteService


def mostrar_menu():
    print("\n=== GESTOR INTELIGENTE DE CLIENTES ===")
    print("1) Crear cliente")
    print("2) Listar clientes")
    print("3) Editar cliente")
    print("4) Eliminar cliente")
    print("0) Salir")


def pedir_opcion():
    return input("Elige una opción: ").strip()


def run_menu():
    service = ClienteService()

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            categoria = input(
                "Categoría (regular/premium/corporativo) [Enter=regular]: "
            )

            nuevo_id = service.crear_cliente(nombre, email, telefono, categoria)
            print(f"✅ Cliente guardado con ID {nuevo_id}")

        elif opcion == "2":
            clientes = service.listar_clientes()

            if len(clientes) == 0:
                print("No hay clientes registrados.")
            else:
                print("\n--- LISTA DE CLIENTES ---")
                for c in clientes:
                    print(f"ID: {c.id_cliente}")
                    print(f"Nombre: {c.nombre}")
                    print(f"Email: {c.email}")
                    print(f"Teléfono: {c.telefono}")
                    print(f"Categoría: {c.tipo()}")
                    print(f"Beneficios: {c.get_beneficios()}")
                    print("-" * 30)

        elif opcion == "3":
            clientes = service.listar_clientes()

            if len(clientes) == 0:
                print("No hay clientes para editar.")
                continue

            try:
                id_buscar = int(input("Ingrese el ID del cliente a editar: "))
            except ValueError:
                print("ID inválido.")
                continue

            encontrado = None
            for c in clientes:
                if c.id_cliente == id_buscar:
                    encontrado = c
                    break

            if encontrado is None:
                print("Cliente no encontrado.")
                continue

            print("Deja vacío si no quieres modificar un campo.")
            nuevo_nombre = input(f"Nuevo nombre ({encontrado.nombre}): ").strip()
            nuevo_email = input(f"Nuevo email ({encontrado.email}): ").strip()
            nuevo_telefono = input(f"Nuevo teléfono ({encontrado.telefono}): ").strip()
            nueva_categoria = input(f"Nueva categoría ({encontrado.tipo()}): ").strip()

            clientes_dict = service._cargar_clientes_dict()
            for d in clientes_dict:
                if d.get("id_cliente") == id_buscar:
                    if nuevo_nombre:
                        d["nombre"] = nuevo_nombre
                    if nuevo_email:
                        d["email"] = nuevo_email
                    if nuevo_telefono:
                        d["telefono"] = nuevo_telefono
                    if nueva_categoria:
                        d["categoria"] = nueva_categoria.strip().lower()
                    break

            service._guardar_clientes_dict(clientes_dict)
            print("✅ Cliente actualizado correctamente.")

        elif opcion == "4":
            clientes = service.listar_clientes()

            if len(clientes) == 0:
                print("No hay clientes para eliminar.")
                continue

            try:
                id_borrar = int(input("Ingrese el ID del cliente a eliminar: "))
            except ValueError:
                print("ID inválido.")
                continue

            encontrado = None
            for c in clientes:
                if c.id_cliente == id_borrar:
                    encontrado = c
                    break

            if encontrado is None:
                print("Cliente no encontrado.")
                continue

            confirmacion = (
                input(f"¿Seguro que deseas eliminar a '{encontrado.nombre}'? (s/n): ")
                .strip()
                .lower()
            )

            if confirmacion != "s":
                print("Operación cancelada.")
                continue

            clientes_dict = service._cargar_clientes_dict()
            clientes_dict = [
                d for d in clientes_dict if d.get("id_cliente") != id_borrar
            ]
            service._guardar_clientes_dict(clientes_dict)
            print("✅ Cliente eliminado correctamente.")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

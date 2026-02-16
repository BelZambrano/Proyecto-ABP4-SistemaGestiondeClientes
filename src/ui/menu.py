from src.services.cliente_service import ClienteService
from src.utils.exceptions import (
    ValidationError,
    ClienteNoEncontradoError,
    ArchivoDatosError,
)
from src.utils.logger import configurar_logger

logger = configurar_logger()


def mostrar_menu():
    print("\n=== GESTOR INTELIGENTE DE CLIENTES ===")
    print("1) Crear cliente")
    print("2) Listar clientes")
    print("3) Editar cliente")
    print("4) Eliminar cliente")
    print("0) Salir")


def pedir_opcion() -> str:
    return input("Elige una opción: ").strip()


def pedir_int(mensaje: str) -> int:
    while True:
        valor = input(mensaje).strip()
        try:
            return int(valor)
        except ValueError:
            print("❌ Debes ingresar un número entero.")


def imprimir_cliente(c):
    print(f"ID: {c.id_cliente}")
    print(f"Nombre: {c.nombre}")
    print(f"Email: {c.email}")
    print(f"Teléfono: {c.telefono}")
    print(f"Categoría: {c.tipo()}")
    print(f"Beneficios: {c.get_beneficios()}")
    print("-" * 30)


def run_menu():
    service = ClienteService()

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        try:
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
                if not clientes:
                    print("No hay clientes aún.")
                else:
                    for c in clientes:
                        imprimir_cliente(c)

            elif opcion == "3":
                id_cliente = pedir_int("ID a editar: ")

                # Mostrar actual (si existe)
                actual = service.obtener_por_id(id_cliente)
                print("\n--- Cliente actual ---")
                imprimir_cliente(actual)

                print("Deja vacío para mantener el valor actual.")
                nombre = input("Nuevo nombre: ")
                email = input("Nuevo email: ")
                telefono = input("Nuevo teléfono: ")
                categoria = input("Nueva categoría (regular/premium/corporativo): ")

                service.editar_cliente(id_cliente, nombre, email, telefono, categoria)
                print("✅ Cliente actualizado.")

            elif opcion == "4":
                id_cliente = pedir_int("ID a eliminar: ")
                confirm = input("¿Seguro? (s/n): ").strip().lower()
                if confirm == "s":
                    service.eliminar_cliente(id_cliente)
                    print("✅ Cliente eliminado.")
                else:
                    print("Ok, no se eliminó.")

            elif opcion == "0":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")

        except ValidationError as e:
            print(f"❌ {e}")

        except ClienteNoEncontradoError as e:
            print(f"⚠ {e}")

        except ArchivoDatosError as e:
            print(f"📁 {e}")

        except Exception as e:
            logger.exception("Error inesperado en el menú")
            print("⚠ Ocurrió un error inesperado. Revisa logs/app.log")

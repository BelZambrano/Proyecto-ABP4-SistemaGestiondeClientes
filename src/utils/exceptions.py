# Clase base para errores personalizados del sistema
class AppError(Exception):
    """Error base de la aplicación."""

    pass


# Clase base para errores de validación de datos
class ValidationError(AppError):
    """Error general de validación."""

    pass


# Se lanza cuando el nombre no cumple el formato esperado
class NombreInvalidoError(ValidationError):
    pass


# Se lanza cuando el email no cumple el formato esperado
class EmailInvalidoError(ValidationError):
    """El email ingresado no es válido."""

    pass


# Se lanza cuando el teléfono no cumple el formato requerido
class TelefonoInvalidoError(ValidationError):
    """El teléfono ingresado no es válido."""

    pass


# Se lanza cuando la categoría no es regular, premium o corporativo
class CategoriaInvalidaError(ValidationError):
    """La categoría ingresada no es válida."""

    pass


# Se lanza cuando se intenta buscar un cliente inexistente
class ClienteNoEncontradoError(AppError):
    """El cliente solicitado no existe."""

    pass


# Se lanza cuando ocurre un problema al leer o guardar el JSON
class ArchivoDatosError(AppError):
    """Error al procesar el archivo de datos."""

    pass

class AppError(Exception):
    pass


class ValidationError(AppError):
    pass


class NombreInvalidoError(ValidationError):
    pass


class EmailInvalidoError(ValidationError):
    pass


class TelefonoInvalidoError(ValidationError):
    pass


class CategoriaInvalidaError(ValidationError):
    pass


class ClienteNoEncontradoError(AppError):
    pass


class ArchivoDatosError(AppError):
    pass

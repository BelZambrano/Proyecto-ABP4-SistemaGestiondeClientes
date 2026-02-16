## 🧠 Gestor Inteligente de Clientes (ABP4)

Proyecto desarrollado en Python aplicando Programación Orientada a Objetos, herencia, validaciones personalizadas, manejo de excepciones y persistencia de datos en archivo JSON.

## 📌 Descripción

Este sistema permite gestionar clientes mediante operaciones CRUD desde consola:

Crear cliente

Listar clientes

Editar cliente

Eliminar cliente

El sistema valida datos de entrada, utiliza jerarquías de excepciones personalizadas y almacena la información de forma persistente en un archivo clientes.json.

## 🏗️ Arquitectura del Proyecto

El proyecto está organizado en capas siguiendo una estructura modular:

src/
 ├── domain/        → Modelos del dominio (Cliente y subclases)
 ├── services/      → Lógica de negocio (ClienteService)
 ├── persistence/   → Manejo de archivos JSON (JsonRepo)
 ├── validators/    → Validaciones de datos
 ├── utils/         → Excepciones personalizadas y logger
 └── ui/            → Menú de interacción por consola

## 🧬 Conceptos aplicados
🔹 Programación Orientada a Objetos

Clase base Cliente

Subclases:

ClienteRegular

ClientePremium

ClienteCorporativo

Uso de __init__

Uso de super()

Métodos especiales __str__ y __eq__

 🔹 Herencia y Polimorfismo

Cada tipo de cliente redefine:

tipo()

get_beneficios()

El sistema trabaja con objetos polimórficos sin necesidad de preguntar el tipo manualmente.

🔹 Manejo de Excepciones Personalizadas

Jerarquía implementada:

AppError
 ├── ValidationError
 │    ├── NombreInvalidoError
 │    ├── EmailInvalidoError
 │    ├── TelefonoInvalidoError
 │    └── CategoriaInvalidaError
 ├── ClienteNoEncontradoError
 └── ArchivoDatosError


Se aplicó:

raise para validaciones manuales

Captura diferenciada con except

Propagación de errores entre capas

 🔹 Persistencia de Datos

Archivo: data/clientes.json

Lectura y escritura mediante clase JsonRepo

Manejo seguro de archivos

Generación automática de ID incremental

🔹 Sistema de Logs

Se implementó un logger utilizando el módulo logging.

Archivo generado:

logs/app.log


Registra:

Errores inesperados

Posibles errores de persistencia

Esto permite separar:

Mensajes amigables al usuario

Información técnica para debugging

## ▶️ Cómo ejecutar el programa

Clonar el repositorio

Ubicarse en la carpeta raíz del proyecto

Ejecutar:

python main.py

## 🧪 Casos probados

Creación de cliente válido

Error por email inválido

Error por categoría inválida

Edición de cliente

Eliminación confirmada

Persistencia correcta en JSON

Registro de logs

Capturas disponibles en carpeta docs/.

## 📊 Diagrama UML

El proyecto incluye:

Archivo uml_abp4_gc.puml

Imagen uml_abp4_gc.png

Se representan:

Clases

Herencia

Dependencias entre capas

Jerarquía de excepciones

## 🚀 Posibles mejoras futuras

Agregar nivel INFO al logger (registro de operaciones exitosas)

Implementar pruebas unitarias automatizadas

Agregar interfaz gráfica

Migrar persistencia a base de datos relacional

Implementar patrón Factory más explícito

Separar configuración en archivo externo

## 🎯 Objetivo académico

Este proyecto integra los contenidos trabajados en:

Programación orientada a objetos

Herencia y polimorfismo

Manejo avanzado de excepciones

Manejo de archivos

Persistencia de datos

Organización modular del código

---

## 👩‍💻 Autora

Belén Zambrano  
Proyecto desarrollado como parte del ABP4 – Programación Orientada a Objetos.
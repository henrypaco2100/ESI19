# ESI Agente IA para Odoo 19

Aplicación independiente con menús de Ventas, Compras, Inventario, Importación, Fabricación, POS, Contabilidad, Tablero, Informe y Ajustes. Cada consulta queda registrada con respuesta, estado, usuario, compañía, modelo, tokens y duración. El tablero usa gráfico y tabla dinámica; Informe abre una tabla dinámica por mes y área.

## Instalación

1. Copiar `Esi_Agenteia_v19` a un directorio incluido en `addons_path` de Odoo 19.
2. Actualizar la lista de aplicaciones e instalar **ESI Agente IA**.
3. En Usuarios, asignar el grupo **Usuario Agente IA** o **Responsable Agente IA**. El responsable puede revisar las interacciones de sus compañías permitidas.
4. Un administrador abre Agente IA > Ajustes, introduce su clave de API de OpenAI, el nombre de un modelo disponible para su cuenta y guarda.
5. Crear una consulta en cualquiera de las siete áreas y pulsar **Consultar agente IA**.

La clave queda en `ir.config_parameter` y solo un administrador puede abrir el menú de Ajustes. La aplicación llama a `POST https://api.openai.com/v1/responses` con `store=false`. El contenido de la consulta se envía al proveedor al pulsar el botón. No lee automáticamente documentos de Odoo, no crea ventas/compras/asientos y no ejecuta herramientas de negocio. Las áreas organizan las conversaciones y ajustan las instrucciones del asistente. Para integrar datos y acciones de cada módulo se requieren conectores específicos posteriores.

## Requisitos

El servidor Odoo debe tener salida HTTPS hacia `api.openai.com`. No se requiere paquete Python externo; utiliza `urllib` de la biblioteca estándar. Se validó sintaxis Python, XML y referencias locales; falta prueba de instalación en un servidor Odoo 19 real.

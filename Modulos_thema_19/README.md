# ESI Theme Suite v19 - V2

Version corregida para Odoo 19 Community.

## Cambios clave frente a V1

- Eliminado `web._assets_primary_variables` del theme ESI.
- Eliminados los SCSS propios del ESI Theme; los estilos ahora son CSS puro.
- Eliminada la sustitucion OWL completa de `web.NavBar.AppsMenu`, que podia competir con MuK.
- Corregido el xpath del login de Odoo 19: `o_database_list` vive en `t-attf-class`.
- Agregada capa opcional `esi_theme_muk_compat_v19` que depende de `muk_web_theme` y se carga despues de MuK.
- Agregado metapaquete `esi_theme_suite_muk_v19` para instalaciones que usan MuK.

## Modulos

- `esi_theme_core_v19`: backend/base visual ESI.
- `esi_theme_login_v19`: login ESI y recuperación de contraseña via `auth_signup`.
- `esi_theme_mail_v19`: Chatter/Discuss.
- `esi_theme_muk_compat_v19`: acabado ESI sobre MuK 19 (opcional; requiere MuK).
- `esi_theme_suite_v19`: instala ESI sin requerir MuK.
- `esi_theme_suite_muk_v19`: instala suite ESI + capa MuK; requiere que los modulos MuK esten disponibles en addons.

## Que instalar

### Si NO usas MuK
Instala `ESI Theme Suite v19`.

### Si SI usas MuK
Instala/actualiza MuK 19 y luego instala `ESI Theme Suite + MuK v19`.

No instales versiones viejas V1 mezcladas con estos archivos.

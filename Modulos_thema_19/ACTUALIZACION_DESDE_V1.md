# Actualizar desde ESI Theme V1

1. Sustituye completamente las carpetas `esi_theme_*` de V1 por las de V2.
2. Reinicia Odoo.
3. Actualiza la lista de aplicaciones.
4. Actualiza `esi_theme_core_v19`, `esi_theme_login_v19`, `esi_theme_mail_v19` y el metapaquete.
5. Si usas MuK, instala `esi_theme_muk_compat_v19` o `esi_theme_suite_muk_v19`.
6. Fuerza recarga del navegador (`Ctrl+Shift+R`).

## Docker

Ejemplo de reinicio:

```bash
cd /opt/odoo19
docker compose restart odoo01
```

## Diagnostico de assets

```bash
docker logs --tail 200 odoo19_01 | grep -Ei "asset|scss|css|error|traceback"
```

La V2 no incluye SCSS ESI, por lo que un error de compilacion SCSS posterior debe revisarse en otro modulo/theme (por ejemplo MuK o personalizaciones adicionales).

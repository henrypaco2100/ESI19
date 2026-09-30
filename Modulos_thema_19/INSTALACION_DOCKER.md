# Instalación en Docker - Odoo 19

Ejemplo para un contenedor llamado `odoo19_01`.

1. Copiar los módulos al repositorio/directorio de addons personalizados que ya esté montado en el contenedor.
2. Confirmar que las carpetas queden visibles desde el contenedor.
3. Reiniciar Odoo:

```bash
docker restart odoo19_01
```

4. En Odoo: activar modo desarrollador → Aplicaciones → Actualizar lista de aplicaciones.
5. Buscar **ESI Theme Suite v19** e instalar.

## Si los estilos no cambian inmediatamente

Abre una vez con:

```text
/web?debug=assets
```

Haz recarga forzada del navegador (`Ctrl+Shift+R`). Luego vuelve a la URL normal.

## Actualización por línea de comandos

Si conoces la base de datos y el binario/configuración del contenedor, también puedes ejecutar una actualización de módulos con `-u esi_theme_suite_v19`, pero el comando exacto depende de cómo esté definido tu `compose.yaml` y tu `odoo.conf`.

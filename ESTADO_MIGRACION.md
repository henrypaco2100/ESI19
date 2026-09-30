# Migración ESI a Odoo 19 — borrador de trabajo

Este archivo conserva los 27 módulos de ESI para completar una migración gradual. **No instalar en una base de producción ni considerar los módulos validados.**

## Cambios aplicados

- Se incorporó `esi_produccion_report_v13` al grupo `ESI_REPORTES`.
- Se ajustaron las versiones de los manifiestos a 19.0 y se convirtieron vistas `tree` a `list`, `attrs` y `states` a expresiones de vistas modernas.
- Se eliminó la escritura SQL que alteraba `stock_valuation_layer.create_date` durante el reproceso. Se conservaron los rangos de fechas de los reportes.
- Se inició la adaptación de los flujos de ventas y compras automatizadas: `move_type` de facturas, `move_ids` de transferencias, cantidad de movimientos y creación nativa de factura de proveedor.
- La comprobación estática encontró 27 manifiestos, archivos de datos presentes, Python compilable y XML bien formado.

## Trabajo pendiente para instalación en Odoo 19

1. Reescribir `esi_sd_stock_valuation_layer`: usa métodos internos, campos, cálculos de quants y capas de valoración de Odoo 13. No se debe instalar aún.
2. Adaptar el kardex y reportes de producción a `stock.move.line.quantity` y al modelo de valoración de Odoo 19.
3. Adaptar cinco archivos JavaScript heredados al cliente web de Odoo 19 y mover los assets a los manifiestos.
4. Revisar las vistas heredadas contra los IDs y estructura reales de Odoo 19; la validez XML no verifica el XPath de Odoo.
5. Revisar modelos contables, POS, fabricación, multisucursal y pagos con pruebas de instalación y flujos reales.
6. Ejecutar instalaciones por dependencias en base nueva Odoo 19 y pruebas funcionales. No se tuvo un servidor Odoo 19 disponible en este entorno.

La fecha del pedido puede ser anterior; la validación de transferencia y la capa de valoración deben seguir la fecha efectiva estándar de Odoo, sin reescribir `create_date`.

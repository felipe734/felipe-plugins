# Catálogo de Felipe OS

Registro único de las skills de Felipe OS, el sistema personal de Felipe Tobar. `felipe-os` lo lee al integrar skills; lo que no está aquí no existe para Felipe OS. Al agregar, retirar o renombrar una skill, actualiza este archivo.

Felipe OS escribe por ahora en la **TRAZABILIDAD de Verse** (base 9. VERSE OS `appylcO9bGU5EBgV2`, tabla `tblXVY1dEl79x3uVW`), siempre con Línea `Personal`; la tabla propia queda para después (decisión del 7 nov 2026). Usa tres skills del plugin `verse`: `verse-trazabilidad`, `os-correo` y `verse-marca`. No tiene brief propio ni tareas programadas: lo personal sale en el bloque PERSONAL del brief de Verse (`verse-brief-diario`), y la depuración diaria de la tabla la hace Verse OS · Diario; `felipe-os` solo depura sus propios duplicados cuando Felipe lo corre.

## Mapa

| Skill / proceso | Proceso en TRAZABILIDAD | Línea | Frecuencia | Quién la dispara | Tipo |
|---|---|---|---|---|---|
| felipe-os | Felipe OS | Personal | A pedido | Felipe ("felipe-os", "qué tengo personal", "revisa mi correo personal") | Motor: pendientes personales, actividades FELIPE, correo del OS felipe; solo escribe Pendientes y su Corrida con Línea Personal |
| ↳ correo personal (vía `os-correo` os=felipe) | Correo (o Felipe recurrentes si es el cobro de una actividad) | Personal | Cada corrida de felipe-os en modo ejecutar | felipe-os | Pendientes con Link al hilo y Ref externa el threadId |
| felipe-recurrentes | Felipe recurrentes | Personal | Mensual, día 28 (reintento hasta fin de mes) | Verse OS · Diario (la despacha desde este plugin) y Felipe en conversación | Automático: proyecta RECURRENTES de la base FELIPE |
| felipe-gym | — (sin Corrida; Pendiente Manual solo si falla una escritura) | Personal | Por sesión de gimnasio | Felipe en conversación ("hoy día X", "registra gym", "cómo voy en el gym") | Registro: filas en GYM de la base FELIPE |

## Lo que sigue en el plugin `verse` (no se copia aquí)

| Skill / proceso | Dónde vive | Relación con Felipe OS |
|---|---|---|
| verse-brief-diario, bloque PERSONAL | plugin `verse` | Muestra cada mañana los Pendientes Línea Personal, RECURRENTES de la base FELIPE y el correo del OS felipe; es el brief de Felipe OS |
| os-correo | plugin `verse` | Lee las seis cuentas y devuelve a felipe-os solo las colas personal, finanzas y sistema (sección 4 de `ruteo.md`). SVMG queda en Verse (regla C10) |
| verse-trazabilidad | plugin `verse` | Registro, cierre y checks; Felipe OS usa la tabla de Verse con Línea Personal |

La base FELIPE (8 nov 2026) es la base propia de Felipe OS para datos personales; la tabla FELIPE de 9. VERSE OS (`tbl9M7iHSs3xVMiU3`) quedó en desuso.

Procesos que Felipe OS escribe en TRAZABILIDAD: Felipe OS, Correo, Felipe recurrentes, Manual. `Felipe OS` puede no existir todavía como opción del campo Proceso (`fldGUOALzCds6je18`): se escribe con `typecast: true` y, si falla, con `Manual`.

## Tareas programadas

Ninguna. Felipe OS corre solo a pedido. Si algún día se programa, el prompt vive en `references/tareas/` y se agrega aquí, siguiendo el formato de `cc-os/references/tareas/cc-os-diario.md`.

## Tablas que Felipe OS lee

| Base | Tabla | Para qué |
|---|---|---|
| 9. VERSE OS `appylcO9bGU5EBgV2` | TRAZABILIDAD `tblXVY1dEl79x3uVW` | Pendientes y Corrida con Línea Personal (lectura y escritura) |
| FELIPE `appJP5HcHMyhPRdcA` (workspace 1. C&C) | RECURRENTES `tblgowyhDZzl8hDe9` | Actividades personales; felipe-recurrentes escribe, felipe-os lee |
| FELIPE `appJP5HcHMyhPRdcA` | GYM `tblbKKuwaOjYL4DL0` | Sesiones de gimnasio; solo felipe-gym |
| Correo por Composio (cuenta `felipe-personal` `gmail_codist-plass`, jtobar1998@gmail.com, más lo ruteado a `felipe` desde las otras cinco) | — | A través de `os-correo` os=felipe; solo lectura; nunca envía |

## Cómo se integra una skill nueva (checklist obligatorio)

1. **Prefijo `felipe-`**, nombre corto en español, `model:` en el frontmatter (haiku, sonnet u opus con el criterio de Verse).
2. **Proceso.** Si es nuevo, agrégalo como opción del campo Proceso de TRAZABILIDAD de Verse (`fldGUOALzCds6je18`), a la fórmula del campo Área y a la lista de `verse-trazabilidad` (PR en verse-plugins en el mismo paquete).
3. **Registro.** Sección "Registro en TRAZABILIDAD (obligatorio)" con `verse-trazabilidad`, Línea `Personal`.
4. **Relaciones.** Sección "Cómo se engrana en Felipe OS": qué lee, quién la dispara, quién lee lo que deja.
5. **Catálogo.** Fila en el Mapa y, si lee una tabla nueva, en "Tablas que Felipe OS lee". Si el brief de Verse debe mostrar lo que deja, PR en verse-plugins para el bloque PERSONAL de `verse-brief-diario`.
6. **Correo.** Solo vía `os-correo` (cuenta `felipe-personal`, solo lectura) y `verse-marca`; nunca `mcp__Gmail__*`. La cuenta personal nunca envía nada de negocio. Sin correo aparte a Felipe: va a TRAZABILIDAD y el brief de Verse lo muestra.
7. **Datos.** Sin cifras, saldos, datos de salud ni números de cuenta en el repositorio ni en TRAZABILIDAD.
8. **SKILLS.** Fila en SKILLS (1. VL PRIVADO `appLgl0G3iW4tdQFp`, `tblG7pA9lUGWiCez5`) con Categoría Personal.
9. **Validador.** `python3 plugins/felipe/scripts/validar_skills.py --base origin/main` en verde.
10. **Repositorio.** Rama `claude/<tema>` → versión subida en `plugins/felipe/.claude-plugin/plugin.json` → conteo del README → PR a `main`.

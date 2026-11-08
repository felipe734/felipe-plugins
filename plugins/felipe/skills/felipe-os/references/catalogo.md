# Catálogo de Felipe OS

Registro único de las skills de Felipe OS, el sistema personal de Felipe Tobar. `felipe-os` lo lee al integrar skills; lo que no está aquí no existe para Felipe OS. Al agregar, retirar o renombrar una skill, actualiza este archivo.

Felipe OS es independiente de Verse OS desde el 8 nov 2026: sus datos y su registro viven en la base FELIPE (`appJP5HcHMyhPRdcA`, workspace 1. C&C), tiene su propia skill de registro (`felipe-trazabilidad`) y su propia tarea programada. Del plugin `verse` solo usa `os-correo`, el receptor único de correo de los tres OS, en solo lectura. El brief de Verse lee la base FELIPE en solo lectura para su bloque PERSONAL; Felipe OS no depende de él.

## Mapa

| Skill / proceso | Proceso en TRAZABILIDAD | Frecuencia | Quién la dispara | Tipo |
|---|---|---|---|---|
| felipe-os | Felipe OS | A pedido | Felipe ("felipe-os", "qué tengo personal", "revisa mi correo personal") | Motor: pendientes personales, recurrentes vencidas y correo del OS felipe |
| ↳ correo personal (vía `os-correo` os=felipe) | Correo (o Felipe recurrentes si es el cobro de una actividad) | Cada corrida de felipe-os en modo ejecutar | felipe-os | Pendientes con Link al hilo y Ref externa el threadId |
| felipe-trazabilidad | — (es el registro) | Cada corrida de una skill felipe- | Las demás skills felipe-; Felipe ("listo", "qué tengo pendiente personal") | Base: Corridas y Pendientes en la TRAZABILIDAD de la base FELIPE |
| felipe-recurrentes | Felipe recurrentes | Mensual, días 28 a 31 | Tarea Felipe OS · Recurrentes; Felipe en conversación | Automático: proyecta RECURRENTES del mes siguiente |
| felipe-gym | — (sin Corrida; Pendiente Felipe gym solo si falla una escritura) | Por sesión de gimnasio | Felipe ("hoy día X", "registra gym", "cómo voy en el gym") | Registro: filas en GYM |

## Lo que se comparte con el plugin `verse`

| Pieza | Dónde vive | Relación con Felipe OS |
|---|---|---|
| os-correo | plugin `verse` | Lee las seis cuentas y devuelve a felipe-os solo las colas personal, finanzas y sistema (sección 4 de `ruteo.md`). SVMG queda en Verse (regla C10). Solo lectura |
| verse-brief-diario, bloque PERSONAL | plugin `verse` | Lee en solo lectura la TRAZABILIDAD y RECURRENTES de la base FELIPE. Opcional: si no corre, Felipe OS sigue igual |

Procesos que Felipe OS escribe en su TRAZABILIDAD: Felipe OS, Felipe recurrentes, Felipe gym, Correo, Manual. Uno nuevo se escribe con `typecast: true` y se agrega aquí y en `PROCESOS_FELIPE` del validador.

## Tareas programadas

| Tarea | Horario | Skill | Prompt |
|---|---|---|---|
| Felipe OS · Recurrentes | Días 28 a 31, 7:11 (Bogotá) | felipe-recurrentes | `references/tareas/felipe-os-recurrentes.md` |

El prompt del archivo es la fuente de verdad: si se cambia la tarea, se cambia primero aquí.

## Tablas de Felipe OS

| Base | Tabla | Para qué |
|---|---|---|
| FELIPE `appJP5HcHMyhPRdcA` | TRAZABILIDAD `tbl6LcSWFXUCH8dqs` | Corridas y Pendientes personales (solo `felipe-trazabilidad` escribe) |
| FELIPE `appJP5HcHMyhPRdcA` | RECURRENTES `tblgowyhDZzl8hDe9` | Actividades personales; felipe-recurrentes escribe, felipe-os lee |
| FELIPE `appJP5HcHMyhPRdcA` | GYM `tblbKKuwaOjYL4DL0` | Sesiones de gimnasio; solo felipe-gym |
| Correo por Composio (cuenta `felipe-personal` `gmail_codist-plass`, jtobar1998@gmail.com, más lo ruteado a `felipe` desde las otras cinco) | — | A través de `os-correo` os=felipe; solo lectura; nunca envía |

La tabla FELIPE de 9. VERSE OS (`tbl9M7iHSs3xVMiU3`) se borró el 8 nov 2026 y la TRAZABILIDAD de Verse ya no recibe filas con Línea Personal.

## Cómo se integra una skill nueva (checklist obligatorio)

1. **Prefijo `felipe-`**, nombre corto en español, `model:` en el frontmatter (haiku, sonnet u opus).
2. **Proceso.** Si es nuevo, agrégalo a la lista de arriba, a `felipe-trazabilidad` y a `PROCESOS_FELIPE` del validador.
3. **Registro.** Sección "Registro en TRAZABILIDAD" con `felipe-trazabilidad`.
4. **Relaciones.** Sección "Cómo se engrana en Felipe OS": qué lee, quién la dispara, quién lee lo que deja.
5. **Catálogo.** Fila en el Mapa y, si usa una tabla nueva, en "Tablas de Felipe OS". Si tiene tarea programada, fila en "Tareas programadas" y su prompt en `references/tareas/`.
6. **Correo.** Solo lectura vía `os-correo`; nunca `mcp__Gmail__*`. Felipe OS no envía correo.
7. **Datos.** Sin cifras, saldos, datos de salud ni números de cuenta en el repositorio ni en TRAZABILIDAD.
8. **SKILLS.** Fila en SKILLS (1. VL PRIVADO `appLgl0G3iW4tdQFp`, `tblG7pA9lUGWiCez5`) con Categoría Personal.
9. **Validador.** `python3 plugins/felipe/scripts/validar_skills.py --base origin/main` en verde.
10. **Repositorio.** Rama `claude/<tema>` → versión subida en `plugins/felipe/.claude-plugin/plugin.json` → conteo del README → PR a `main`.

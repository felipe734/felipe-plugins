# Calendario de Verse OS

Zona horaria: America/Bogota (UTC-5, sin horario de verano). Toda fecha se calcula en hora de Bogotá.

## Festivos nacionales de Colombia

Ley Emiliani (Ley 51 de 1983). Fijos: 1 ene, 1 may, 20 jul, 7 ago, 8 dic, 25 dic. Trasladables al lunes siguiente: 6 ene, 19 mar, 29 jun, 15 ago, 12 oct, 1 nov, 11 nov. Ligados a Pascua: Jueves y Viernes Santo; Ascensión (Pascua + 43), Corpus Christi (+64), Sagrado Corazón (+71).

| Año | Festivos |
|---|---|
| 2026 | 1 ene, 12 ene, 23 mar, 2 abr, 3 abr, 1 may, 18 may, 8 jun, 15 jun, 29 jun, 20 jul, 7 ago, 17 ago, 12 oct, 2 nov, 16 nov, 8 dic, 25 dic |
| 2027 | 1 ene, 11 ene, 22 mar, 25 mar, 26 mar, 1 may, 10 may, 31 may, 7 jun, 5 jul, 20 jul, 7 ago, 16 ago, 18 oct, 1 nov, 15 nov, 8 dic, 25 dic |

Para años posteriores a 2027, calcúlalos con las reglas de arriba y, si hay duda, verifícalos en la web antes de decidir.

## Definiciones

- **Día hábil:** lunes a viernes que no sea festivo. El sábado no es día hábil para el cierre, aunque Edy trabaje media jornada.
- **DHn:** el n-ésimo día hábil del mes calendario. Ejemplo noviembre 2026: el 2 es festivo, así que DH1 = martes 3, DH2 = miércoles 4, DH3 = jueves 5, DH4 = viernes 6, DH5 = lunes 9.
- **Mes a cerrar (M):** el mes calendario anterior al actual, en formato YYYY-MM.
- **"Día X o el siguiente hábil":** si el día X del mes cae en sábado, domingo o festivo, se corre el siguiente día hábil. Ejemplo: día 15 de noviembre 2026 es domingo y el 16 es festivo, así que corre el martes 17.
- **Ventanas para la regla de un disparo:** "hoy" = fecha de Bogotá; "esta semana" = lunes a domingo actual; "este mes" = mes calendario actual.

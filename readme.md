Este proyecto tiene como objetivo identificar qué áreas concentran la mayor proporción del presupuesto de las licitaciones incluidas en el seguimiento de la SSTEDU.

Importante: los importes utilizados son ficticios y fueron establecidos con fines académicos para practicar cálculos y visualizaciones.

Problema de negocio

El seguimiento de compras y contrataciones contiene registros sin presupuesto informado y procesos con diferentes estados administrativos.

Esto dificulta identificar rápidamente qué áreas deberían revisarse primero.

Herramientas utilizadas:
- Python
- pandas
- Visual Studio Code
- Microsoft Excel como fuente de referencia
- PowerPoint para la presentación ejecutiva

Metodología:

Se aplicó CRISP-DM para comprender el problema, revisar la estructura de los datos, delimitar el análisis, calcular indicadores y comunicar resultados.

El trabajo se organizó en dos sprints:

Sprint 1: identificación de la hoja, definición del alcance y exclusión de registros sin presupuesto.

Sprint 2: ejecución del código Python con valores simulados, análisis de porcentajes y presentación de resultados.

Alcance: 
Se consideraron las filas 1 a 20 de la hoja «Seguimiento Procesos SSTES». De 18 procesos revisados, 9 tenían presupuesto informado y 9 fueron excluidos del análisis monetario.

Cómo ejecutar el proyecto:

- Instalar Python.

- Instalar pandas desde la terminal:

- python -m pip install pandas

- Descargar el archivo Preentrega3.py.

- Abrirlo en Visual Studio Code.

- Ejecutar: python Preentrega3.py

El programa mostrará los presupuestos ficticios y la participación porcentual de cada área.

Limitaciones: 

El script utiliza importes simulados cargados manualmente y no lee directamente el archivo Excel. No se verificaron adjudicaciones, precios de mercado ni montos ejecutados.

Próximos pasos:

Automatizar la lectura del Excel, validar los estados administrativos y utilizar importes oficiales autorizados para profundizar el análisis.

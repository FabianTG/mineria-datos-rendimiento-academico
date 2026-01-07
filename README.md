# Proyecto: Minería de Datos con IA – De la pregunta al insight

## 1. Objetivo y Pregunta Central
El objetivo de este proyecto es identificar los factores que más influyen en el rendimiento académico (nota final G3) de los estudiantes de secundaria.
**Pregunta central:** ¿Cómo afectan las variables socio-ambientales y el comportamiento de estudio al éxito académico?

## 2. Fuente de los Datos y Proceso de Limpieza

Los datos utilizados provienen del dataset **Student Performance** del repositorio UCI Machine Learning, el cual recopila información de estudiantes de secundaria en Portugal. El conjunto de datos final consta de **395 registros**, cumpliendo con la restricción de tamaño para este análisis.

El proceso de preparación incluyó la verificación de integridad, confirmando que no existían valores nulos ni registros duplicados. Se realizaron transformaciones específicas como la normalización de las ausencias para generar una tasa de asistencia teórica y la codificación de variables categóricas binarias a formato numérico. Finalmente, se aplicó una estandarización de características para asegurar que el algoritmo de clustering no se viera sesgado por las diferentes escalas de las variables.

## 3. Técnicas de Minería de Datos Aplicadas

Para abordar el problema, se implementaron dos enfoques complementarios utilizando la librería **scikit-learn**. En primer lugar, se aplicó una **Regresión Lineal** para predecir la calificación final (G3). Este modelo demostró una alta capacidad predictiva con un coeficiente de determinación **R² de 0.78**, destacando que el rendimiento pasado y el historial de fallos son los factores más determinantes.

En segundo lugar, se utilizó el algoritmo **K-Means** para segmentar a los estudiantes en tres perfiles diferenciados basados en su comportamiento y entorno social. Los resultados de esta segmentación se resumen en la siguiente tabla:

| Perfil de Estudiante | Características Principales | Rendimiento Promedio (G3) |
| :--- | :--- | :--- |
| **Cluster 0: Enfocados** | Alto tiempo de estudio y bajo consumo de alcohol. | 10.90 |
| **Cluster 1: Sociales** | Alta frecuencia de salidas y consumo social de alcohol. | 10.65 |
| **Cluster 2: En Riesgo** | Elevado índice de fallos previos y bajo tiempo de estudio. | 5.75 |

## 4. Resultados y Conclusiones

El análisis revela que el **historial de fallos previos** es el predictor negativo más potente del éxito académico actual. Esto sugiere que las dificultades de aprendizaje tienden a ser acumulativas si no se intervienen a tiempo. Por otro lado, se observó una correlación positiva moderada entre la calidad de las **relaciones familiares** y el rendimiento, subrayando la importancia del entorno emocional del estudiante.

Curiosamente, el consumo de alcohol durante los fines de semana no mostró un impacto negativo tan directo en las calificaciones finales como se hipotetizó inicialmente, siempre que el tiempo de estudio se mantuviera constante. Sin embargo, los estudiantes en el perfil "En Riesgo" presentan una combinación de factores que los aleja significativamente del promedio, requiriendo atención prioritaria.

## 5. Limitaciones y Recomendaciones Futuras
- **Limitaciones:** El dataset es pequeño (395 filas), lo que puede limitar la generalización.
- **Recomendaciones:** Para futuros estudios, se sugiere incluir variables sobre salud mental y uso de tecnologías digitales para profundizar en los patrones de distracción.

---
*Proyecto desarrollado con asistencia de IA (Manus) - 2026*

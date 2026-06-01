# Minería de Datos e Inteligencia Artificial: De la Pregunta al Insight
## Análisis de Factores de Rendimiento Académico en Estudiantes de Secundaria

Este repositorio contiene un proyecto completo de **Minería de Datos y Ciencia de Datos** aplicado al ámbito educativo. El objetivo principal es identificar y modelar los factores socio-ambientales, familiares y de comportamiento que influyen de manera más determinante en el rendimiento académico final (calificación G3) de los estudiantes.

El proyecto está diseñado bajo un enfoque metodológico riguroso, aplicando técnicas de **aprendizaje supervisado (Regresión Lineal)** y **no supervisado (Clustering con K-Means)** sobre el conjunto de datos de rendimiento escolar de Portugal (UCI Machine Learning Repository).

---

## 📋 Estructura del Repositorio

El proyecto se organiza de forma modular y reproducible:

```
DataMiningIA_FabianTorres/
├── README.md                 # Documentación técnica principal
├── definicion_problema.md    # Formulación del problema e hipótesis iniciales
├── resultados_analisis.json  # Métricas y coeficientes reales del modelo
├── Video explicativo         # Enlace a la presentación interactiva del proyecto
├── data/
│   └── student-mat.csv       # Dataset original (395 registros, 33 variables)
├── data_clean/
│   ├── student_clean.csv     # Dataset preprocesado y normalizado
│   └── student_with_clusters.csv # Dataset etiquetado con los perfiles de K-Means
├── scripts/
│   ├── limpieza_datos.py     # Pipeline de ETL y preprocesamiento de datos
│   ├── analisis_mineria.py   # Modelamiento matemático (Regresión y Clustering)
│   └── visualizacion.py      # Generación automatizada de gráficos de análisis
└── visualizaciones/
    ├── distribucion_notas.png # Distribución de la variable objetivo (G3)
    ├── mapa_correlacion.png  # Matriz de correlación de Pearson
    ├── notas_por_cluster.png # Comparativa de rendimiento por perfil de estudiante
    └── estudio_vs_nota.png   # Relación entre horas de estudio y calificación final
```

---

## 🛠️ Pipeline de Datos y Metodología

### 1. Extracción, Transformación y Carga (ETL)
El script `limpieza_datos.py` realiza el preprocesamiento de los datos de forma robusta y portable:
*   **Integridad de Datos**: Verificación de ausencia de valores nulos y registros duplicados.
*   **Ingeniería de Características (Feature Engineering)**: Creación de la métrica `attendance_rate` (tasa de asistencia teórica) a partir de las ausencias reportadas.
*   **Codificación de Variables**: Transformación de variables cualitativas binarias (ej. acceso a internet, apoyo familiar, actividades extracurriculares) a formato numérico binario `(0, 1)`.
*   **Portabilidad**: Uso de rutas relativas dinámicas (`os.path`) para garantizar que el código se ejecute correctamente en cualquier máquina.

### 2. Modelamiento Matemático y Minería de Datos
El script `analisis_mineria.py` implementa dos técnicas fundamentales utilizando **scikit-learn**:

#### A. Aprendizaje Supervisado: Regresión Lineal (Predicción de G3)
*   **Corrección de Target Leakage**: Se excluyeron las calificaciones parciales `G1` y `G2` de las variables predictoras. Esto evita la "fuga de datos del objetivo" (un error común en ciencia de datos donde las notas intermedias inflan artificialmente el R² a 0.78, pero hacen que el modelo sea inútil para predecir de forma temprana).
*   **Rendimiento del Modelo Real**: El modelo alcanza un $R^2 \approx 0.12$, lo cual es estadísticamente coherente y realista para predicciones basadas puramente en factores socio-ambientales previos.
*   **Factores Clave Identificados (Coeficientes)**:
    *   **Historial de fallos previos (`failures`)**: Coeficiente de **-1.94**. Es el predictor negativo más potente del rendimiento. Cada fallo académico acumulado reduce la nota final en casi 2 puntos.
    *   **Tiempo de estudio semanal (`studytime`)**: Coeficiente de **+0.50**. Factor positivo directo para el rendimiento.
    *   **Educación de la madre (`Medu`)**: Coeficiente de **+0.63**. El nivel educativo del entorno materno es el predictor de apoyo socio-familiar más fuerte.
    *   **Frecuencia de salidas con amigos (`goout`)**: Coeficiente de **-0.48**. Un exceso de salidas sociales impacta negativamente el desempeño.

#### B. Aprendizaje No Supervisado: Segmentación con K-Means
Se agruparon los estudiantes en **3 perfiles o clusters diferenciados** basados en su comportamiento y entorno social (tiempo de estudio, fallos previos, tiempo libre, salidas con amigos y consumo de alcohol):

| Perfil de Estudiante | Características Principales (Medias) | Rendimiento Promedio (G3) |
| :--- | :--- | :--- |
| **Cluster 0: Enfocados** | Alto tiempo de estudio, bajísimo índice de fallos (0.12), bajo consumo de alcohol y salidas moderadas. | **10.90** |
| **Cluster 1: Sociales** | Tiempo de estudio moderado, salidas frecuentes, alto consumo de alcohol en fines de semana (3.77/5). | **10.65** |
| **Cluster 2: En Riesgo** | Elevadísimo índice de fallos previos (2.50), bajo tiempo de estudio, alta disponibilidad de tiempo libre. | **5.75** |

---

## 📈 Visualizaciones Clave

Las gráficas generadas automáticamente en la carpeta `visualizaciones/` revelan insights profundos:
*   **`mapa_correlacion.png`**: Muestra que, si bien las calificaciones parciales `G1` y `G2` están altamente correlacionadas con `G3` (0.80+), las variables socio-ambientales como `failures` (-0.36) y `Medu` (+0.22) tienen correlaciones lineales significativas y directas.
*   **`notas_por_cluster.png`**: Evidencia de forma gráfica la brecha de rendimiento del **Cluster 2 (En Riesgo)**, cuya mediana de calificaciones se encuentra por debajo de la línea de aprobación (10), mientras que los Clusters 0 y 1 muestran distribuciones saludables y similares.

---

## 🚀 Cómo Ejecutar el Proyecto

1.  **Requisitos Previos**: Asegúrate de tener instalado Python 3 y las librerías necesarias:
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn
    ```
2.  **Ejecución del Pipeline**: Ejecuta los scripts en orden secuencial desde la raíz del repositorio:
    ```bash
    python scripts/limpieza_datos.py
    python scripts/analisis_mineria.py
    python scripts/visualizacion.py
    ```
    Los scripts actualizarán automáticamente los datos limpios, el archivo JSON de resultados y todas las gráficas en la carpeta `visualizaciones/`.

---
*Proyecto de grado desarrollado con rigor científico y metodológico - 2026*

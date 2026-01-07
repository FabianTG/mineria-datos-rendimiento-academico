import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import json

# Cargar datos limpios
df = pd.read_csv('/home/ubuntu/proyecto_mineria/data_clean/student_clean.csv')

# --- TÉCNICA 1: REGRESIÓN LINEAL (Predecir G3 - Nota Final) ---
# Seleccionamos variables numéricas relevantes
features_reg = ['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 
                'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2']
X = df[features_reg]
y = df['G3']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_reg = LinearRegression()
model_reg.fit(X_train, y_train)
y_pred = model_reg.predict(X_test)

reg_results = {
    "mse": mean_squared_error(y_test, y_pred),
    "r2": r2_score(y_test, y_pred),
    "coefficients": dict(zip(features_reg, model_reg.coef_))
}

# --- TÉCNICA 2: CLUSTERING (Agrupar estudiantes por comportamiento) ---
# Variables de comportamiento: tiempo de estudio, fallos, tiempo libre, salidas, consumo alcohol
features_cluster = ['studytime', 'failures', 'freetime', 'goout', 'Dalc', 'Walc']
X_cluster = df[features_cluster]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_cluster)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Resumen de clusters
cluster_summary = df.groupby('cluster')[features_cluster + ['G3']].mean().to_dict()

# Guardar resultados para el informe
results = {
    "regresion": reg_results,
    "clustering": cluster_summary
}

with open('/home/ubuntu/proyecto_mineria/resultados_analisis.json', 'w') as f:
    json.dump(results, f, indent=4)

# Guardar dataset con clusters
df.to_csv('/home/ubuntu/proyecto_mineria/data_clean/student_with_clusters.csv', index=False)

print("Análisis completado. Resultados guardados en resultados_analisis.json")

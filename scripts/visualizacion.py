import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de estilo
sns.set_theme(style="whitegrid")
os.makedirs('/home/ubuntu/proyecto_mineria/visualizaciones', exist_ok=True)

# Cargar datos con clusters
df = pd.read_csv('/home/ubuntu/proyecto_mineria/data_clean/student_with_clusters.csv')

# 1. Histograma de Notas Finales (G3)
plt.figure(figsize=(10, 6))
sns.histplot(df['G3'], bins=20, kde=True, color='skyblue')
plt.title('Distribución de Calificaciones Finales (G3)')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.savefig('/home/ubuntu/proyecto_mineria/visualizaciones/distribucion_notas.png')
plt.close()

# 2. Correlación entre variables clave
plt.figure(figsize=(12, 10))
cols_corr = ['age', 'studytime', 'failures', 'absences', 'G1', 'G2', 'G3', 'attendance_rate']
sns.heatmap(df[cols_corr].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor de Correlaciones')
plt.savefig('/home/ubuntu/proyecto_mineria/visualizaciones/mapa_correlacion.png')
plt.close()

# 3. Boxplot de Notas por Cluster
plt.figure(figsize=(10, 6))
sns.boxplot(x='cluster', y='G3', data=df, palette='Set2')
plt.title('Calificaciones Finales por Cluster de Estudiantes')
plt.xlabel('Cluster')
plt.ylabel('G3')
plt.savefig('/home/ubuntu/proyecto_mineria/visualizaciones/notas_por_cluster.png')
plt.close()

# 4. Relación entre Tiempo de Estudio y Nota Final
plt.figure(figsize=(10, 6))
sns.regplot(x='studytime', y='G3', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relación: Tiempo de Estudio vs Nota Final')
plt.xlabel('Tiempo de Estudio (1-4)')
plt.ylabel('G3')
plt.savefig('/home/ubuntu/proyecto_mineria/visualizaciones/estudio_vs_nota.png')
plt.close()

print("Visualizaciones generadas en /home/ubuntu/proyecto_mineria/visualizaciones/")

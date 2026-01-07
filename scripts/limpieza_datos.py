import pandas as pd
import os

# Crear directorio para datos limpios
os.makedirs('/home/ubuntu/proyecto_mineria/data_clean', exist_ok=True)

# Cargar el dataset (el separador es coma en esta versión del archivo)
df = pd.read_csv('/home/ubuntu/proyecto_mineria/data/student-mat.csv')

# 1. Identificar valores faltantes y duplicados
missing_values = df.isnull().sum().sum()
duplicates = df.duplicated().sum()

print(f"Valores faltantes: {missing_values}")
print(f"Duplicados: {duplicates}")

# 2. Normalizar/Estandarizar variables
# Crearemos una variable 'attendance_rate' basada en 'absences'
# El máximo de ausencias en este dataset suele ser alrededor de 93
max_absences = df['absences'].max()
if max_absences == 0: max_absences = 1 # Evitar división por cero
df['attendance_rate'] = 1 - (df['absences'] / 100) # Usamos 100 como base teórica de días

# 3. Corregir formatos
# Convertir variables binarias a numéricas para facilitar el análisis
binary_cols = ['schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']
for col in binary_cols:
    if col in df.columns:
        df[col] = df[col].map({'yes': 1, 'no': 0})

# 4. Guardar versión limpia
df.to_csv('/home/ubuntu/proyecto_mineria/data_clean/student_clean.csv', index=False)
print("Dataset limpio guardado en /home/ubuntu/proyecto_mineria/data_clean/student_clean.csv")
print(f"Dimensiones del dataset: {df.shape}")
print(f"Columnas: {df.columns.tolist()}")

import pandas as pd
import os

# Determinar la ruta base del repositorio dinámicamente
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Crear directorio para datos limpios de forma relativa
os.makedirs(os.path.join(BASE_DIR, 'data_clean'), exist_ok=True)

# Cargar el dataset usando ruta relativa
df = pd.read_csv(os.path.join(BASE_DIR, 'data', 'student-mat.csv'))

# 1. Identificar valores faltantes y duplicados
missing_values = df.isnull().sum().sum()
duplicates = df.duplicated().sum()

print(f"Valores faltantes: {missing_values}")
print(f"Duplicados: {duplicates}")

# 2. Normalizar/Estandarizar variables
# Crearemos una variable 'attendance_rate' basada en 'absences'
max_absences = df['absences'].max()
if max_absences == 0: max_absences = 1 # Evitar división por cero
df['attendance_rate'] = 1 - (df['absences'] / 100) # Usamos 100 como base teórica de días

# 3. Corregir formatos
# Convertir variables binarias a numéricas para facilitar el análisis
binary_cols = ['schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']
for col in binary_cols:
    if col in df.columns:
        df[col] = df[col].map({'yes': 1, 'no': 0})

# 4. Guardar versión limpia en ruta relativa
output_path = os.path.join(BASE_DIR, 'data_clean', 'student_clean.csv')
df.to_csv(output_path, index=False)
print(f"Dataset limpio guardado en {output_path}")
print(f"Dimensiones del dataset: {df.shape}")
print(f"Columnas: {df.columns.tolist()}")

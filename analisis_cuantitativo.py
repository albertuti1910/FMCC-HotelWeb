import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import FactorAnalysis
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_regression
from scipy.stats import bartlett
from factor_analyzer.factor_analyzer import calculate_kmo
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Cargar el archivo Excel
file_path = 'c:/Users/yadai/Downloads/FMCC - Actividad 4.xlsx'  # Cambia "ruta_del_archivo" por la ubicación del archivo
data_booking = pd.read_excel(file_path, sheet_name='Booking')
data_tripadvisor = pd.read_excel(file_path, sheet_name='Tripadvisor')

# Exploración inicial de los datos
print("Datos de Booking:")
print(data_booking.head())
print("\nDatos de Tripadvisor:")
print(data_tripadvisor.head())

# REGRESIÓN MÚLTIPLE
def regression_analysis(df, target_variable, independent_vars):
    """
    Realiza un análisis de regresión múltiple.
    """
    X = df[independent_vars]
    y = df[target_variable]
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)
    print("Coeficientes del modelo:", model.coef_)
    print("Intercepto:", model.intercept_)
    print("Error cuadrático medio (MSE):", mse)

# VARIABLES (ajusta estas según tus datos)
target_variable1 = 'Valoración /10'  # Cambia por la variable dependiente
target_variable2 = 'Valoración /5'
independent_vars = ['Limpieza', 'Personal']  # Cambia por las independientes

# Aplica regresión en ambas hojas
# Aquí elige las columnas de tu interés en cada conjunto
print("Regreción de Booking")
regression_analysis(data_booking, target_variable1, independent_vars)
print("Regreción de TripAdvisor")
regression_analysis(data_tripadvisor, target_variable2, independent_vars)

# ANÁLISIS FACTORIAL
def factorial_analysis(df, n_factors):
    """
    Realiza un análisis factorial y calcula la varianza explicada.
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # Pruebas de adecuación
    _, p_value = bartlett(*scaled_data.T)
    kmo_all, kmo_model = calculate_kmo(df)
    print("Prueba de Bartlett - p-value:", p_value)
    print("Índice KMO:", kmo_model)

    # Análisis factorial
    fa = FactorAnalysis(n_components=n_factors)
    factors = fa.fit_transform(scaled_data)
    explained_variance = fa.noise_variance_
    print("Varianza explicada por cada factor:", explained_variance)
    factores = ("Factor1", "Factor2", "Factor3")
    # Visualización
    plt.bar(factores, explained_variance)
    plt.ylabel("Varianza Explicada")
    plt.title("Varianza Explicada por Factores")
    plt.show()


# Aplica análisis factorial en ambas hojas (ajustando las columnas de interés)
selected_columns_booking = ['Ubicación', 'Limpieza', 'Personal']  # Cambia según tus datos
selected_columns_tripadvisor = ['Ubicación', 'Limpieza', 'Personal']  # Cambia según tus datos
print("Booking:")
factorial_analysis(data_booking[selected_columns_booking], n_factors=3)
print("TripAdvisor:")
factorial_analysis(data_tripadvisor[selected_columns_tripadvisor], n_factors=3)


def analyze_factors(df, n_factors):
    """
    Realiza un análisis factorial, muestra cargas factoriales y asigna nombres a los factores.
    """
    # Escalar datos
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # Análisis factorial
    fa = FactorAnalysis(n_components=n_factors, random_state=42)
    fa.fit(scaled_data)
    factor_loadings = pd.DataFrame(fa.components_.T, 
                                   index=df.columns, 
                                   columns=[f"Factor {i+1}" for i in range(n_factors)])

    # Mostrar cargas factoriales
    print("Cargas factoriales:")
    print(factor_loadings)

    # Asignar nombres a factores (manual o automático)
    for i in range(n_factors):
        top_vars = factor_loadings[f"Factor {i+1}"].abs().sort_values(ascending=False).head(3).index
        print(f"Factor {i+1} está relacionado con las variables: {', '.join(top_vars)}")

    return factor_loadings

# Ajusta las columnas y número de factores
selected_columns = ['Ubicación', 'Limpieza', 'Personal']  # Cambia por tus variables
print("Booking:")
factor_loadings = analyze_factors(data_booking[selected_columns], n_factors=3)
print("TripAdvisor:")
factor_loadings = analyze_factors(data_tripadvisor[selected_columns], n_factors=3)

def analyze_clusters(df, max_clusters=5):
    """
    Realiza un análisis de clústeres y calcula el puntaje de silueta para varios K.
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    silhouette_scores = []
    for k in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(scaled_data)
        silhouette = silhouette_score(scaled_data, labels)
        silhouette_scores.append((k, silhouette))
        print(f"Para K={k}, puntaje de silueta: {silhouette:.4f}")

    # Visualizar método del codo
    plt.plot([x[0] for x in silhouette_scores], [x[1] for x in silhouette_scores], marker='o')
    plt.xlabel("Número de Clústeres (K)")
    plt.ylabel("Puntaje de Silueta")
    plt.title("Puntaje de Silueta para Diferentes K")
    plt.show()

    # Selecciona un K (puedes hacerlo manual o basado en el gráfico)
    optimal_k = 3  # Cambia según el análisis
    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    labels = kmeans.fit_predict(scaled_data)

    # Agregar etiquetas al dataframe original
    df['Cluster'] = labels
    print(f"Clusters formados con K={optimal_k}:")
    print(df.groupby('Cluster').mean())

    return df, labels

# Ajusta las columnas y aplica clúster
print("Booking:")
clustered_data, cluster_labels = analyze_clusters(data_booking[selected_columns], max_clusters=5)
print("TripAdvisor:")
clustered_data, cluster_labels = analyze_clusters(data_tripadvisor[selected_columns], max_clusters=5)

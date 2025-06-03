import pandas as pd
from sklearn.datasets import load_iris
from aves_tablas.features.utils import (
    standardize_columns,
)  # asegúrate de tener este módulo
from aves_tablas.config import setup_style

setup_style(font_scale=0.85)

# 1. Cargar el dataset Iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["largo del sépalo (cm)"] = df["sepal length (cm)"]
df["largo del pétalo (cm)"] = df["petal length (cm)"]
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# 2. Separar solo las características numéricas
features = df[iris.feature_names]

# 3. Estandarizar las columnas
standardized = standardize_columns(features)

# 4. Volver a unir con la etiqueta de especie
df_standardized = pd.concat([standardized, df["species"]], axis=1)
df_standardized["largo del sépalo (cm)"] = standardized["sepal length (cm)"]
df_standardized["largo del pétalo (cm)"] = standardized["petal length (cm)"]
# 5. Ver resultado
print(df_standardized.head())

import matplotlib.pyplot as plt
from aves_tablas.visualization.scatter import scatterplot

# Crear figura
fig, ax = plt.subplots(figsize=(8, 6))

# Graficar usando la función personalizada
scatterplot(
    ax=ax,
    df=df_standardized,
    x="largo del sépalo (cm)",
    y="largo del pétalo (cm)",
    hue="species",
    scatter_args={"s": 60, "alpha": 0.8},
    annotate=False,
    drop_na=True,
)

# Mostrar gráfico
plt.title("Iris Dataset - Largo del Sepalo vs Petalo (estandarizado)", fontsize=14)
plt.tight_layout()
# plt.show()
plt.savefig("docs/scatterplotejemplo", dpi=300, bbox_inches="tight")

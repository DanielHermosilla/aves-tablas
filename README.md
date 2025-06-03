# 🐦 `aves_tablas`: Análisis y Visualización, Educación y Soporte

Este repositorio es un *fork* del repositorio [AVES](https://github.com/zorzalerrante/aves). Contiene todo el código que alude al **manejo de tablas**.

## Instalación

Bastaría con clonar el repositorio e instalar localmente. No es necesario el uso de ambientes virtuales. 

```
git clone https://github.com/DanielHermosilla/aves-tablas

pip install -e .
```

## Ejemplos 

Se utilizará el dataset de [flores iris](https://es.wikipedia.org/wiki/Conjunto_de_datos_flor_iris): el "Hola Mundo" de la ciencia de datos.

### Visualización de tablas

```{python}
from sklearn.datasets import load_iris
from aves_tablas.features.utils import (
    standardize_columns,
)  # asegúrate de tener este módulo
from aves_tablas.visualization.scatter import scatter_plot

# Cargar el dataset Iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Separar solo las características numéricas
features = df[iris.feature_names]

# Estandarizar las columnas
standardized = standardize_columns(features)
df_standardized = pd.concat([standardized, df["species"]], axis=1)

fig, ax = plt.subplots(figsize=(8, 6))

# Graficar usando la función personalizada
scatterplot(
    ax=ax,
    df=df_standardized,
    x="Largo del sépalo (cm)",
    y="Largo del pétalo (cm)",
    hue="species",
    scatter_args={"s": 60, "alpha": 0.8},
    annotate=False,
    drop_na=True,
)

# Mostrar gráfico
plt.title("Iris Dataset - Largo del sépalo vs pétalo (estandarizado)", fontsize=14)
plt.tight_layout()
plt.show()

```


![Scatterplot de ejemplo](scatterplotejemplo.png)

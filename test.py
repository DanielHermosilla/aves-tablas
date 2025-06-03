import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from aves_tablas.visualization.boxplot import boxplot

# Crear un DataFrame de ejemplo
np.random.seed(42)
df = pd.DataFrame(
    {
        "grupo": np.random.choice(["A", "B", "C"], size=300),
        "valor": np.random.normal(loc=100, scale=20, size=300),
        "peso": np.random.uniform(0.5, 2.0, size=300),
    }
)

# Crear la figura
fig, ax = plt.subplots(figsize=(8, 5))

# Llamar a la función boxplot
boxplot(
    ax=ax,
    df=df,
    group_column="grupo",
    value_column="valor",
    weight_column="peso",
    vert=True,
    showfliers=True,
    boxplot_kwargs={"boxprops": {"facecolor": "lightblue"}},
)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

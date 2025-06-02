import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from aves_tablas.visualization.tables.bars import barchart

# Crear un DataFrame de prueba
df = pd.DataFrame(
    {
        "Categoría A": [10, 15, 7, 5],
        "Categoría B": [20, 10, 14, 6],
        "Categoría C": [5, 8, 12, 9],
    },
    index=["Item 1", "Item 2", "Item 3", "Item 4"],
)

# Crear figura
fig, ax = plt.subplots(figsize=(8, 5))

# Llamar a tu función
barchart(
    ax=ax,
    df=df,
    stacked=True,
    normalize=True,
    annotate=True,
    annotate_args={"fontsize": 8, "fmt": ".2f"},
    legend=True,
    legend_args={"bbox_to_anchor": (1.05, 1), "loc": "upper left"},
    bar_width=0.85,
)

plt.tight_layout()
plt.savefig("hello_barchart.png")
print("Barchart generado: hello_barchart.png")

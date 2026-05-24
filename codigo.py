#DESARROLLO DEL SCRIPT DE ANÁLISIS
import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset
df = pd.read_csv("../datos/ventas.csv", parse_dates=["fecha"])

# Calcular ventas totales
df["total"] = df["cantidad"] * df["precio"]
ventas_totales = df["total"].sum()

# Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Ventas por mes
df["mes"] = df["fecha"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["total"].sum()

# Guardar resultados
ventas_por_mes.to_csv("../resultados/ventas_por_mes.csv")

# Gráfico
ventas_por_mes.plot(kind="line", title="Evolución mensual de ventas")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.tight_layout()
plt.savefig("../resultados/evolucion_ventas.png")
plt.close()

import pandas as pd
presupuestos_ficticios = pd.DataFrame({
    "area": ["DGSGE", "DGPTE", "SSTEDU"],
    "presupuesto_ars": [700_000_000, 250_000_000, 50_000_000]
})
total = presupuestos_ficticios["presupuesto_ars"].sum()
presupuestos_ficticios["participacion_pct"] = (
    presupuestos_ficticios["presupuesto_ars"] / total * 100
)
print(presupuestos_ficticios.to_string(index=False))

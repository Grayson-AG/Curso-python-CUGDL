saldo_disponible = input("Cuanto dinero tenemos para la semana? ")
transporte = input("Cuanto gastas en transporte? ")
comida = input("Cuanto gastas en comida? ")
material = input("Cuanto gastas en material para la escuela? ")
Gastos_semana = int(transporte) + int(comida) + int(material)
saldo_final = int(saldo_disponible) - (Gastos_semana)

print("Tu saldo restante al final de la semana es", int(saldo_disponible) - (Gastos_semana))

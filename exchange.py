def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


budget = float(input("Introduce tu presupuesto: "))
rate = float(input("Introduce la tasa de cambio: "))

result = exchange_money(budget, rate)

print("Recibirás:", result, "en la moneda extranjera")
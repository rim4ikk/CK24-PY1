salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен
money_capital = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for month in range(1, months + 1):
    money_capital += spend * increase**(month - 1) - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))

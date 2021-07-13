
dias = int(input("Informe onumero de dias "))

horas = int(input("informe apenas a hora sem os minutos: "))

minutos = int(input("Informe os minutos: "))


dias_segund = dias * 86400

horas_segund = horas * 3600

minutos_segund = minutos * 60

soma = (dias_segund + horas_segund + minutos_segund)

print("dias":, dias, "horas:", horas,"minutos: ", minutos, " = ", soma, "segundos")
nombre = input("ingrese su nombre: ")
dias = int(input("ingrese los dias trabajados: "))
salario = int(input("ingresar su salario: "))

print(f"señor {nombre} para los {dias} dias laborados y salario {salario} su liquidacion se compone asi: ")

prima = salario*dias/360
cesantias = salario*dias/360
interesescesantias = cesantias*0.12/dias
vacaciones = salario*dias/720
liquidacion = prima+cesantias+interesescesantias+vacaciones

print(f"prima: ${round(prima, 2)}")
print(f"cesantias: ${round(cesantias, 2)}")
print(f"interesescesantias: ${round(interesescesantias, 2)}")
print(f"vacaciones: ${round(vacaciones, 2)}")
print(f"liquidacion: ${round(liquidacion, 2)}")



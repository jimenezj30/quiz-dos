nombre = input("ingrese su nombre: ")
dias = int(input("ingrese los dias trabajados: "))
salario = int(input("ingresar su salario: "))

print(f"señor {nombre} para los {dias} dias laborados y salario {salario} su liquidacion se compone asi: ")

prima = salario*dias/360
cesantias = salario*dias/360
interesescesantias = cesantias*0.12/dias
vacaciones = salario*dias/720
liquidacion = prima+cesantias+interesescesantias+vacaciones

print(f"prima: ${prima} "
      f"cesantias: ${cesantias} "
      f"interesescesantias: ${interesescesantias} "
      f"vacaciones: ${vacaciones} "
      f"liquidacion: ${liquidacion} ")

      
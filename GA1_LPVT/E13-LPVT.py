#Leslie Pamela Velásquez Tzarax (29)
#Ejercicio 13

#Constantes (por convención, se escriben en mayúsculas)
SALARIO_BASE = 3500.00 #Salario mensual en quetzales
BONO_PRODUCTIVIDAD = 500.00 #Bono mensual fijo
IMPUESTO = 0.12 #12% de impuesto sobre el salario total

#Datos del empleado (variables)
nombre_empleado = "Leslie Velásquez"
es_empleado_fijo = True

#Cálculo del salario bruto (salario base + bono)
salario_bruto = SALARIO_BASE + BONO_PRODUCTIVIDAD

#Cálculo del descuento por impuestos
descuento = salario_bruto * IMPUESTO

#Cálculo del salario neto
salario_neto = salario_bruto - descuento

#Mostrar información
print("Nombre del empleado: ", nombre_empleado)
print("¿Empleado fijo?", es_empleado_fijo)
print("Salario base: ", SALARIO_BASE)
print("Bono de productividad: ", BONO_PRODUCTIVIDAD)
print("Salario bruto: ", salario_bruto)
print("Descuento por impuestos: ", descuento)
print("Salario neto: ", salario_neto)
"""
#1. Lea dos números e imprima solo los positivos.
numero1=int(input(f'Escriba el numero 1: '))
numero2=int(input(f'Escriba el numero 2: '))
if numero1 >= 0 and numero2 >= 0:
    print(f"Los numeros positivos son: {numero1} y {numero2}")
elif numero1 >= 0:
    print(f"El numero positivo es: {numero1}")
elif numero2 >= 0:
    print(f"El numero positivo es: {numero2}")
else:
    print(f"No hay numeros positivos")


#2. lea dos números e imprima ambos solo si son positivos
numero1=int(input(f"Escriba el numero 1: "))
numero2=int(input(f"Escriba el numero 2: "))

if numero1 >= 0 and numero2 >= 0:
    print(f"Los numeros positivos son: {numero1} y {numero2}")
else:
    print(f"No hay numeros positivos o uno de los numeros no lo es.")


#3. lea dos números calcule la suma e imprima los dos números leídos solo si la suma es negativa

numero1=int(input(f"Escriba el numero 1: "))
numero2=int(input(f"Escriba el numero 2: "))
suma = numero1 + numero2
if suma < 0:
    print(f"Los numeros {numero1} y {numero2} da un resultado negativo de {suma}.")
else:
    print(f"Su resultado no da negativo.")


#4. elaborar un algoritmo que averigüe si un triangulo es equilátero, isósceles o escaleno, como datos de entrada se tienen sus 3 lados.

lado1=int(input(f"Digite el primer lado de su triangulo: "))
lado2=int(input(f"Digite el segundo lado de su triangulo: "))
lado3=int(input(f"Digite el tercer lado de su triangulo: "))

if lado1 == lado2 and lado2 == lado3:
    print(f"Su triangulo es equilatero.")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print(f"Su triangulo es isoseles.")
elif lado1 == lado2 or lado1 != lado2 and lado1 == lado3 or lado1 != lado3 and lado2 == lado3 or lado2 != lado3:
    print(f"Su triangulo es escaleno.")


#5. Una frutería ofrece peras con descuento según la siguiente tabla:
#Entrar por pantalla: numero de peras compradas y valor compra. Determinar cuanto pagara una persona que compre peras en esa frutería.

peras=int(input(f"Digite la cantidad de peras a llevar: "))
valorventa=int(input(f"Digite el valor de la compra: "))
descuento10 = valorventa * 10 / 100
valorcondescuento10 = valorventa - descuento10
descuento15 = valorventa * 15 / 100
valorcondescuento15 = valorventa - descuento15
descuento18 = valorventa * 18 / 100
valorcondescuento18 = valorventa - descuento18
if peras >= 0 and peras <= 2:
    print(f"El total a pagar por {peras} peras es de COP{valorventa}.")
elif peras >= 3 and peras <= 5:
    print(f"El total a pagar por {peras} peras es de COP{valorcondescuento10}.")
elif peras >= 6 and peras <= 10:
    print(f"El total a pagar por {peras} peras es de COP{valorcondescuento15}.")
elif peras >= 11:
    print(f"El total a pagar por {peras} peras es de COP{valorcondescuento18}.")


#6. Realizar un algoritmo que lea el valor de la unidad y el # de unidades vendidas por un empleado e imprima su comisión
# si se sabe que la comisión es del 15 % si vende mas de 200 unidades del 10% si vende entre 100 y 200 unidades y el 5% si
# vende menos de 100 unidades sobre el valor total de la venta.


def comisionventa ():
    valorxunidad=int(input(f"Digite el valor por unidad: "))
    unidadesvendidas=int(input(f"Digite el numero de unidades vendidas: "))
    valortotal = valorxunidad * unidadesvendidas
    comision15 = valortotal * 15 / 100
    comision10 = valortotal * 10 / 100
    comision5 = valortotal * 5 / 100
    if unidadesvendidas > 200:
        print(f"La comicion por sus ventas es de: COP{comision15}.")
    elif unidadesvendidas >= 100 and unidadesvendidas <= 200:
        print(f"La comicion por sus ventas es de: COP{comision10}.")
    elif unidadesvendidas < 100:
        print(f"La comicion por sus ventas es de: COP{comision5}.")
comisionventa()

#7. Calcular el total que una persona debe pagar en una llantera, si el precio de cada llanta es de $800 si se
# compran menos de 5 llantas y de $700 si se compran 5 o mas.

def llantera ():
    llantas=int(input(f"Digite el numero de llantas a llevar: "))
    valortotalmenosde5 = 800 * llantas
    valortoptalmasde5 = 700 * llantas
    if llantas < 5:
        print(f"El valor total de su venta es de ${valortotalmenosde5}")
    else:
        print(f"El valor total de su compra es de ${valortoptalmasde5}")
llantera()


#8. En una escuela la colegiatura el costo de matrícula de los alumnos se determina según el número de materias que cursan.
# El costo de todas las materias es el mismo. Se ha establecido un programa para estimular a los alumnos, el cual consiste en
# lo siguiente: si el promedio obtenido por un alumno en el ultimo periodo es mayor o igual que 4, se le hará un descuento
# del 30% sobre la matrícula y no se le cobrara IVA; si el promedio obtenido es menor que 4 deberá pagar la matricula completa,
# la cual incluye el 10% de IVA. Obtener cuanto debe pagar un alumno.

def matricula ():
    materias=int(input(f"Digite el numero de materias a cursar: "))
    costoxmateria=int(input(f"Digite el valor de la materia: "))
    promedioxalumno=int(input(f"Digite el promedio del alumno: "))
    costodematricula = costoxmateria * materias
    descuento = costodematricula * 30 / 100
    decuentoaplicado = costodematricula - descuento
    iva = costodematricula * 10 / 100
    ivaaplicado = costodematricula + iva
    if promedioxalumno >= 4:
        print(f"El valor de la matricula es de COP{decuentoaplicado}")
    else:
        print(f"El valor de la matricula es COP{ivaaplicado}")

matricula()



#9. En una fábrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del número
# de computadoras que compre. Si las computadoras son menos de cinco se les dará un 10% de descuento sobre el total
# de la compra; si el número de computadoras es mayor o igual a cinco pero menos de diez se le otorga un
# 20% de descuento; y si son 10 o más se les da un 40% de descuento. El precio de cada computadora es de $11,000

def computadoras ():
    numerodecompus=int(input(f"Digite el numero de computadoras que va a llevar: "))
    valordelaventa = 11000 * numerodecompus
    descuento10 = valordelaventa * 10 / 100
    descuentoaplicado10 = valordelaventa - descuento10
    descuento20 = valordelaventa * 20 / 100
    descuentoaplicado20 = valordelaventa - descuento20
    descuento40 = valordelaventa * 40 / 100
    descuentoaplido40 = valordelaventa - descuento40
    if numerodecompus < 5:
        print(f"El total de su compra es de: ${descuentoaplicado10}")
    elif numerodecompus >= 5 and numerodecompus < 10:
        print(f"El total de su compra es de: ${descuentoaplicado20}")
    elif numerodecompus >= 10:
        print(f"El total de su compra es de: ${descuentoaplido40}")

computadoras()

#10. Un almacén de venta de ropa tiene las siguientes promociones para sus clientes las cuales consisten en lo siguiente:
# Para ventas menores ó iguales a 100.000 con pago en efectivo, se hace un descuento del 20%, con tarjeta de crédito se hace el 10%
# Para ventas mayores a 100.000 y menores o iguales a 200.0000, con pago en Efectivo se hace un descuento del 30%, con tarjeta de crédito se hace el 15%
# Para ventas mayores a 200.000, con pago en efectivo se hace un descuento del 40% y con tarjeta de crédito se hace el 20%.

def almacen():
    valordecompra=int(input(f"Digite el valor de la compra: "))
    tipodepago=int(input(f"Digite el tipo de pago 1: efectivo, 2: tarjeta. "))
    ventamenoroigualefectivo100 = valordecompra * 20 / 100
    ventamenoroigualtarjeta100 = valordecompra * 10 / 100
    totalpagarefectivo100 = valordecompra - ventamenoroigualefectivo100
    totalpagartarjeta100 = valordecompra - ventamenoroigualtarjeta100
    ventamayor100menorigual200efectivo = valordecompra * 30 / 100
    ventamayor100menorigual200tarjeta = valordecompra * 15 / 100
    totalpagarefectivo100y200 = valordecompra - ventamayor100menorigual200efectivo
    totalpagartarjeta100y200 = valordecompra - ventamayor100menorigual200tarjeta
    ventamayor200efectivo = valordecompra * 40 / 100
    ventamayor200tarjeta = valordecompra * 20 / 100
    totalpagarefectivo200 = valordecompra - ventamayor200efectivo
    totalpagartarjeta200 = valordecompra - ventamayor200tarjeta
    if valordecompra <= 100000:
        if tipodepago == 1:
            print(f"El total a pagar tiene un valor de COP{totalpagarefectivo100}.")
        else:
            print(f"El total a pagar tiene un valor de COP{totalpagartarjeta100}.")
    elif valordecompra > 100000 and valordecompra <= 200000:
        if tipodepago == 1:
            print(f"El total a pagar tiene un valor de COP{totalpagarefectivo100y200}.")
        else:
            print(f"El total a pagar tiene un valor de COP{totalpagartarjeta100y200}.")
    elif valordecompra > 200000:
        if tipodepago == 1:
            print(f"El total a pagar tiene un valor de COP{totalpagarefectivo200}.")
        else:
            print(f"El total a pagar tiene un valor de COP{totalpagartarjeta200}.")

almacen()

#11. Una tienda que vende pantalones al menudeo y al mayoreo tiene las siguientes tarifas, si se compran menos
#de 5 pantalones estos se cobran a su precio normal, en caso de que se compren 5 o más pero menos de 12 ,
# se les descuenta el 15% en cada pantalón, si se compran más de 12 se les descuenta 30% en cada pantalón.
# Escriba un programa que pida como dato de entrada el número de pantalones que se desean comprar y con ello imprima
# el total a pagar por la compra hecha.

def pantalones():
    cantidad_pantalones = int(input(f"Digite la cantidad de pantalones que va a llevar: "))
    precio_x_mantalon = int(input(f"Digite el precio de un pantalon: "))
    cionco_o_mas_but_menos_12 = precio_x_mantalon * 15 / 100
    mas_12 = precio_x_mantalon * 30 / 100
    if cantidad_pantalones < 5:
        total_a_pagar = precio_x_mantalon * cantidad_pantalones
        print(f"El total de su compra es de COP{total_a_pagar}.")
    elif cantidad_pantalones >= 5 and cantidad_pantalones < 12:
        precio_x_panalon_con_cescuento = precio_x_mantalon - cionco_o_mas_but_menos_12
        total_a_pagar = precio_x_panalon_con_cescuento * cantidad_pantalones
        print(f"El precio total a pagar de su compra es de COP{total_a_pagar}.")
    elif cantidad_pantalones > 12:
        precio_x_pantalon_con_descuento = precio_x_mantalon - mas_12
        total_a_pagar = precio_x_pantalon_con_descuento * cantidad_pantalones
        print(f"El total a pagar se du compra es de COP{total_a_pagar}.")


pantalones()
"""



































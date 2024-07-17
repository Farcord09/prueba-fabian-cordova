import random
import statistics
empleados = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]


def generar():
    sueldos = {}
    for empleado in empleados:
        sueldo = random.randint(400000, 1500000)
        sueldos[empleado] = sueldo
        return sueldos
  
def clasificar():
    menores_800000 = []
    entre_800000_2000000=[]
    mayores_2000000 = []
    for empleados, sueldo in sueldos_empleado.items():
        if sueldo < 800000:
            menores_800000.append((trabajadores, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800000_2000000.append((trabajadores, sueldo))
        elif sueldo > 2000000:
            mayores_2000000.append((trabajadores, sueldo))
    menuClasificar='''
    menu clasificar
    1. sueldos menores a 800000
    2. sueldos entre 800000 y 2000000
    3. sueldos mayores a 2000000
    4. salir
    '''
    print (menuClasificar)
    
while True:
    op1=int('Ingrese la opcion: ')
    while(op1<1 or op1>4):
        op1=int(input('Ingrese opción del 1 al 3: '))
        if(op1==1):
            print("Sueldos menores a 800000: ")
            for empleado, sueldo in menores_800000:
                print(f"{empleado}: {sueldo}")
            continue
        if(op1==2):
            print("\nSueldos Entre 600000 y 800000: ")
            for empleado, sueldo in entre_800000_2000000:
                print(f"{empleado}: {sueldo}")
            continue
        if(op1==3):
            print("\nSueldos Mayores a 2.000.000: ")
            for empleado, sueldo in mayores_2000000:
                print(f"{empleado}: {sueldo}")
            continue
        if(op1==4):
            break
        
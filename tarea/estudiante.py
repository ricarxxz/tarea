estudiantes = []


def agregar_estudiante(nombre, nota):
    if nota < 0:
        print("Error: La nota no puede ser negativa")
        return False
    
    estudiante = {
        "nombre": nombre,
        "nota": nota
    }
    
    estudiantes.append(estudiante)
    print(f"Estudiante '{nombre}' agregado con nota {nota}")
    return True


def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    
    print("LISTA DE ESTUDIANTES")
    
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"{i}. {estudiante['nombre']:<30} Nota: {estudiante['nota']:.2f}")
    

def calcular_promedio():
    if not estudiantes:
        print("No hay estudiantes para calcular promedio")
        return None
    
    suma_notas = sum(x['nota'] for x in estudiantes)
    promedio = suma_notas / len(estudiantes)
    
    print(f"\nPromedio general: {promedio:.2f}")
    return promedio


def menu_principal():
    while True:
        print("\n")
        print("SISTEMA DE GESTIÓN DE ESTUDIANTES")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Calcular promedio general")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            nombre = input("Nombre del estudiante: ")
            nota = float(input("Nota del estudiante: "))
            agregar_estudiante(nombre, nota)
        elif opcion == '2':
            mostrar_estudiantes()
        
        elif opcion == '3':
            calcular_promedio()
        
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intente nuevamente")


    menu_principal()


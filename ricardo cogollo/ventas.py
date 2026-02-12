ventas = [1200, 850, 1020, 2100, 1750, 980]

def calcular_ventas(ventas):
    if not ventas:
        print("No hay ventas registradas")
        return None
    venta_mayor = max(ventas),
    venta_menor = min(ventas) ,  
    promedio_ventas = sum(ventas) / len(ventas),
    return {
        'venta_mayor': venta_mayor,
        'venta_menor': venta_menor,
        'promedio_ventas': promedio_ventas
    }

print("Análisis de ventas:")
resultado=calcular_ventas(ventas)
print(f"Venta mayor: ${resultado['venta_mayor'][0]}")
print(f"Venta menor: ${resultado['venta_menor'][0]}")
print(f"Promedio de ventas: ${resultado['promedio_ventas'][0]:.2f}")
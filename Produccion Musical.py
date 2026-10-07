def obtener_duracion_cancion(nombre_cancion):
    """Solicita al usuario los minutos y segundos de una canción y los devuelve en segundos totales."""
    print(f"\n--- {nombre_cancion} ---")
    while True:
        try:
            minutos = int(input("Minutos: "))
            segundos = int(input("Segundos: "))
            
            if minutos < 0 or segundos < 0 or segundos >= 60:
                print("Por favor, ingresa valores válidos (segundos entre 0 y 59).")
                continue
            
            # Convertir todo a segundos para facilitar el cálculo
            return (minutos * 60) + segundos
        except ValueError:
            print("Entrada inválida. Por favor, ingresa solo números enteros.")

def calcular_playlist():
    print("=== CALCULADORA DE DURACIÓN DE PLAYLIST ===")
    
    try:
        cantidad = int(input("¿Cuántas canciones tiene la playlist?: "))
        if cantidad <= 0:
            print("La playlist debe tener al menos una canción.")
            return
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    duracion_total_segundos = 0

    # Bucle para pedir la duración de cada canción
    for i in range(1, cantidad + 1):
        segundos_cancion = obtener_duracion_cancion(f"Canción {i}")
        duracion_total_segundos += segundos_cancion

    # Convertir el total de segundos de nuevo a formato Minutos:Segundos
    minutos_totales = duracion_total_segundos // 60
    segundos_restantes = duracion_total_segundos % 60

    # Mostrar el resultado final
    print("\n" + "="*40)
    print(f"Duración total de la playlist: {minutos_totales} minutos y {segundos_restantes} segundos.")
    print("="*40)

# Ejecutar el programa
if __name__ == "__main__":
    calcular_playlist()
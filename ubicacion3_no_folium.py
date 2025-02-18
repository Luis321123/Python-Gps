import requests

def obtener_ubicacion():
    try:
        # Hacer una solicitud a ipinfo.io
        response = requests.get("https://ipinfo.io")
        if response.status_code == 200:
            data = response.json()
            # Obtener la ubicación (latitud y longitud)
            ubicacion = data.get('loc', '').split(',')
            if len(ubicacion) == 2:
                latitud = ubicacion[0]
                longitud = ubicacion[1]
                return latitud, longitud
            else:
                print("No se pudo obtener la ubicación desde la respuesta.")
                return None, None
        else:
            print(f"Error al obtener la ubicación. Código de estado: {response.status_code}")
            return None, None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None, None

# Obtener la ubicación
latitud, longitud = obtener_ubicacion()
if latitud and longitud:
    print(f"Latitud: {latitud}, Longitud: {longitud}")
else:
    print("No se pudo obtener la ubicación.")
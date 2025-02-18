import requests
import folium

def obtener_ubicacion():
    try:
        response = requests.get("https://ipinfo.io")
        if response.status_code == 200:
            data = response.json()
            ubicacion = data.get('loc', '').split(',')
            if len(ubicacion) == 2:
                latitud = float(ubicacion[0])
                longitud = float(ubicacion[1])
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

def mostrar_mapa(latitud, longitud):
    mapa = folium.Map(location=[latitud, longitud], zoom_start=15)
    folium.Marker([latitud, longitud], popup="Tu ubicación").add_to(mapa)
    mapa.save("mapa.html")
    print("Mapa guardado como 'mapa.html'. Abre este archivo en tu navegador para ver el mapa.")

# Obtener la ubicación
latitud, longitud = obtener_ubicacion()
if latitud and longitud:
    print(f"Latitud: {latitud}, Longitud: {longitud}")
    mostrar_mapa(latitud, longitud)
else:
    print("No se pudo obtener la ubicación.")


        #tambien es la menos precisa que he encontrado 
from geopy.geocoders import Nominatim

def obtener_ubicacion_precisa():
    geolocalizador = Nominatim(user_agent="mi_aplicacion")
    try:
        # Obtener la ubicación basada en la dirección IP o nombre de la ciudad
        ubicacion = geolocalizador.geocode("Puerto ordaz,Ciudad Guayana,Estado Bolivar, Venezuela")
        if ubicacion:
            return ubicacion.latitude, ubicacion.longitude
        else:
            print("No se pudo obtener la ubicación precisa.")
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

latitud, longitud = obtener_ubicacion_precisa()
if latitud and longitud:
    print(f"Latitud: {latitud}, Longitud: {longitud}")

    #esta es la mas precisa actualmente
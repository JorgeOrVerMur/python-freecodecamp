# 1. Definición de variables con valores iniciales de prueba
distance_mi = 5
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

# 2. Evaluación de condiciones en orden ascendente
if not distance_mi:
    # Si distance_mi es un valor falso (como 0)
    print(False)

elif distance_mi <= 1:
    # Si la distancia es menor o igual a 1 milla
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi > 1 and distance_mi <= 6:
    # Si la distancia es mayor que 1 y menor o igual a 6 millas
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

else:
    # Si la distancia es mayor a 6 millas
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
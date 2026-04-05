import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c  # distance in KM


def calculate_eta(distance_km):
    speed = 30  # avg bus speed km/h
    if speed == 0:
        return 0
    return round((distance_km / speed) * 60)  # minutes
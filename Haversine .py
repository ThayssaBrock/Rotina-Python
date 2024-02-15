import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371  

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = R * c
    return distancia

def encontrar_pares_proximos(coordenadas, limite_distancia):
    for i in range(len(coordenadas)):
        for j in range(i + 1, len(coordenadas)):
            lat1, lon1 = coordenadas[i]
            lat2, lon2 = coordenadas[j]

            distancia = calcular_distancia(lat1, lon1, lat2, lon2)

            if distancia <= limite_distancia:
                print(f"Coordenadas próximas: {coordenadas[i]} e {coordenadas[j]} - Distância: {distancia:.2f} metros")

# Exemplo de uso
coordenadas = [
    [-6.407042,-38.3230062],
    [-23.33180172,-46.30179326],
    [-23.444016,-46.71080378],
    [-23.44911031,-46.734095],
    [-23.4496131,-46.732435],
    [-23.4653218,-46.6511406],
    [-23.4718149,-46.6422577],
    [-23.47260703,-46.64149655],
    [-23.4759575,-46.6414303],
    [-23.4870438,-46.4936151],
    [-23.4881716,-46.4931665],
    [-23.4888235,-46.4793446],
    [-23.4950099,-46.8840636],
    [-23.4987433,-46.7535253],
    [-23.58121487,-46.52811782],
    [-23.6017311,-46.5001693],
    [-23.602349,-46.4977542],
    [-23.6039709,-46.4993115],
    [-23.6040186,-46.4993376],
    [-23.6118624,-46.4393799],
    [-23.6119097,-46.4392718],
    [-23.6119119,-46.4392712],
    [-23.6119126,-46.4392623],
    [-23.6119148,-46.439268],
    [-23.6130167,-46.4685718],
    [-23.6175561,-46.4750348],
    [-23.6176892,-46.47183],
    [-23.633753,-46.6364251],
    [-23.6357946,-46.6350066],
    [-23.6358758,-46.6370244],
    [-23.6364212,-46.6311252],
    [-23.6366311,-46.6411252],
    [-23.6366814,-46.6311408],
    [-23.636732,-46.6326177],
    [-23.6367516,-46.6325753],
    [-23.6368452,-46.6342398],
    [-23.6373051,-46.6336308],
    [-23.6378211,-46.639549],
    [-23.6379175,-46.6350324],
    [-23.6933284,-46.7441988],
    [-23.7483761,-46.7060477],
    [-23.7571019,-46.7072136],
    [-23.76110975,-46.70113009],
    [-23.76464555,-46.70112177],
    [-23.76498121,-46.70117816],
    [-23.76498121,-46.70117816],


]

limite_distancia = 0.10 # 100 metros
encontrar_pares_proximos(coordenadas, limite_distancia)

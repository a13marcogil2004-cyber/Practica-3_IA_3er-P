import heapq

grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    cola = [(0, inicio)]
    visitados = set()

    print(f"\nNodo inicial: {inicio}\n")

    paso = 1

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        print(f"PASO {paso}")
        print(f"Nodo actual: {nodo_actual}")
        print("Distancias actuales:")

        for nodo, distancia in distancias.items():
            print(f"{nodo}: {distancia}")

        print("-" * 30)

        paso += 1


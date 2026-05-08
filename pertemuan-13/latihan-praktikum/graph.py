class LogNavSystem:
    def __init__(self):
        self.graph = {}

    def add_city(self, city_name):
        if city_name not in self.graph:
            self.graph[city_name] = []
    
    def add_route(self, x, y, distance):
        self.add_city(x)
        self.add_city(y)
        self.graph[x].append((y, distance))
        self.graph[y].append((x, distance))
        print(f"[INPUT] adding route: {x} - {y} ({distance} km)")
    
    def display_graph(self):
        print("[INFO] Distribution Network Structure")
        for k, v in self.graph.items():
            connected_city = ", ".join([f"{c} ({d})" for (c, d) in v])
            print(f"- {k} connected to:", connected_city)
    
    def dijkstra(self, start_from_city):
        distance = {c: float("inf") for c in self.graph}
        distance[start_from_city] = 0
        visited = set()

        print(f"[PROCESS] Calculate shortest route from: {start_from_city}...")
        while len(visited) < len(self.graph):
            current_city = None
            shortest_distance = float("inf")

            for c in self.graph:
                if c not in visited and distance[c] < shortest_distance:
                    shortest_distance = distance[c]
                    current_city = c
            
            if current_city is None:
                break
            visited.add(current_city)

            for c, d in self.graph[current_city]:
                new_distance = distance[current_city] + d
                if new_distance < distance[c]:
                    distance[c] = new_distance
            
        return distance


def main():
    nav = LogNavSystem()
    print("LOGISTICS NAVIGATION SYSTEM \"KILAT MAJU\"")
    print("=========================================")

    nav.add_route("Jakarta", "Bandung", 150)
    nav.add_route("Jakarta", "Cirebon", 200)
    nav.add_route("Bandung", "Tasikmalaya", 100)
    nav.add_route("Bandung", "Cirebon", 130)
    nav.add_route("Cirebon", "Semarang", 250)
    nav.add_route("Tasikmalaya", "Semarang", 200)

    print()
    nav.display_graph()

    print()
    result = nav.dijkstra("Jakarta")
    print("\n[RESULT] Shortest Route from Jakarta:")
    for i, (c, d) in enumerate(sorted(result.items(), key=lambda x: x[1]), 1):
        if c == "Jakarta":
            continue
        print(f"{i}. To {c}: {d} km")
    
    print("\n=========================================")
    print("Navigaton Simulation Completed!")
    


if __name__ == "__main__":
    main()
def read_city_data(file_path):
    cities = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                data = line.strip().split()
                if len(data) == 3:
                    city_name, population, area = data
                    cities.append({
                        'city_name': city_name,
                        'population': float(population),
                        'area': float(area)
                    })
    except FileNotFoundError:
        print("File not found.")

    return cities

def calculate_total_area(cities):
    return sum(city['area'] for city in cities)

def main():
    file_path = "city.txt"
    cities = read_city_data(file_path)

    if not cities:
        print("No city data found.")
        return

    total_area = calculate_total_area(cities)
    print(f"Total area of all cities: {total_area:.2f} sq KM")

if __name__ == "__main__":
    main()

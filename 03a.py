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

def display_city_details(cities):
    if not cities:
        print("No city data found.")
        return

    print("City Data:")
    for city in cities:
        print(f"{city['city_name']}: Population - {city['population']} lakhs, Area - {city['area']} sq KM")

def main():
    file_path = "city.txt"
    cities = read_city_data(file_path)

    display_city_details(cities)

if __name__ == "__main__":
    main()


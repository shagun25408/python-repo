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

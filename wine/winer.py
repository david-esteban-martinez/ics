import os


def group_wine_data(folder_path):
    red_wine_data = {}
    white_wine_data = {}

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    wine_type, attribute_value = line.strip().split(':')
                    wine_type = wine_type.strip()
                    attribute, value = attribute_value.split("\t")
                    value = float(value)

                    if wine_type == 'red':
                        if attribute not in red_wine_data:
                            red_wine_data[attribute] = []
                        red_wine_data[attribute].append(value)
                    elif wine_type == 'white':
                        if attribute not in white_wine_data:
                            white_wine_data[attribute] = []
                        white_wine_data[attribute].append(value)

    print("Red Wine Data:")
    for attribute, values in red_wine_data.items():
        print(attribute + ": " + str(values))

    print("\n" + '-' * 30 + "\n")

    print("White Wine Data:")
    for attribute, values in white_wine_data.items():
        print(attribute + ": " + str(values))

folder_path = 'salida_vino'
group_wine_data(folder_path)

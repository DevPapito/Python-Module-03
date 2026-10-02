import math


def main():
    print("=== Game Coordinate System ===")

    # Leitura do primeiro ponto
    print("Get a first set of coordinates")
    while True:
        user_input = input("Enter new coordinates floats in format 'x,y,z': ")
        splited_input = user_input.split(",")
        if len(splited_input) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(splited_input[0].strip())
            y = float(splited_input[1].strip())
            z = float(splited_input[2].strip())
            break  # Encerra o loop ao obter entradas válidas
        except ValueError:
            print("Invalid Syntax")
            continue

    tuple_point_1 = (x, y, z)
    print(f"Got a first tuple {tuple_point_1}")
    print(f"It includes: X={x}, Y={y}, Z={z}")

    # Cálculo da distância do primeiro ponto ao centro (0,0,0)
    dist_center = math.sqrt(
        tuple_point_1[0] ** 2 + tuple_point_1[1] ** 2 + tuple_point_1[2] ** 2
    )
    print(f"Distance to center : {round(dist_center, 4)}")

    # Leitura do segundo ponto
    print("Get a second set of coordinates")
    while True:
        user_input = input("Enter new coordinates floats in format 'x,y,z': ")
        splited_input = user_input.split(",")
        if len(splited_input) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(splited_input[0].strip())
            y = float(splited_input[1].strip())
            z = float(splited_input[2].strip())
            break  # Encerra o loop ao obter entradas válidas
        except ValueError:
            print("Invalid Syntax")
            continue

    tuple_point_2 = (x, y, z)

    # Cálculo da distância entre os dois pontos
    dist = math.sqrt(
        (tuple_point_2[0] - tuple_point_1[0]) ** 2
        + (tuple_point_2[1] - tuple_point_1[1]) ** 2
        + (tuple_point_2[2] - tuple_point_1[2]) ** 2
    )
    print(f"Distance between points : {round(dist, 4)}")


if __name__ == "__main__":
    main()
import os

if __name__ == '__main__':
    folder = "salida_temp"
    max_temp1 = 27
    min_temp2 = -1
    max_name = None
    min_name = None

    for file in os.listdir(folder):
        if file=="_SUCCESS":
            continue
        with open(os.path.join(folder, file), "r") as f:
            # f.readline()
            for line in f:
                name, temp1, temp2 = line.split()
                temp1 = float(temp1)
                temp2 = float(temp2)
                if temp1 > max_temp1:
                    max_temp1 = temp1
                    max_name = name
                if temp2 < min_temp2:
                    min_temp2 = temp2
                    min_name = name
    print("Max temperature seen in " + max_name+ " at "+str(max_temp1))
    print("Min temperature seen in " + min_name+" at "+str(min_temp2))

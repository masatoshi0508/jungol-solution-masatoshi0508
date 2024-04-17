while True:
    width = int(input("Width = "))
    height = int(input("Height = "))
    triangle_area = width * height / 2
    print(f"Triangle Area = {triangle_area}")
    continue1 = input("continue? ")
    if continue1 != "Y" and continue1 != "y":
        break
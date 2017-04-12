x = "12 km/L"
one_km = 1 / 12
hours = int(input())
speed = int(input())

fuel_cost = one_km * hours * speed

print("%.3f" % fuel_cost)

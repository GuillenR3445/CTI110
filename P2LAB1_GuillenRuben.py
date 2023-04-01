miles_per_gallon = float(input())
dollars_per_gallon = float(input())


cost_20miles = (20 / miles_per_gallon) * dollars_per_gallon
cost_75miles = (75 / miles_per_gallon) * dollars_per_gallon
cost_500miles = (500 / miles_per_gallon) * dollars_per_gallon

print(f'{cost_20miles:.2f} {cost_75miles:.2f} {cost_500miles:.2f}')
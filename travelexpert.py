destinations = {
    "1": {"name": "Чолпон-Ата", "distance": 264, "mountain": False},
    "2": {"name": "Каракол", "distance": 400, "mountain": False},
    "3": {"name": "Ош", "distance": 605, "mountain": True},
    "4": {"name": "Нарын", "distance": 315, "mountain": True},
    "5": {"name": "Талас", "distance": 300, "mountain": True},
    "6": {"name": "Баткен", "distance": 850, "mountain": True}
}

print("--- Система расчета поездок по Кыргызстану ---")
print("Выберите пункт назначения:")
for key, city in destinations.items():
    print(f"{key}. {city['name']} ({city['distance']} км)")

choice = input("\nВведите номер (или '0' для своего расстояния): ")

if choice in destinations:
    city = destinations[choice]
    dist = city['distance']
    is_mtn = city['mountain']
    print(f"Выбран маршрут до г. {city['name']}")
else:
    dist = float(input("Введите расстояние в км: "))
    is_mtn = input("Маршрут через горы? (да/нет): ").lower() == "да"

consumption = float(input("Расход топлива (л/100 км): "))
price = float(input("Цена литра бензина (сом): "))
people = int(input("Количество человек в машине: "))


k = 1.2 if is_mtn else 1.0
needed_fuel = (dist * consumption / 100) * k
total_cost = needed_fuel * price
per_person = total_cost / people

print("\n--- РЕЗУЛЬТАТЫ ---")
print(f"Расстояние: {dist} км")
if is_mtn: print("(!) Учтен повышенный расход в горах (+20%)")
print(f"Нужно бензина: {round(needed_fuel, 2)} л.")
print(f"Общая сумма: {round(total_cost, 2)} сом")
print(f"С каждого человека: {round(per_person, 2)} сом")


if per_person > 3000:
    print("\nСовет: Поездка выходит дорогой, лучше ехать большой компанией.")
else:
    print("\nСовет: Отличная цена для такого путешествия!")
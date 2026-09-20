def expert_system_full_analysis(first_name, last_name):
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()

    
    unisex_names = ['Жениш', 'Эркин', 'Жылдыз', 'Рахат', 'Аян', 'Нур']

    female_last_markers = ['ова', 'ева', 'кызы']
    male_last_markers = ['ов', 'ев', 'уулу']

    female_name_markers = ['гул', 'гүл', 'ай', 'кыз']

    print(f"\n--- Анализ: {first_name} {last_name} ---")

    
    if first_name in unisex_names:

        
        for marker in female_last_markers:
            if last_name.lower().endswith(marker):
                return "Результат: Женщина (определено по фамилии)"

        
        for marker in male_last_markers:
            if last_name.lower().endswith(marker):
                return "Результат: Мужчина (определено по фамилии)"

        return "Результат: Общее имя, пол определить сложно"

    
    for marker in female_name_markers:
        if marker in first_name.lower():
            return "Результат: Женщина (определено по имени)"

    # Если ничего не найдено
    return "Результат: Мужчина или данных недостаточно"




print("ПРОГРАММА ЗАПУЩЕНА")

user_f = input("Введите имя: ")
user_l = input("Введите фамилию: ")

result = expert_system_full_analysis(user_f, user_l)

print(result)
#nums = [3, 5, 7, 9, 10.5]
#nums.append('Python')
#del nums[0] # Удаление по индексу
#nums.remove('Python') # Удаление значения
#print(nums)

#other = ['Пылесо', 'Жесткий диск']
#items = {"1": "Компьютер", "2": "Монитор", "3": "Веб камера"}

#print(items.get("4")) # Безопасное обращение к ключу

#print(items.get("5", "Колонки")) # Назначение значения 
# по умолчаняю для не существующего ключа
#items['6'] = other # Объединение списка и словаря
#print(items)

info_city = {"city": 'Москва', 'temperature': '20'}

info_city['temperature'] = '25'
print(info_city['temperature'])
print(info_city.get('country', 'Россия'))
info_city['date'] = '27.05.2019'
print(info_city)

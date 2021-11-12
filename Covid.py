import requests, json

url = "https://covid-19-world-vaccination-data.p.rapidapi.com/"

querystring = {"iso":"RUS"}

headers = {
    'x-rapidapi-host': "covid-19-world-vaccination-data.p.rapidapi.com",
    'x-rapidapi-key': "censored"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

## Конвертируем ответ в удобный формат

json_data = json.loads(response.text)

## Записываем отклик в файл

with open("vaccination_rus_total.txt", "w") as file:
    file.write(str(json_data))

## Получаем из кучи исторических данных последнюю, самую свежую запись

latest_entry = json_data[-1]

## Записываем последнюю запись в отдельный файл

with open("vaccination_rus_latest.txt", "w") as file:
    file.write(str(latest_entry))

## Выводим интересующие данные в форматированный принт
    
print(f'Последние данные по вакцинации в России: \n \
Дата: {latest_entry["date"]} \n \
Полностью вакцинировано: {latest_entry["people_fully_vaccinated"]} \n \
Процент полностью вакцинированных: {latest_entry["people_fully_vaccinated_per_hundred"]} \n \
Вакцинаций в день на миллион человек: {latest_entry["daily_vaccinations_per_million"]} \n \
Используемые вакцины: {latest_entry["vaccines"]}')

## 3c08ba7d24msh31782e821bc621bp134e51jsn3107d7f505fe

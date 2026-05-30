#API Attempt

import requests

def city_comp():
    city_dict = {}
    while True:
        x = input('please input a city name with the first letter being a capital letter, or press enter to start comparison')
        if x == '':
            break
        x_response = requests.get(f'https://wttr.in/{x}?format=j1')
        if x_response.status_code != 200:
            print('please input a correct city name')   
        else:
            city_data = x_response.json()
            city_dict[x] = {'temp' : city_data['current_condition'][0]['temp_C'], 
                        'humidity' : city_data['current_condition'][0]['humidity'],
                        'precipMM' : city_data['current_condition'][0]['precipMM']}
        
    high_temp = max(city_dict, key=lambda city : city_dict[city]['temp'])
    high_precip = max(city_dict, key=lambda city : city_dict[city]['precipMM'])
    high_humid = max(city_dict, key=lambda city : city_dict[city]['humidity'])
    return f'In {high_temp} the temperature is highest, as it is {city_dict[high_temp]["temp"]} degrees celsius.\nIn {high_precip} the precipitation is the highest, being {city_dict[high_temp]["precipMM"]}mm.\nIn {high_humid} the humidity is highest at {city_dict[high_temp]["humidity"]}%'

print(city_comp())      



    
    


from flask import Flask, render_template, request
from API_weather_fetcher import city_comp
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    city_input = request.form.get('city')
    city_dict = {}
    x_clean = [z.strip() for z in city_input.split(',')]
    for i in x_clean:
        i_response = requests.get(f'https://wttr.in/{i}?format=j1')
        if i_response.status_code != 200:
            pass
        else:
            city_data = i_response.json()
            city_dict[i] = {'temp' : city_data['current_condition'][0]['temp_C'], 
                        'humidity' : city_data['current_condition'][0]['humidity'],
                        'precipMM' : city_data['current_condition'][0]['precipMM']}
    high_temp = max(city_dict, key=lambda city : city_dict[city]['temp'])
    high_precip = max(city_dict, key=lambda city : city_dict[city]['precipMM'])
    high_humid = max(city_dict, key=lambda city : city_dict[city]['humidity'])
    return render_template('results.html', 
    high_temp=high_temp,
    temp=city_dict[high_temp]['temp'],
    high_humid=high_humid,
    humid=city_dict[high_humid]['humidity'],
    high_precip=high_precip,
    precip=city_dict[high_precip]['precipMM'])

if __name__ == '__main__':
    app.run(debug=True)
from django.shortcuts import render


# Create your views here.
def home(request):
    # http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=787109E0-CF60-48A6-A2CA-47A18E7B50ED
    import json
    import requests

    if request.method == "POST":
        zipcode = (request.POST['zipcode'])
        api_req = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json"
                               "&zipCode=" + zipcode + "&distance=5&API_KEY=787109E0-CF60-48A6-A2CA-47A18E7B50ED")

        try:
            api = json.loads(api_req.content)
        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == 'Good':
            category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or " \
                                   "no risk. "
        elif api[0]['Category']['Name'] == 'Moderate':
            category_description = "(51-100) Air quality is acceptable however, for some pollutants there may be a " \
                                   "moderate health concern for a very samll numver of people who usually very " \
                                   "sensitive " \
                                   "to air pollution "
        elif api[0]['Category']['Name'] == 'USG':
            category_description = "(101-150) Although general public is not likely to br affected at this AQI range, " \
                                   "people with lung disease, older adults and children are at a greater risk from " \
                                   "exposure to ozone, whereas persons with heart and lung disease, older adults and " \
                                   "children are at greater risk from the presence of particles in the air. "
        elif api[0]['Category']['Name'] == 'Unhealthy':
            category_description = "(151-200) everyone may begin to experience health effects; members of sensitive " \
                                   "groups may experience more serious health effects. "
        elif api[0]['Category']['Name'] == 'Very Unhealthy':
            category_description = "(201-250) Health alert: everyone may experience more serious health effects"
        elif api[0]['Category']['Name'] == 'Ha':
            category_description = "(251-300) Health warning of emergency conditions. The entire population is more " \
                                   "likely to be affcted. "

    else:
        api_req = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5"
            "&API_KEY=787109E0-CF60-48A6-A2CA-47A18E7B50ED")

        try:
            api = json.loads(api_req.content)

        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == 'Good':
            category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or " \
                                   "no risk. "
        elif api[0]['Category']['Name'] == 'Moderate':
            category_description = "(51-100) Air quality is acceptable however, for some pollutants there may be a " \
                                   "moderate health concern for a very samll numver of people who usually very " \
                                   "sensitive " \
                                   "to air pollution "
        elif api[0]['Category']['Name'] == 'USG':
            category_description = "(101-150) Although general public is not likely to br affected at this AQI range, " \
                                   "people with lung disease, older adults and children are at a greater risk from " \
                                   "exposure to ozone, whereas persons with heart and lung disease, older adults and " \
                                   "children are at greater risk from the presence of particles in the air. "
        elif api[0]['Category']['Name'] == 'Unhealthy':
            category_description = "(151-200) everyone may begin to experience health effects; members of sensitive " \
                                   "groups may experience more serious health effects. "
        elif api[0]['Category']['Name'] == 'Very Unhealthy':
            category_description = "(201-250) Health alert: everyone may experience more serious health effects"
        elif api[0]['Category']['Name'] == 'Ha':
            category_description = "(251-300) Health warning of emergency conditions. The entire population is more " \
                                   "likely to be affcted. "
    return render(request, 'home.html', {'api': api, 'category_description': category_description})


def about(request):
    return render(request, 'about.html')

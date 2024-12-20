import requests



url = 'https://assets.ithillel.ua/images/icons/courses-reach/_transform_icon64_2x/qa-python.png'
# response = requests.get(url)
#
# with open('random_image.png', 'wb') as p:
#     p.write(response.content)


with open('random_image.png', 'rb') as p:
    data = {'file_name': p}

requests.post(url, files=data)
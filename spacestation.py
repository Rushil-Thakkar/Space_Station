import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("People in space :", result['number'])
people = result['people']

for pep in people:
    print(pep['name'])

url1 = 'http://api.open-notify.org/iss-now.json'
response1 = urllib.request.urlopen(url1)
result1 = json.loads(response1.read())

location = result1['iss_position']
lat = location['latitude']
log = location['longitude']
print('lat :', lat)
print('long :', log)

screen = turtle.Screen()
screen.setup(700, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.jpg')

screen.register_shape("iss.png")
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

iss.penup()
iss.goto(lat, log)
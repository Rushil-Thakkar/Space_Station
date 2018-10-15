### Space Station (Python, Turtle, json, urllib)
- Created python application which demonstrate the use of a web service that helps to 
  find out the current location of the International Space Station (ISS). 
- The whole plot with its location is placed on the map.
- Worked with python features like turtle, Json and urllib.
- Open URL is provided by NASA which gives the live data in JSON format that we can integrate and use.

## Steps to run the program
> Lets assume you already have python installed.

- In the terminal, Go up to the folder directory.
```
    python practice.py

```

- GUI window will open up with map already loaded in the window.

```
    screen = turtle.Screen()
    screen.setup(700, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.jpg')

```

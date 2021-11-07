import csv
import pandas as pd

rows = []
gravity=[]

with open('final.csv', 'r') as f:
    csv_r = csv.reader(f)
    for i in csv_r:
        rows.append(i)
headers = rows[0]
data = rows[1:]
headers[0] = 'Index'

star_data = []
for star in data:
    if star[3] != '?': 
        star[3] = float(star[3].strip("\'"))*1.989e+30
    
    if star[4] != '?':
        star[4] = float(star[4].strip("\'"))*6.957e+8
    star_data.append(star)

radius = []
radius.append(star[3])
mass = []
mass.append(star[4])

def gravity_calculation(radius,mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g= (mass[index]*G)/((radius[index])**2)
        gravity.append(g)
        
gravity_calculation(radius,mass)


name = []
distance = []
for i in gravity:
    name.append(i[1])
    distance.append(i[2])
    mass.append(i[3])
    radius.append(i[4])
    gravity.append(i[5])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"]
)
df.to_csv('final.csv')

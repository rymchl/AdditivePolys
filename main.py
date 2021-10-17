from PIL import Image, ImageDraw
import math

#connects all of the points given with lines.
def connect_points(points, draw, i):
    for i in range(len(points)):
        for j in range(i, len(points)):
            ifac = int(float(i/20)*255);
            draw.line((points[i], points[j]), fill=(ifac, 122 + int(ifac/2), 255-ifac), width=1)
            
#returns the point in screenspace based on given T=theta
def get_point(T):
    return (500 + 500*math.cos(T),500 + 500*math.sin(T))

#Gets all n points to form the polygon 
def get_points(n):
    x = 2 * math.pi / n
    points = []
    for i in range(n):
        points.append(get_point(i*x))
    return points
    
#instantiating image
im = Image.new('RGB', (1000,1000), (0, 0, 0))
draw = ImageDraw.Draw(im)

#displays 20 images, iteratively showing the formation of the curves.
for i in range(1,20):
    points = get_points(i)
    connect_points(points,draw, i*255/20)
im.show() #indent this to see the continuous formation of this shape.





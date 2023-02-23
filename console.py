from math import pow, sin, cos, sqrt, acos, pi

x = 119
y = 30
aspect = x / y
pixel_aspect = 19 / 39
# shades = " .:!/r(l1Z4H9W8$@"
shades = " .*/?9#&@"

def clamp(value, min1, max1):
    return(min(max(value, min1), max1))

def dist(vec1, vec2):
    return sqrt(pow(vec2[0] - vec1[0], 2) + pow(vec2[1] - vec1[1], 2) + pow(vec2[2] - vec1[2], 2))

def mag(vec):
    return dist((0, 0, 0), vec)

def dot(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]

def angle(vec1, vec2):
    return acos(dot(vec1, vec2) / (mag(vec1) * mag(vec2)))

def map(value, min_in, max_in, min_out, max_out):
    return min_out + ((max_out - min_out) / (max_in - min_in) * (value - min_in))

def sphere_dist(point, centre, radius):
    return dist(point, centre) - radius

def add(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2])
def subtract(vec1, vec2):
    return (vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2])

def draw_ray():
    for t in range(10000):
        draw_string = ""
        for i in range(y):
            for j in range(x):
                u = j / x * 2 - 1
                v = i / y * 2 - 1
                u *= aspect * pixel_aspect

                sphere_origin = (0, 0, 5)
                radius = 7
                light = (sin(t * 0.01) * 5, -5, cos(t * 0.01) * 5)
                pixel = " "

                ray = (u * 10, v * 10, 0)
                hit = False
                for ii in range(10):
                    ray = (u * 10, v * 10, sphere_dist(ray, sphere_origin, radius))
                    if (sphere_dist(ray, sphere_origin, radius) < 1):
                        hit = True
                        break
                if (hit):
                    pixel = shades[round(map(angle(subtract(ray, sphere_origin), light), 0, pi, len(shades) - 1, 0))]
                    # break
                draw_string += pixel
                    
            draw_string += "\n"
        print(draw_string)


# draw()
# print(map(angle((-1, 0, 0), (1, 0, 0)), 0, pi, 0, 180))
draw_ray()
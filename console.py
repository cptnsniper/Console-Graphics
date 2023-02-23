from math import pow, sin, cos, sqrt

x = 119
y = 30
aspect = x / y
pixel_aspect = 19 / 39
shades = " .:!/r(l1Z4H9W8$@"

def clamp(value, mini, maxi):
    return(min(max(value, mini), maxi))

def dist(vec1, vec2):
    return sqrt(pow(vec2[0] - vec1[0], 2) + pow(vec2[1] - vec1[1], 2) + pow(vec2[2] - vec1[2], 2))

def draw():
    for t in range(10000):
        draw_string = ""
        for i in range(y):
            for j in range(x):
                u = j / x * 2 - 1
                v = i / y * 2 - 1
                u *= aspect * pixel_aspect

                u += sin(t * 0.02)
                v += cos(t * 0.02)

                color = clamp((1 - (pow(u, 2) + pow(v, 2)) / (pow(1 * aspect * pixel_aspect, 2) + 1)) * (len(shades) - 1), 0, len(shades) - 1)

                draw_string += shades[round(color)]
                
            draw_string += "\n"
        print(draw_string)

def draw_ray():
    draw_string = ""
    for i in range(y):
        for j in range(x):
            u = j / x * 2 - 1
            v = i / y * 2 - 1
            u *= aspect * pixel_aspect

            # camera_start = (u, v, 0)
            sphere_origin = (0, 0, 5)
            pixel = " "

            # for i in range(100):
            ray = (u * 10, v * 10, 0)
            ray = (u * 10, v * 10, dist(ray, sphere_origin))
            if (dist(ray, sphere_origin) < 5):
                pixel = "@"
                # break
            draw_string += pixel
                
        draw_string += "\n"
    print(draw_string)


# draw()
draw_ray()
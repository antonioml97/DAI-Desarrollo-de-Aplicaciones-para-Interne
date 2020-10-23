import random
def generarColorHexadecimal():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return '#%02X%02X%02X' % (r,g,b)
def svg():
    formas=['rect','circle','ellipse']

    forma = random.choice(formas)
    cadena = '<svg width=400 height=400>'

    if forma == 'rect':
        width = random.randint(0,400)
        height = random.randint(0,400)

        color_relleno = generarColorHexadecimal()
        color_linea = generarColorHexadecimal()

        cadena+='<rect width="{}" height="{}" style="fill:{};stroke-width:3;stroke:{}" />'.format(width,height,color_relleno,color_linea)


    elif forma == 'circle':
        cx = random.randint(0,400)
        cy = random.randint(0,400)
        r = random.randint(0,200)

        color_relleno = generarColorHexadecimal()
        color_linea = generarColorHexadecimal()

        cadena+='<circle cx="{}" cy="{}" r="{}" stroke="{}" stroke-width="3" fill="{}" />'.format(cx,cy,r,color_linea,color_relleno)

    elif forma == 'ellipse':
        cx = random.randint(0,400)
        cy = random.randint(0,400)
        rx = random.randint(0,200)
        ry = random.randint(0,200)

        color_relleno = generarColorHexadecimal()
        color_linea = generarColorHexadecimal()

        cadena += '<ellipse cx="{}" cy="{}" rx="{}" ry="{}" style="fill:{};stroke:{};stroke-width:2" />'.format(cx,cy,rx,ry,color_relleno,color_linea)

    return cadena
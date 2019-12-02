from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time

start = False

width,height = 1200,1200
m1 = 5
m2 = 5
u =  0


t = 0
g= 9.8
accln = (m2 * g - u * m1 * g) / (m1 + m2)
# For m1
x2, y2 = -0.5, 0.125
x1, y1 = -0.625, 0

# For m2
X2, Y2 = 0.125, -0.3025
X1, Y1 = 0, -0.425


# Scaling factor
k = 900
p = 0
q = 0



def draw():
    global x1, x2, t, Y1, Y2, l1, l2, L1, L2,p,q

    #-------------------------------------------------------------
    if m1 <= 5:
        p = 0.05
    elif m1 > 5 and m1 <= 7:
        p = 0.04
    elif m1 > 7 and m1 < 10:
        p = 0.03
    elif m1 >= 10 and m1 < 13:
        p = 0.02
    elif m1 > 12 and m1 <= 14:
        p = 0.01
    elif m1 == 15:
        p = 0

    if m2 <= 5:
        q = 0.05
    elif m2 > 5 and m2 <= 7:
        q = 0.04
    elif m2 > 7 and m2 < 10:
        q = 0.03
    elif m2 >= 10 and m2 < 13:
        q = 0.02
    elif m2 > 12 and m2 <= 14:
        q = 0.01
    elif m2 == 15:
        q = 0
    #-------------------------------------------------------------

    print(t)
    if accln > 0 :
        a = accln * math.pow(t, 2)
        v = accln * t
        #print(a)
    else:
        a = 0


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear screen buffer
    glColor(1.0,1.0,0.0,0.0)

    flag = False
    # Horizontal movement
    if (x1 - a / k) < -0.0625 * 3 :
        x1 += a / k
        x2 += a / k
        # For tension line 1
        l1, l2 = x2 - a  / k, 0.0625
        flag = True
        if start:
            t += 0.005
    # Drawing mass 1
    glRectf(x1 -  a / k +  p, y1, x2 - a / k, y2 - p)

    # Vertical movement
    if (Y1 - a / k) >= -0.875:
        Y1 -= a / k
        Y2 -= a / k
        #For tension line 2
        L1, L2 = 0.0625, Y2 - a / k
        if not flag:
            if start:
                t += 0.005
    # Drawing mass 2
    glRectf(X1 + q/2, Y1 - a / k + q/2, X2 - q/2, Y2 - a / k)

    # Drawing rectangular surface
    glBegin(GL_POLYGON)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(-0.125,0)
    glVertex2f(-0.875,0)
    glVertex2f(-0.875,-0.875)
    glVertex2f(-0.125,-0.875)
    glEnd()



    # Drawing Circle d=0.125, c(0.0625,0.0625)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = (i*3.14)/180
        r = 0.0625
        glVertex2f((r*math.cos(theta)),(r*math.sin(theta)))
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.125,0)
    glVertex2f(0.0,0.0)
    glVertex2f(0.0,0.0)
    glVertex2f(-0.125,-0.024)
    glEnd()

    # Drawing tension lines
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(l1,l2)
    glVertex2f(0,0.0625)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(0.0625,0)
    glVertex2f(L1,L2)
    glEnd()


    display_text(-0.3, 0.9, GLUT_BITMAP_TIMES_ROMAN_24, "HORIZONTAL PULLEY WITH FRICTION.", (0, 255, 0))
    display_text(x2-0.09, y2+0.01, GLUT_BITMAP_TIMES_ROMAN_24, "m1 = "+str(m1)+" kg", (0, 255, 0))
    display_text(X2 + 0.01, Y2 - 0.04, GLUT_BITMAP_TIMES_ROMAN_24, "m2 = "+str(m2)+" kg", (0, 255, 0))
    display_text(0.3, 0.7, GLUT_BITMAP_TIMES_ROMAN_24, "Acceleration = ", (0, 255, 0))
    display_text(0.6, 0.7, GLUT_BITMAP_TIMES_ROMAN_24, str(round(accln, 2)) + " m/s^2", (255, 255, 255))
    display_text(0.3, 0.6, GLUT_BITMAP_TIMES_ROMAN_24, "Distance = ", (0, 255, 0))
    display_text(0.6, 0.6, GLUT_BITMAP_TIMES_ROMAN_24, str(round(a,2)) + " m", (255, 255, 255))
    display_text(0.3, 0.5, GLUT_BITMAP_TIMES_ROMAN_24, "Coefficient of friction = ", (0, 255, 0))
    display_text(0.7, 0.5, GLUT_BITMAP_TIMES_ROMAN_24, str(round(u, 2)), (255, 255, 255))
    display_text(0.3, 0.4, GLUT_BITMAP_TIMES_ROMAN_24, "Time = ", (0, 255, 0))
    display_text(0.6, 0.4, GLUT_BITMAP_TIMES_ROMAN_24, str(round(t, 2)) + " seconds", (255, 255, 255))
    display_text(0.3, 0.3, GLUT_BITMAP_TIMES_ROMAN_24, "Velocity = ", (0, 255, 0))
    display_text(0.6, 0.3, GLUT_BITMAP_TIMES_ROMAN_24, str(round(v, 2)) + " m/s", (255, 255, 255))
    display_text(-0.6, 0.7, GLUT_BITMAP_TIMES_ROMAN_24, "KEY ", (255, 255, 255))
    display_text(-0.4, 0.7, GLUT_BITMAP_TIMES_ROMAN_24, "FUNCTION", (0, 255, 0))
    display_text(-0.6, 0.65, GLUT_BITMAP_TIMES_ROMAN_24, "w ", (0, 255, 0))
    display_text(-0.4, 0.65, GLUT_BITMAP_TIMES_ROMAN_24, "Increase m1", (255, 255, 255))
    display_text(-0.6, 0.6, GLUT_BITMAP_TIMES_ROMAN_24, "s ", (0, 255, 0))
    display_text(-0.4, 0.6, GLUT_BITMAP_TIMES_ROMAN_24, "Decrease m1", (255, 255, 255))
    display_text(-0.6, 0.55, GLUT_BITMAP_TIMES_ROMAN_24, "a ", (0, 255, 0))
    display_text(-0.4, 0.55, GLUT_BITMAP_TIMES_ROMAN_24, "Decrease m2", (255, 255, 255))
    display_text(-0.6, 0.5, GLUT_BITMAP_TIMES_ROMAN_24, "d ", (0, 255, 0))
    display_text(-0.4, 0.5, GLUT_BITMAP_TIMES_ROMAN_24, "Increase m2", (255, 255, 255))
    display_text(-0.6, 0.45, GLUT_BITMAP_TIMES_ROMAN_24, "j ", (0, 255, 0))
    display_text(-0.4, 0.45, GLUT_BITMAP_TIMES_ROMAN_24, "Decrease coeff. of friction", (255, 255, 255))
    display_text(-0.6, 0.4, GLUT_BITMAP_TIMES_ROMAN_24, "k ", (0, 255, 0))
    display_text(-0.4, 0.4, GLUT_BITMAP_TIMES_ROMAN_24, "Increase coeff. of friction", (255, 255, 255))
    display_text(-0.6, 0.35, GLUT_BITMAP_TIMES_ROMAN_24, "q ", (0, 255, 0))
    display_text(-0.4, 0.35, GLUT_BITMAP_TIMES_ROMAN_24, "To start", (255, 255, 255))
    display_text(-0.6, 0.3, GLUT_BITMAP_TIMES_ROMAN_24, "r ", (0, 255, 0))
    display_text(-0.4, 0.3, GLUT_BITMAP_TIMES_ROMAN_24, "To reset", (255, 255, 255))
    display_text(0.3, -0.7, GLUT_BITMAP_TIMES_ROMAN_24, "Bipesh Subedi ", (255, 255, 255))
    display_text(0.3, -0.75, GLUT_BITMAP_TIMES_ROMAN_24, "Roll No : 54 ", (255, 255, 255))
    display_text(0.3, -0.8, GLUT_BITMAP_TIMES_ROMAN_24, "Computer Graphics mini project", (255, 255, 255))


    # t += 0.005
    glFlush()

def reset():
    global m1,m2,u,t,accln,x1,y1,x2,y2,X1,Y1,X2,Y2,k,p,q
    m1 = 5
    m2 = 5
    u = 0.1

    t = 0

    accln = (m2 * g - u * m1 * g) / (m1 + m2)
    # For m1
    x2, y2 = -0.5, 0.125
    x1, y1 = -0.625, 0

    # For m2
    X2, Y2 = 0.125, -0.3025
    X1, Y1 = 0, -0.425

    # Scaling factor
    k = 900
    p = 0
    q = 0


def Timer(x):
    glutPostRedisplay()
    glutTimerFunc(100, Timer, 0)

def mouse(button, state,x , y):
    print(x, y)

def keyboard(key, x, y):
    global m1,m2,start,u
    char = key.decode("utf-8")
    if start == False:
        if char == "w":
            if m1 < 15:
                m1+=1
        if char == "s":
            if  m1>6:
                m1-= 1
        if char == "d":
            if  m2 < 15:
                m2+=1
        if char == "a":
            if  m2>5:
                m2-= 1
        if  char == "k":
            if u<0.9:
                u+=0.1
        if  char == "j":
            if u >=0.1:
                u-=0.1


    if char == "q" :
        start = True
    if char == "r":
        reset()
        start = False



def display_text(x,  y,  font,  text, color):
        glColor3ub(color[0], color[1], color[2])

        glRasterPos2f(x, y)
        for ch in text:

            glutBitmapCharacter(font, ctypes.c_int(ord(ch)))




if __name__ == "__main__":
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(width,height)
        glutInitWindowPosition(200,200)
        glutCreateWindow("Horizontal Pulley")
        glutDisplayFunc(draw)
        glutKeyboardFunc(keyboard)
        glutMouseFunc(mouse)
        #Text(0.5,0.5,"Horizontal Pulley")
        Timer(0)
        glutMainLoop()

from math import sin, cos, radians
import turtle

class Triangle:
    default_color = "DeepPink3"

    def __init__(self, x1, y1, x2, y2):
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self.color = Triangle.default_color
        self.position = (0, 0)
        self.rotation = 0
        self.scale = (1, 1)

    def set_position(self, x, y):
        self.position = (x, y)

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def set_color(self, color):
        self.color = color

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_rotation_degree(self, degree):
        self.rotation = radians(degree)

    def rotationMatrix(self):
        fi = self.rotation
        return [
            [cos(fi), -sin(fi)],
            [sin(fi), cos(fi)]
        ]

    @staticmethod
    def multMatrixVector(M, v):
        turnedVertex = [0, 0]
        turnedVertex[0] = M[0][0] * v[0] + M[0][1] * v[1]
        turnedVertex[1] = M[1][0] * v[0] + M[1][1] * v[1]
        return turnedVertex

    @staticmethod
    def scaleVertex(vertex, scale):
        return scale[0] * vertex[0], scale[1] * vertex[1]

    def calc_abs_pos(self):
        scaledVertex1 = Triangle.scaleVertex(self._vertex1, self.scale)
        scaledVertex2 = Triangle.scaleVertex(self._vertex2, self.scale)
        M = self.rotationMatrix()
        turnedVertex1 = Triangle.multMatrixVector(M, scaledVertex1)
        turnedVertex2 = Triangle.multMatrixVector(M, scaledVertex2)

        v1 = (self.position[0] + turnedVertex1[0], self.position[1] + turnedVertex1[1])
        v2 = (self.position[0] + turnedVertex2[0], self.position[1] + turnedVertex2[1])
        return v1, v2

    def draw(self):
        v1, v2 = self.calc_abs_pos()
        turtle.color(self.color)
        turtle.up()
        turtle.setpos(*self.position)
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.setpos(*self.position)
        turtle.up()
        turtle.color(Triangle.default_color)

if __name__ == '__main__':
    turtle.speed(0)
    triangle = Triangle(100, 100, 100, 0)
    turtle.hideturtle()  # Приховати черепаху перед анімацією

    for degree in range(0, 360, 3):
        turtle.clear()
        triangle.set_rotation_degree(degree)
        triangle.draw()

    turtle.showturtle()
    turtle.mainloop()

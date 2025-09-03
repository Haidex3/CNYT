import math

# Function: Addition of two complex numbers
def add(a, b):
    real_part = a[0] + b[0]
    imaginary_part = a[1] + b[1]
    return (real_part, imaginary_part)


# Function: Multiplication of two complex numbers
def multiply(a, b):
    real_part = a[0] * b[0] - a[1] * b[1]
    imaginary_part = (a[0] * b[1]) + (a[1] * b[0])
    return (real_part, imaginary_part)


# Function: Subtraction of two complex numbers
def subtract(a, b):
    real_part = a[0] - b[0]
    imaginary_part = a[1] - b[1]
    return (real_part, imaginary_part)


# Function: Division of two complex numbers
def divide(a, b):
    denominator = b[0] ** 2 + b[1] ** 2
    if denominator != 0:
        real_part = ((a[0] * b[0]) + (a[1] * b[1])) / denominator
        imaginary_part = ((a[1] * b[0]) - (a[0] * b[1])) / denominator
        return (real_part, imaginary_part)


# Function: Modulus (magnitude) of a complex number
def modulus(a):
    return (a[0] ** 2 + a[1] ** 2) ** 0.5


# Function: Conjugate of a complex number
def conjugate(a):
    if a[1] != 0:
        return (a[0], -a[1])
    else:
        return (a[0], 0)


# Function: Polar representation of a complex number
def polar(a):
    magnitude = (a[0] ** 2 + a[1] ** 2) ** 0.5
    angle = math.atan(a[1] / a[0])  
    real_part = magnitude * math.cos(angle)
    imaginary_part = magnitude * math.sin(angle)
    return (real_part, imaginary_part)


# Function: Phase (angle) of a complex number
def phase(c1):
    slope = c1[1] / c1[0]
    angle = math.atan(slope)  
    return angle

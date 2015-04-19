import math
import random
print 'Welcome to Python Calculator'
print 'Please pick a Category'
print 'Category 1: Basic Functions'
print 'Category 2: Advanced Functions'
print 'Category 3: Trigonometry'
print 'Category 4: Equations'
print 'Category 5: Geometry'
print 'Category 6: Finance'
category = int(raw_input('What is your category choice?'))
if category !=1 and category !=2 and category !=3 and category !=4 and category !=5 and category !=6:
    print 'Please make a valid selection'
    quit
if category == 1:
    print 'You have selected Category 1'
    print 'Please choose an option'
    print 'Option 1: Addition'
    print 'Option 2: Subtraction'
    print 'Option 3: Multiplication'
    print 'Option 4: Division'
    print 'Option 5: Exponents'
    print 'Option 6: Logarithms'
    option = int(raw_input('Please select an option'))
    if option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6:
        print 'Please pick a valid option'
        quit
    first_number = float(raw_input('What is your first number?'))
    second_number = float(raw_input('What is your second number'))
    if option == 1:
        addition = first_number + second_number
        print addition
    if option == 2:
        subtraction = first_number - second_number
        print subtraction
    if option == 3:
        multiplication = first_number * second_number
        print multiplication
    if option == 4:
        division = first_number / second_number
        print division
    if option == 5:
        exponents = first_number ** second_number
        print exponents
    if option == 6:
        logarithm = math.log(second_number, first_number)
if category == 2:
    print 'You have selected Category 2'
    print 'Please select an option'
    print 'Option 1: Absolute Value'
    print 'Option 2: Square Root'
    option = int(raw_input('Please select an option'))
    if option != 1 and option != 2:
        print 'Please select a valid option'
        quit
    number = float(raw_input('What is your number'))
    if option == 1:
        absolute_value = math.fabs(number)
        print absolute_value
    if option == 2:
        square_root = math.sqrt(number)
        print square_root
if category == 3:
    print 'You have selected Category 3'
    print 'Please select an option'
    print 'Option 1: Sine'
    print 'Option 2: Cosine'
    print 'Option 3: Tangent'
    print 'Option 4: Cosecant'
    print 'Option 5: Secant'
    print 'Option 6: Cotangent'
    print 'Option 7: Convert Degrees to Radians'
    print 'Option 8: Convert Radians to Degrees'
    option = int(raw_input('Please select an option'))
    if option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and  option != 6 and option != 7 and option != 8:
        print 'Please select a valid option'
        quit
    number = float(raw_input('What is your number (in radians)?'))
    if option == 1:
        sine = math.sin(number)
        print sine
    if option == 2:
        cosine = math.cos(number)
        print cosine
    if option == 3:
        tangent = math.tan(number)
        print tangent
    if option == 4:
        sine = math.sin(number)
        cosecant = 1 / sine
        print cosecant
    if option == 5:
        cosine = math.cos(number)
        secant = 1 / cosine
        print secant
    if option == 6:
        tangent = math.tan(number)
        cotangent = 1 / tangent
        print cotangent
    if option == 7:
        radians = math.radians(number)
        print radians
    if option == 8:
        degrees = math.degrees(number)
        print degrees
if category == 4:
    print 'You have selected Category 4'
    print 'Please select an option'
    print 'Option 1: Quadratic Formula'
    print 'Option 2: Random Number Generator'
    print 'Option 3: Pythagorean Theroem'
    option = int(raw_input('What is your selection?'))
    if option != 1 and option != 2 and option != 3:
        print 'Please make a valid selection'
        quit
    if option == 1:
        a = float(raw_input('What is the a value?'))
        b = float(raw_input('What is the b value?'))
        c = float(raw_input('What is the c value?'))
        part_aa = -1 * b
        part_ab = 2 * a
        part_a = part_aa / part_ab
        part_ba = b ** 2
        part_bb = -4 * a
        part_bc = part_bb * c
        part_bd = part_ba + part_bc
        if part_bd < 0:
            print 'undefined'
        else:
            part_be = math.sqrt(part_bd)
            part_b = part_be / part_ab
            first_x = part_a + part_b
            second_x = part_a - part_b
            print first_x
            print second_x
    if option == 2:
        first_number = float(raw_input('What is the start of your range?'))
        second_number = float(raw_input('What is the end of your range'))
        print random.randint(first_number,second_number)
    if option == 3:
        missing_value = raw_input('What is the number you are looking for (a, b, or c)?')
    if missing_value == 'a':
        b_value = float(raw_input('What is the b value?'))
        c_value = float(raw_input('What is the c value?'))
        c_value_squared = c_value ** 2
        b_value_squared = b_value ** 2
        a_value_squared = c_value_squared - b_value_squared
        a_value = math.sqrt(a_value_squared)
        print a_value
    if missing_value == 'b':
        a_value = float(raw_input('What is the a value?'))
        c_value = float(raw_input('What is the c value?'))
        c_value_squared = c_value ** 2
        a_value_squared = a_value ** 2
        b_value_squared = c_value_squared - a_value_squared
        b_value = math.sqrt(b_value_squared)
        print b_value
    if missing_value == 'c':
        a_value = float(raw_input('What is the a value?'))
        b_value = float(raw_input('What is the b value?'))
        a_value_squared = a_value ** 2
        b_value_squared = b_value ** 2
        c_value_squared = a_value_squared + b_value_squared
        c_value = math.sqrt(c_value_squared)
        print c_value
    if missing_value != 'a' and missing_value != 'b' and missing_value != 'c':
        print 'Please pick either a, b, or c.'
if category == 5:
    print 'You have selected Category 5'
    print 'Please select an option'
    print 'Option 1: Rectangle'
    print 'Option 2: Triangle'
    print 'Option 3: Circle'
    print 'Option 4: Sphere'
    print 'Option 5: Cone'
    print 'Option 6: Rectangular Prism'
    print 'Option 7: Cylinder'
    option = int(raw_input('What option do you choose?'))
    if option != 1 and option !=2 and option != 3 and option != 4 and option != 5 and option != 6 and option != 7:
        print 'Please select a valid option'
        quit
    if option == 1:
        print 'You have selected Option 1: Rectangle'
        print 'Please select what part of the rectangle you want to find'
        print 'Part 1: Perimeter'
        print 'Part 2: Area'
        print 'Part 3: Length of Diagonals'
        part = int(raw_input('What part of the rectangle do you want to find?'))
        if part != 1 and part != 2 and part != 3:
            print 'Please select a valid part'
            quit
        first_side = float(raw_input('What is the length of the rectangle?'))
        second_side = float(raw_input('What is the width of the rectangle?'))
        if part == 1:
            length = first_side * 2
            width = second_side * 2
            perimeter = length + width
            print 'The perimeter is', perimeter
        if part == 2:
            area = first_side * second_side
            print 'The area is', area
        if part == 3:
            first_side_squared = first_side ** 2
            second_side_squared = second_side ** 2
            diagonal_squared = first_side_squared + second_side_squared
            diagonal = math.sqrt(diagonal_squared)
            print 'The diagonal is', diagonal
    if option == 2:
        print 'You have selected Option 2: Triangle'
        print 'Please select what part of the triangle you want to find'
        print 'Part 1: Area'
        print 'Part 2: Perimeter'
        part = int(raw_input('What part of the triangle do you want to find?'))
        if part != 1 and part != 2:
            print 'Please select a valid part'
            quit
        if part == 1:
            base = float(raw_input('What is the base of the triangle?'))
            height = float(raw_input('What is the height of the triangle?'))
            double_area = base * height
            area = double_area / 2
            print 'The area is', area
        if part == 2:
            first_side = float(raw_input('What is the length of the first side?'))
            second_side = float(raw_input('What is the length of the second side?'))
            third_side = float(raw_input('What is the length of the third side?'))
            perimeter = first_side + second_side + third_side
            print 'The perimeter is', perimeter
    if option == 3:
        print 'You have selected Option 3: Circle'
        print 'Please select what part of the triangle you want to find'
        print 'Part 1: Area'
        print 'Part 2: Circumference'
        part = int(raw_input('What is your selection?'))
        if part != 1 and part != 2:
            print 'Please make a valid selection'
            quit
        radius = float(raw_input('What is the radius of the circle?'))
        if part == 1:
            radius_squared = radius ** 2
            area = math.pi * radius_squared
            print 'The area is', area
        if part == 2:
            circumference = 2 * math.pi * radius
            print 'The circumference is', circumference
    if option == 4:
        print 'You have selected Option 4: Sphere'
        print 'Please select a part of the sphere'
        print 'Part 1: Volume'
        print 'Part 2: Surface Area'
        part = int(raw_input('What part do you select?'))
        if part != 1 and part != 2:
            print 'Please make a valid selection'
            quit
        radius = float(raw_input('What is the radius of the sphere?'))
        if part == 1:
            radius_cubed = radius ** 3
            four_thirds = 4 / 3
            volume = four_thirds * math.pi * radius_cubed
            print 'The volume is', volume
        if part == 2:
            radius_squared = radius ** 2
            surface_area = 4 * math.pi * radius_squared
            print 'The surface area is', surface_area
    if option == 5:
        print 'You have selected Option 5: Cone'
        print 'Please select a part of the cone'
        print 'Part 1: Volume'
        print 'Part 2: Surface Area'
        part = int(raw_input('What part do you select?'))
        if part != 1 and part != 2:
            print 'Please make a valid selection'
            quit
        radius = float(raw_input('What is the radius of the cone?'))
        height = float(raw_input('What is the height of the cone?'))
        if part == 1:
            new_height = height / 3
            radius_squared = radius ** 2
            volume = math.pi * new_height * radius_squared
            print 'The volume is', volume
        if part == 2:
            height_squared = height ** 2
            radius_squared = radius ** 2
            part_e = height_squared + radius_squared
            part_ee = math.sqrt(part_e)
            part_ef = radius + part_ee
            surface_area = math.pi * radius * part_ef
            print 'The surface area is', surface_area
    if option == 6:
        print 'You have selected Option 6: Rectangular Prism'
        print 'Please select a part of the rectangular prism'
        print 'Part 1: Volume'
        print 'Part 2: Surface Area'
        print 'Part 3: Diagonals'
        part = int(raw_input('What part do you select?'))
        if part != 1 and part != 2 and part != 3:
            print 'Please make a valid selection'
            quit
        length = float(raw_input('What is the length of the rectangular prism?'))
        width = float(raw_input('What is the width of the rectangular prism?'))
        height = float(raw_input('What is the height of the rectangular prism'))
        if part == 1:
            volume = length * width * height
            print 'The volume is', volume
        if part == 2:
            wl = width * length
            hl = height * length
            hw = height * width
            combined = wl + hl + hw
            surface_area = 2 * combined
            print 'The surface area is', surface_area
        if part == 3:
            length_squared = length ** 2
            width_squared = width ** 2
            height_squared = height ** 2
            combined = length_squared + width_squared + height_squared
            diagonal = math.sqrt(combined)
            print 'The diagonal is', diagonal
    if option == 7:
        print 'You have selected Option 7: Cylinder'
        print 'Please choose a part of the cylinder'
        print 'Part 1: Volume'
        print 'Part 2: Surface Area'
        part = int(raw_input('What part of the cylinder do you select?'))
        if part != 1 and part != 2:
            print 'Please make a valid input'
            quit
        height = float(raw_input('What is the height of the cylinder?'))
        radius = float(raw_input('What is the radius of the cylinder?'))
        if part == 1:
            radius_squared = radius ** 2
            volume = math.pi * radius_squared * height
            print 'The volume is', volume
        if part == 2:
            radius_squared = radius ** 2
            part_b = 2 * math.pi * radius_squared
            part_a = 2 * math.pi * radius * height
            surface_area = part_a + part_b
            print 'The surface area is', surface_area
if category == 6:
    print 'You have selected Category 6: Finance'
    print 'Option 1: Simple Interest'
    print 'Option 2: Compounded Interest'
    option = int(raw_input('What is your selection?'))
    if option != 1 and option != 2:
        print 'Please make a valid selection'
        quit
    if option == 1:
        print 'You have selected Option 1: Simple Interest'
        starting_value = float(raw_input('What is your starting value?'))
        interest_rate = float(raw_input('What is your interest rate?'))
        number_of_years = float(raw_input('How many years is interest collected'))
        second_interest = interest_rate / 100
        third_interest = second_interest + 1
        final_amount = starting_value * third_interest * number_of_years
        print 'Your final amount is', final_amount
    if option == 2:
        print 'You have selected Option 2: Compounded Interest'
        starting_value = float(raw_input('What is your starting value?'))
        interest_rate = float(raw_input('What is your interest rate?'))
        number_of_years = float(raw_input('How many years is interest compounded?'))
        print 'Please selected one of the following ways interest is compounded'
        print 'Term 1: Semi-Annually'
        print 'Term 2: Quarterly'
        print 'Term 3: Monthly'
        print 'Term 4: Weekly'
        print 'Term 5: Daily'
        term = int(raw_input('What is your term selection?'))
        if term != 1 and term != 2 and term != 3 and term != 4 and term != 5:
            print 'Please make a valid selection'
            quit
        if term == 1:
            compounding_per_year = 2
        if term == 2:
            compounding_per_year = 4
        if term == 3:
            compounding_per_year = 12
        if term == 4:
            compounding_per_year = 52
        if term == 5:
            compounding_per_year = 365
        second_interest = interest_rate / 100
        part_aa = second_interest / compounding_per_year
        part_ab = part_aa + 1
        part_b = compounding_per_year * number_of_years
        part_c = part_ab ** part_b
        final_amount = part_c * starting_value
        print 'Your final amount is', final_amount
print 'Thank you for using the Python Calculator!'
quit

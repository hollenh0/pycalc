import guiframework
continuance = 'true'
while continuance == 'true':
    print 'Thank you for using Python Calculator'
    print 'Please select a category'
    print 'Category 1: Basic Functions'
    print 'Category 2: Advanced Functions'
    print 'Category 3: Trigonometry'
    print 'Category 4: Equations'
    print 'Category 5: Geometry'
    print 'Category 6: Finance'
    print 'Category 7: Cancel'
    category = int(raw_input('What is your selection?'))
    if category != 1 and category != 2 and category != 3 and category != 4 and category != 5 and category != 6 and \
            category != 7:
        print 'Please select a valid option'
        continuance = 'false'
    if category == 1:
        print 'You have selected Category 1'
        print 'Please select a function'
        print 'Function 1: Addition'
        print 'Function 2: Subtraction'
        print 'Function 3: Multiplication'
        print 'Function 4: Division'
        print 'Function 5: Exponents'
        print 'Function 6: Logarithms'
        function = int(raw_input('What is your function?'))
        if function != 1 and function != 2 and function != 3 and function != 4 and function != 5 and function != 6:
            print 'Please select a valid option'
            continuance = 'false'
        first_number = float(raw_input('What is your first number?'))
        second_number = float(raw_input('What is your second number?'))
        if function == 1:
            print guiframework.addition(first_number, second_number)
        if function == 2:
            print guiframework.subtraction(first_number, second_number)
        if function == 3:
            print guiframework.multiplication(first_number, second_number)
        if function == 4:
            print guiframework.division(first_number, second_number)
        if function == 5:
            print guiframework.exponenets(first_number, second_number)
        if function == 6:
            print guiframework.logarithm(first_number, second_number)
    if category == 2:
        print 'You have selected Category 2'
        print 'Please select a function'
        print 'Function 1: Absolute Value'
        print 'Function 2: Square Root'
        function = int(raw_input('What is your function?'))
        if function != 1 and function != 2:
            print 'Please select a valid option'
            continuance = 'false'
        number = float(raw_input('What is your number?'))
        if function == 1:
            print guiframework.absolute_value(number)
        if function == 2:
            print guiframework.square_root(number)
    if category == 3:
        print 'You have selected Category 3'
        print 'Please select a function'
        print 'Function 1: Sine'
        print 'Function 2: Cosine'
        print 'Function 3: Tangent'
        print 'Function 4: Cosecant'
        print 'Function 5: Secant'
        print 'Function 6: Cotangent'
        print 'Function 7: Convert Degrees to Radians'
        print 'Function 8: Convert Radians to Degrees'
        function = int(raw_input('What is your function?'))
        if function != 1 and function != 2 and function != 3 and function != 4 and function != 5 and function != 6 \
                and function != 7 and function != 8:
            print 'Please select a valid option'
            continuance = 'false'
        number = float(raw_input('What is your number?'))
        if function == 1:
            print guiframework.sine(number)
        if function == 2:
            print guiframework.cosine(number)
        if function == 3:
            print guiframework.tangent(number)
        if function == 4:
            print guiframework.cosecant(number)
        if function == 5:
            print guiframework.secant(number)
        if function == 6:
            print guiframework.cotangent(number)
        if function == 7:
            print guiframework.degrees_to_radians(number)
        if function == 8:
            print guiframework.radians_to_degrees(number)
    if category == 4:
        print 'You have selected Category 4'
        print 'Please select an equation'
        print 'Equation 1: Quadratic Formula'
        print 'Equation 2: Random Number Generator'
        print 'Equation 3: Pythagorean Theorem'
        equation = int(raw_input('What is your equation?'))
        if equation != 1 and equation != 2 and equation != 3:
            print 'Please make a valid selection'
            continuance = 'false'
        if equation == 1:
            a_value = float(raw_input('What is the a value?'))
            b_value = float(raw_input('What is the b value?'))
            c_value = float(raw_input('What is the c value?'))
            print guiframework.quadratic_formula(a_value, b_value, c_value)
        if equation == 2:
            start = float(raw_input('What is the start of your range?'))
            stop = float(raw_input('What is the end of your range?'))
            print guiframework.rand_number(start, stop)
        if equation == 3:
            missing_value = str(raw_input('What value are you searching for?')).lower()
            if missing_value != 'a' and missing_value != 'b' and missing_value != 'c':
                print 'Please select a valid option'
                continuance = 'false'
            if missing_value == 'a':
                b_value = float(raw_input('What is the b value?'))
                c_value = float(raw_input('What is the c value?'))
                print guiframework.pythagorean_theorem_a(b_value, c_value)
            if missing_value == 'b':
                a_value = float(raw_input('What is the a value?'))
                c_value = float(raw_input('What is the c value?'))
                print guiframework.pythagorean_theorem_b(a_value, c_value)
            if missing_value == 'c':
                a_value = float(raw_input('What is the a value?'))
                b_value = float(raw_input('What is the b value?'))
                print guiframework.pythagorean_theorem_c(a_value, b_value)
    if category == 5:
        print 'You have selected Category 5'
        print 'Please select a shape'
        print 'Shape 1: Rectangle'
        print 'Shape 2: Triangle'
        print 'Shape 3: Circle'
        print 'Shape 4: Sphere'
        print 'Shape 5: Cone'
        print 'Shape 6: Rectangular Prism'
        print 'Shape 7: Cylinder'
        shape = int(raw_input('What is your choice selection?'))
        if shape != 1 and shape != 2 and shape != 3 and shape != 4 and shape != 5 and shape != 6 and shape != 7:
            print 'Please select a valid option'
            continuance = 'false'
        if shape == 1:
            print 'You have selected Shape 1'
            length = float(raw_input('What is the length of the rectangle?'))
            width = float(raw_input('What is the width of the rectangle?'))
            print 'Please select what part of the rectangle do you want to find?'
            print 'Part 1: Perimeter'
            print 'Part 2: Area'
            print 'Part 3: Diagonal'
            part = int(raw_input('What is your selection?'))
            if part != 1 and part != 2 and part != 3:
                print 'Please make a valid selection'
                continuance = 'false'
            if part == 1:
                print guiframework.rectangle_perimeter(length, width)
            if part == 2:
                print guiframework.rectangle_area(length, width)
            if part == 3:
                print guiframework.rectangle_diagonals(length, width)
        if shape == 2:
            print 'You have selected Shape 2'
            print 'Please select which part of the triangle you want to find?'
            print 'Part 1: Area'
            print 'Part 2: Perimeter'
            part = int(raw_input('What is your selection'))
            if part != 1 and part != 2:
                print 'Please select a valid part'
                continuance = 'false'
            if part == 1:
                base = float(raw_input('What is the base of the triangle?'))
                height = float(raw_input('What is the height of the triangle?'))
                print guiframework.triangle_area(base, height)
            if part == 2:
                first_side = float(raw_input('What is the length of the first side?'))
                second_side = float(raw_input('What is the length of the second side?'))
                third_side = float(raw_input('What is the length of the third side?'))
                print guiframework.triangle_perimeter(first_side, second_side, third_side)
        if shape == 3:
            print 'You have selected Shape 3'
            radius = float(raw_input('What is the radius of the circle?'))
            print 'Please select which part of the circle you want to find'
            print 'Part 1: Area'
            print 'Part 2: Circumference'
            part = int(raw_input('What part do you want to find?'))
            if part != 1 and part != 2:
                print 'Please make a valid selection'
                continuance = 'false'
            if part == 1:
                print guiframework.circle_area(radius)
            if part == 2:
                print guiframework.circle_circumference(radius)
        if shape == 4:
            print 'You have selected Shape 4'
            radius = float(raw_input('What is the radius of the circle'))
            print 'Please select which part of the circle you want to find'
            print 'Part 1: Volume'
            print 'Part 2: Surface Area'
            part = int(raw_input('What part do you want to find?'))
            if part != 1 and part != 2:
                print 'Please make a valid selection'
                continuance = 'false'
            if part == 1:
                print guiframework.sphere_volume(radius)
            if part == 2:
                print guiframework.sphere_surface_area(radius)
        if shape == 5:
            print 'You have selected Shape 5'
            radius = float(raw_input('What is the radius of the cone'))
            height = float(raw_input('What is the height of the cone'))
            print 'Please select which part of the cone you want to find'
            print 'Part 1: Volume'
            print 'Part 2: Surface Area'
            part = int(raw_input('What is your selection?'))
            if part != 1 and part != 2:
                print 'Please make a selection'
                continuance = 'false'
            if part == 1:
                print guiframework.cone_volume(radius, height)
            if part == 2:
                print guiframework.cone_surface_area(radius, height)
        if shape == 6:
            print 'You have selected Shape 6'
            width = float(raw_input('What is the width of the rectangular prism?'))
            length = float(raw_input('What is the length of the rectangular prism?'))
            depth = float(raw_input('What is the depth of the rectangular prism?'))
            print 'Please select which part you want to find'
            print 'Part 1: Volume'
            print 'Part 2: Surface Area'
            print 'Part 3: Diagonal'
            part = int(raw_input('What is your selection?'))
            if part != 1 and part != 2 and part != 3:
                print 'Please make a valid selection'
                continuance = 'false'
            if part == 1:
                print guiframework.prism_volume(length, width, depth)
            if part == 2:
                print guiframework.prism_surface_area(length, width, depth)
            if part == 3:
                print guiframework.prism_diagonal(length, width, depth)
        if shape == 7:
            print 'You have selected Shape 7'
            radius = float(raw_input('What is the radius?'))
            height = float(raw_input('What is the height of the cylinder'))
            print 'Please select which part you have to find'
            print 'Part 1: Volume'

            print 'Part 2: Surface Area'
            if part != 1 and part != 2:
                print 'Please make a valid selection'
                continuance = 'false'
            if part == 1:
                print guiframework.cylinder_volume(radius, height)
            if part == 2:
                print guiframework.cylinder_surface_area(radius, height)
    if category == 6:
        print 'You have selected Category 6'
        print 'Please select an equation'
        print 'Equation 1: Simple Interest'
        print 'Equation 2: Compounded Interest'
        equation = float(raw_input('What is your selection?'))
        if equation != 1 and equation != 2:
            print 'Please make a valid selection'
            continuance = 'false'
        if equation == 1:
            print 'You have selected Equation 1'
            principal = float(raw_input('What is your starting amount?'))
            interest_rate = float(raw_input('What is your interest rate?'))
            number_of_years = float(raw_input('How many years is interest gained?'))
            print guiframework.simple_interest(principal, interest_rate, number_of_years)
        if equation == 2:
            print 'You have selected Equation 2'
            principal = float(raw_input('What is your starting amount?'))
            interest_rate = float(raw_input('What is your interest rate?'))
            number_of_years = float(raw_input('How many years is interest compounded?'))
            number_of_times_compounded = float(raw_input('How many times is interest compounded per year?'))
            print guiframework.compounded_interest(principal, interest_rate, number_of_years,
                                                   number_of_times_compounded)
    if category == 7:
        continuance = 'false'
quit()

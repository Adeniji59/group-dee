class Mathematics:
    @staticmethod
    def calculate(operation):
        if operation == "add":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1 + num2
        elif operation == "subtract":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1 - num2
        elif operation == "multiply":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1 * num2
        elif operation == "divide":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1 / num2
        elif operation == "power":
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            return num1 ** num2
        else:
            print("Invalid operation.")
            return None


class Physics:
    @staticmethod
    def calculate(operation):
        if operation == "velocity":
            distance = float(input("Enter the distance in meters: "))
            time = float(input("Enter the time in seconds: "))
            return distance / time
        elif operation == "acceleration":
            velocity_initial = float(input("Enter the initial velocity in meters per second: "))
            velocity_final = float(input("Enter the final velocity in meters per second: "))
            time = float(input("Enter the time in seconds: "))
            return (velocity_final - velocity_initial) / time
        elif operation == "force":
            mass = float(input("Enter the mass in kilograms: "))
            acceleration = float(input("Enter the acceleration in meters per second squared: "))
            return mass * acceleration
        elif operation == "work":
            force = float(input("Enter the force in newtons: "))
            distance = float(input("Enter the distance in meters: "))
            return force * distance
        elif operation == "power":
            work = float(input("Enter the work in joules: "))
            time = float(input("Enter the time in seconds: "))
            return work / time
        else:
            print("Invalid operation.")
            return None


# Main program
choice = input("Enter 'mathematics' or 'physics' to choose the subject: ")

if choice == "mathematics":
    math_operation = input("Enter the math operation you wish to perform (add, subtract, multiply, divide, power): ")
    result = Mathematics.calculate(math_operation)
    print("Result:", result)
elif choice == "physics":
    physics_operation = input("Enter the physics operation you wish to perform (velocity, acceleration, force, work, power): ")
    result = Physics.calculate(physics_operation)
    print("Result:", result)
else:
    print("Invalid choice. Please choose either 'mathematics' or 'physics'.")
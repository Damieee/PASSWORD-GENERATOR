import random

def generate_problems(operation, num_problems):
    """Generates the specified number of random math problems and returns them as a list"""
    problems = []
    for i in range(num_problems):
        if operation == "addition":
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            problem = f"{x} + {y} = "
            answer = x + y
        elif operation == "subtraction":
            x = random.randint(1, 100)
            y = random.randint(1, x)
            problem = f"{x} - {y} = "
            answer = x - y
        elif operation == "multiplication":
            x = random.randint(1, 12)
            y = random.randint(1, 12)
            problem = f"{x} * {y} = "
            answer = x * y
        elif operation == "division":
            y = random.randint(1, 12)
            z = random.randint(1, 12)
            x = y * z
            problem = f"{x} / {y} = "
            answer = z
        problems.append((problem, answer))
    return problems

def main():
    pass
    "WRITE YOUR CODE HERE"

if __name__ == "__main__":
    main()

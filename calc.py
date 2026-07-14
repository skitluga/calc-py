import math


def run_calc():
    while True:
        try:
            expr = input("> ").strip()
            
            if not expr:
                continue
            if expr.lower() in ("exit", "quit"):
                break
            result = eval(expr.replace('^', '**'), {"__builtins__": {}}, math.__dict__)
            print(result)      
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_calc()

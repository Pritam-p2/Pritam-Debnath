
'''
Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
  Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
  Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

'''

class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a,b):
        return a * b

    def division(self,a,b):
        if b != 0:
            return a / b
        else:
            return "Division by zero"

    def calculate(self, a:float, b:float, operation: str, *args, **kwargs):
        if not isinstance(operation,str):
            return 'Third positional argument must be string'
        if args or kwargs:
            return 'No extra agruments allowed'
        operation = operation.lower()
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if hasattr(self, operation):
                return getattr(self, operation)(a,b)
            else:
                return "Invalid Operation"
        else:
            return 'Invalid Inputs'
       

calculator = Calculator()
result = calculator.calculate(c=1,d=1,operation='division')
print(f"Result: {result}")
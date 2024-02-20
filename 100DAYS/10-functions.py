def format_name(f_name, l_name):
    print(f_name.title()) #Con .title podemos convertir un texto en Title case que es primera mayuscula resto no
    print(l_name.title()) #Sirve con Nombres ya que debe ir en mayusculas las iniciales



def format_name2(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    format_Name = f_name.title()
    format_LastName = l_name.title()
    return f'Name: {format_Name} LastName: {format_LastName}'

    
print(format_name2(input("First Name? "), input("Your LastName?")))
#MULTIPLES RETURNS
def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False

      calculator()

calculator()







import re
HISTORY_FILE='history.txt'

def show_history():
  file=open(HISTORY_FILE,'r')
  lines=file.readlines()
  if len(lines)==0:
    print(f"No history found!")
  else:
    for line in lines:
      print(line.strip())

  file.close()

def clear_history():
  file=open(HISTORY_FILE,'w')
  file.close()
  print(f"History Cleared!")

def save_history(equation,result):
  file=open(HISTORY_FILE,'a')
  file.write(f'{equation} = {result} \n')
  file.close()

def calculator(user_input):
  parts = re.split(r'(\+|\-|\*|/)', user_input.replace(" ", ""))
  if len(parts)!=3:
    print(f"Enter the valid Expression to evaluate, By following this Format Operand operator Operand")
    return
  
  num1=float(parts[0])
  op=parts[1]
  num2=float(parts[2])

  if op=='+':
    result = num1 + num2
  elif op=='-':
    result= num1-num2
  elif op=='*':
    result= num1*num2
  elif op=="/":
    if num2==0:
      print(f'Cannot be divided!')
      return
    else:
      result= num1/num2
  else:
    print(f"Choose the valid operator from Available (+,-,*,/)")
    return
  
  if int(result)==result:
    result=int(result)
  
  print(f'Result = {result}')
  save_history(user_input,result)

if __name__=='__main__':

  print(f'----SIMPLE CALCULATOR (type history, clear or exit)')
  while True:
    user_input=input('Enter Calculation (+,-,*,/) or command (history, clear, exit): ')
    if user_input.strip().lower()=='history':
      show_history()
    elif user_input.strip().lower()=='clear':
      clear_history()
    elif user_input.strip().lower()=='exit':
      print(f'GoodBye!')
      break
    else:
      calculator(user_input)
  
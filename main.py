HELP="""
help - печать справки по программе.
add - добавить задачу в список (название задачи 
запрашиваем у пользователя).
show - напечатать все добавленные задачи
"""

tasks=[]
today=[]
tomorrow=[]
other=[]


run= True

while run:
  command =input("Введите команду: ")
  if command =="help":
    print(HELP)
  elif command=="show":
    print(tasks)
  elif command=="add":
    data=input('Введите дату задачи: ')
    task=input('Введите название задачи: ')
    if data=='Сегодня' or data=='сегодня':
      tasks.append(task)
      today.append(task)
      print("Задача добавлена")
    elif data=='Завтра' or data=='завтра':
      tasks.append(task)
      tomorrow.append(task)
      print("Задача добавлена")
    else :
      tasks.append(task)
      other.append(task)
      print("Задача добавлена")
  elif command=="exit":
    print("До свидания!")
    break
  else:
    print("Неизвестная команда")
    #run=False
    break

print('Сегодня',today)
print('Завтра',tomorrow)
print('Другие дни',other)
print('End')

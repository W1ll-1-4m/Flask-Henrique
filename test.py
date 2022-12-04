import csv

def take_tasks():
    
    with open('tasks.csv', 'rt') as file_in:
        leitor = csv.reader(file_in)
        print(leitor)
        for linha in leitor:
            print(linha)

    return leitor

a = take_tasks()
for b in a:
    print(b)
with open('salaary.txt', 'r') as rf:
    with open('output.txt', 'a') as wf:
        for line in rf.readline():
            name,salary = line.split(',')
            wf.write(f'{name}\'s salary is {salary} ')
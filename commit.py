import os
from random import randint
from datetime import date, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2021, 7, 20)
end_date = date(2022, 7, 19)
for single_date in daterange(start_date, end_date):
    d = str(single_date) + ' 12:00:00'
    for j in range(0,randint(1, 10)):
        with open('commit.txt', 'w') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit -m "commit"')
        os.system('GIT_COMMITTER_DATE="' + d + '" git commit --amend --no-edit --date="' + d + '"')
        print('commit ' + d)
    print(d)






import sys
import os

project_dir = os.environ.get('PD')
github_token = os.environ.get('GH')

folder = sys.argv[1]
_dir = project_dir + '/' + folder
os.chdir(project_dir)
check = not os.path.exists(folder)

if check:
    try:
        os.mkdir(_dir)
        os.chdir(_dir)
    except FileExistsError as error:
        print(error)
else:
    print("A folder with that name already exists!")

commands = [
    f'echo #{folder} > README.md'
]

for c in commands:
    os.system(c)



#print(github_token)


#print(sys.argv[1])

#print(os.environ)


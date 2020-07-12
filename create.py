import sys
import os
from github import Github

# Gets variables from the env
project_dir = os.environ.get('PD')
github_token = os.environ.get('GH')

# Creates the dir for the new project
folder = str(sys.argv[1])
_dir = project_dir + '/' + folder
os.chdir(project_dir)

# Login to GitHub and creates a new repo
g = Github(github_token)
user = g.get_user()
username = user.login
check_repo = []
for r in user.get_repos():
    check_repo.append(str(r.name))
if folder not in check_repo:
    repo = user.create_repo(folder)
else:
    print("Repo already exists. Try again!")
    sys.exit()

# Creates the new project folder in the project dir
check = not os.path.exists(folder)
if check:
    try:
        os.mkdir(_dir)
        os.chdir(_dir)
    except FileExistsError as error:
        print(error)
else:
    print("A folder with that name already exists!")
    sys.exit()

# List of commands to be executed
commands = [
    f'echo # {folder} > README.md',
    'git init',
    'git add README.md',
    'git commit -m "first commit"',
    f'git remote add origin https://github.com/{username}/{folder}.git',
    'git push -u origin master'
]

for c in commands:
    os.system(c)

print(f'Folder {folder} was created in {project_dir}.')


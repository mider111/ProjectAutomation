import sys
import os

project_dir = os.environ.get('PD')
github_token = os.environ.get('GH')

folder = sys.argv[1]
dir = project_dir + '/' + folder

os.mkdir(dir)
os.chdir(dir)

commands = [
   # f'echo #{}'
]



#print(github_token)


#print(sys.argv[1])

#print(os.environ)


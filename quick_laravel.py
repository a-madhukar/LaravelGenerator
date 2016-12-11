import sys
import os 

def execute_commands(): 
	commands = [
		"sublime .", 
		"npm install", 
		"git init",
		"git add .",	
		"git commit -m 'Initial commit' "
	]
	for command in commands: 
		os.system(command)


def make_laravel_project(): 
	current_path = os.getcwd() 
	os.chdir(current_path)
	project_name = sys.argv[1]
	try: 
		os.system("laravel new " + project_name)
		os.chdir(current_path + '/' + project_name)
		execute_commands()
	except: 
		print "Unexpected error: ", sys.exc_info()[0]


if(len(sys.argv[1:]) == 1): 
	make_laravel_project()
elif len(sys.argv[1:]) > 1: 
	print "You provided way too many arguments. Please provide a name for your project."
else: 
	print "You haven't provided a project name."



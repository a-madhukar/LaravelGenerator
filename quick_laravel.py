import os 
import sys
import argparse
import webbrowser

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


def make_laravel_project(args): 
	current_path = os.getcwd() 
	os.chdir(current_path)
	project_name = args.name
	try: 
		os.system("laravel new " + project_name)
		if args.valet: 
			webbrowser.open("http://" + project_name + ".dev")
		os.chdir(current_path + '/' + project_name)
		execute_commands()
	except: 
		print "Unexpected error: ", sys.exc_info()[0]


parser = argparse.ArgumentParser() 
parser.add_argument("name",help="The name of the project")
parser.add_argument("-v", "--valet", help="open project in the browser with valet", action="store_true"	) 
make_laravel_project(parser.parse_args())






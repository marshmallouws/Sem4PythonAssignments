#Create a module called utils.py and put the following functions inside:
# Make sure your module can be called both from cli and imported to 
# another module Create a new module that imports utils.py and test each function.


import os, sys

# 1) Write file names in a specific folder and 
#    write file names to a new file
def write_filenames(path):
    # Checks to make module used in cli
    if type(path) is list:
        path = path[0]

    files = os.listdir(path)
    file_list = []

    with open(os.path.join(path, 'files.csv'), 'w') as output:
        for f in files:
            if os.path.isfile(os.path.join(path, f)):
                output.write(f + '\n')

# 2) Write all filenames recursivly in a specific folder
def write_filenames_recursive(path):
    # Checks to make module used in cli
    if type(path) is list:
        path = path[0]

    lst = []
    with open('recursive.csv', 'w') as output: 
        for root, dirs, files in os.walk(path):
            for name in files:
                output.write(name + '\n')


# 3) Take a list of filenames and print first line of each file
def print_first_line(filenames):
    for f in filenames:
        with open(f, 'r') as curr_file:
            print(curr_file.readline())

# 4) Take a list of filenames and print each line that contains
#    an email (@)
def print_emails(filenames):
    for f in filenames:
        with open(f, 'r') as curr_file:
            for line in curr_file.readlines():
                if '@' in line:
                    print(line)

# 5) Take a list of md files and write all headlines to a file
def print_md_files(filenames):
    headlines = []

    for f in filenames:
        with open(f, 'r') as curr_file:
            for line in curr_file.readlines():
                if line.startswith('#'):
                    headlines.append(line)
    
    with open('headlines.md', 'w') as output_file:
        for line in headlines:
            output_file.write(line + '\n')

if __name__ == "__main__":
    func = sys.argv[1]
    param = sys.argv[2:]

    # Getting the name of the called function
    getattr(sys.modules[__name__], func)(param)

#Exercise 1
#Create a python file with 3 functions:
#def print_file_content(file) that can print content of a csv file to the console
#def write_list_to_file(output_file, lst) that can take a list of tuple and write 
# each element to a new line in file
#rewrite the function so that it gets an arbitrary number of strings instead of a list

#def read_csv(input_file) that take a csv file and read each row into a list
#Add a functionality so that the file can be called from cli with 2 arguments
#path to csv file
#an argument --file file_name that if given will write the content to file_name or 
# otherwise will print it to the console.
#Add a --help cli argument to describe how the module is used
import csv
import sys
import getopt

# 1a)
def print_file_content(file):
    with open(file, 'r') as csvfile:
        print(csvfile.read())

# 1b) 
def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as randomfile:
        for l in lst:
            randomfile.writelines([str(i) for i in l])
            randomfile.write('\n')

# 1b) Rewrite to take abitrary number of strings
def write_strings_to_file(output_file, *strings):
    with open(output_file, 'w') as randomfile:
        for s in strings:
            randomfile.write(s)
            randomfile.write('\n')

# 1c)
def read_csv(input_file):
    with open(input_file, 'r') as csv:
        content = []
        for c in csv:
            content.append(c.strip())
    return content

# 2) + 3)
def usage():
    return f'Usage : {sys.argv[0]} <csvfile> [--file=<output_file>]'

def run(arguments):
    try:
        arg = arguments[0]
        opts, args = getopt.getopt(arguments[1:], '', ['file=', 'help'])
    except getopt.GetoptError as err:
        print(err)
        print(usage())
        exit(2)
    
    lst = read_csv(arg)

    if len(opts) == 0:
        print(lst)

    for option, argument in opts:
        if option in ('--file'):
            write_list_to_file(argument, lst)
        elif option in ('--help'):
            print(usage())

if __name__ == "__main__":
    run(sys.argv[1:])





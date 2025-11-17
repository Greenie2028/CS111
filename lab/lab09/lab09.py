import sys
def print_args(arg=0):
    for i in range(arg, len(sys.argv)):
        print(sys.argv[i])

def flag_check(argument_list):
    flag = argument_list[1]
    if flag in ['-p', '-h', '-i','-w','-r']:
        return True
    return False

def flags():
    if flag_check(sys.argv):
        flag = sys.argv[1]
        if flag == '-p':
            for arg in sys.argv[2:]:
                print(arg)
        elif flag == '-i':
            print("Hello World")
        elif flag == '-h':
            print('Valid flags:\n-p : prints out all the command line arguments after the -p\n-i : prints "Hello World"\n-h : prints out a help command')
        elif flag == '-r':
            with open(sys.argv[2]) as read_file:
                for line in read_file:
                    print(line.strip())
        elif flag == '-w':
            if len(sys.argv) < 4:
                print("No Content Provided")
            else:
                with open(sys.argv[2], 'w') as output_file:
                    for line in range(3, len(sys.argv)):
                        output_file.write(f"{sys.argv[line]}\n")
    else:
        print_args()

if __name__ == "__main__":
    flags()
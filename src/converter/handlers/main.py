from . import io_handler

def readLine(ip_file,op_file):
    Lines = ip_file.readlines()
    line_no = 0
    for line in Lines:
        line_to_write = to_handler(line)
        if(not line_to_write):
            print("Error in Line No",line_no+1)
            return None
        else:
            writeLine(op_file,line_to_write)

def writeLine(op_file,line):
    try:
        op_file.write(line)
        op_file.write('\n')
    except:
        print("[INTERNAL ERROR] Write to Temp file failed")

def handle(ip_file,op_file):
    readLine(ip_file,op_file)


def to_handler(line):
    if(line[:5] == "show("):
        return io_handler.cvt(line)
    else:
        return None
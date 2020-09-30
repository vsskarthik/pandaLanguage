import os
from handlers import main as main_handler
import sys



ip_path = sys.argv[1]
op_path = 'temp.py'
os.chdir('../../src/converter')

ip_file = open(ip_path,'r')
op_file = open(op_path,'w+')

main_handler.handle(ip_file,op_file)
ip_file.close()
op_file.close()
if os.name == "nt":
    os.system('') # For Windows
else:
    os.system("python3 temp.py")

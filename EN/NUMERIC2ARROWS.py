from multiprocessing.connection import wait
import os
username = os.getlogin()
print('NUMERIC2ARROWS: By Robichani6-1 (Transportes Chancleta)')
yes = ["sí", "si", "s", "y", "yes"]
no = ["no", "n"]
response = input("Do you want to move camera 0 with the arrow keys and not with the numeric keypad? (Y/N)")

def change_values(file):

    values = {
        ' config_lines[180]: "mix dbgfwd `keyboard.num8?0`"': ' config_lines[180]: "mix dbgfwd `keyboard.uarrow?0`"\n',
        ' config_lines[181]: "mix dbgback `keyboard.num5?0`"': ' config_lines[181]: "mix dbgback `keyboard.darrow?0`"\n',
        ' config_lines[182]: "mix dbgleft `keyboard.num4?0`"': ' config_lines[182]: "mix dbgleft `keyboard.larrow?0`"\n',
        ' config_lines[183]: "mix dbgright `keyboard.num6?0`"': ' config_lines[183]: "mix dbgright `keyboard.rarrow?0`"\n',
    }
    with open(file, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for key in values:
                if key in line:
                    lines[i] = values[key]
                    break
    with open(file, 'w') as f:
        f.writelines(lines)
        print('[+] You can now move camera 0 with the arrows.')
         
while True:
  if response.lower() in yes:
    change_values(os.path.join(r"C:\Users\\"+str(username)+"\Documents\Euro Truck Simulator 2\profiles\controls.sii"))
    break
    quit()
  elif response.lower() in no:
    print("[+] The program is closing...")
    break
    quit()
  else:
   print("Invalid answer, please try again.")
   response = input("Do you want to move camera 0 with the arrow keys and not with the numeric keypad? (Y/N)")


    

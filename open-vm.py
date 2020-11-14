import os
print("Starting script...")
os.chdir("path/to/VMware/folder (probably in C:\Program Files (x86)\VMware\VMware Player)")
print("running vmrun start")
os.system('vmrun -T player start "path/to/your/vm/file.vmx"')
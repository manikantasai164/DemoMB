import os

# Include folder not required
Exclude_list = [ 'Program Files','Program Files (x86)','AWS', 'Python', 'Python_Env', 'file_monitoring', 'done']

for root, dirs, files in os.walk(r"C:\\Scripts\\"):
    dirs[:] = [d for d in dirs if d not in Exclude_list]
    for d in dirs:
        print(os.path.join(root,d))  # full path of the directory by excluding the Exclude_list

import sys
sys.path.append(r'D:\GitHub\Python')

from EricCorePy.Utility.EricUtility import EricUtility

filepath = sys.argv[1]
oldName = sys.argv[2]
newName = sys.argv[3]

print(filepath)
print(newName)

filepath += "launcher_profiles.json"

u = EricUtility()
if u.is_file_exist(filepath) == False:
    print("file is not exist")
    exit
if len(newName) == 0:
    print("error name")
    exit 

data = u.get_file_data(filepath)
data = data.replace(oldName, newName)
u.to_file(filepath, data)
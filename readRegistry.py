'''
Giveb a registry hive in Win 11, this will print subkeys and values. This code can be made a little more better
'''
from Registry.Registry import Registry
 
reg_hive = Registry(r'C:/Users/Admin/Desktop/NEWSoftwareHiveRegistrySekhar.dat')
#reg_hive = Registry("SOFTWARE")
root_key = reg_hive.open(r'Microsoft\Windows NT\CurrentVersion')

#print(root_key.subkeys())
#print(root_key.values())

print("Subkeys:")
for subkey in root_key.subkeys():
    print(subkey.name())

# Print value names and their data
print("\nValues:")
for value in root_key.values():
    print(f"{value.name()}: {value.value()}")
    
'''
If your file is a .reg file (text format), you need to convert it to a binary hive file. 
You can use the reg save command in Command Prompt to save a registry key to a hive file. For example:
reg save HKCU\Software C:\Users\Admin\Desktop\SoftwareHiveRegistrySekhar.dat
'''

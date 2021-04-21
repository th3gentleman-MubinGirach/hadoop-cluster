import os 

print("Providing chmod +x permissions to dynamic inventory")
os.system("chmod +x /root/hadoop-cluster/dynamic_inventory/*")
keypairname=input("Enter the name of the keypair file:  ")
print("Hope your file is in /root/hadoop-cluster/ path ")
chmod="chmod 400"+" "+keypairname
os.system(chmod)
print("installing boto")
os.system("pip3 install boto")
print("You know doing things mannually gives utmost satisfaction")
print("So configure the rest of things manually")
print(""Things left to be configured 
       - Credentials in ~/.boto
       - Path in ansible config file
        -Copy ansible config file in /etc/ansible/
        "")
os.system("exit()")

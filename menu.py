import os
import subprocess
def phonebook():
	print("phonebook.......")
	namenode_ip=input("enter name node ip\t")
	namanode_name='nn'
	
	choice=int(input("how many data node??\t\t"))
	l = []
	for i in range(1,choice+1):
		print(f"enter ip of {i} datanode:\t")
		l.append(input())
	s=''	
	for i in l:
		print(i)
	f=open("zzzz.txt",'w')
	f.write(l)
	f.close()
def install_java_hadoop():
	print("xxxxxxxxx     Installation of java and hadoop now begin     xxxxxxxxxxxxxx\n\n")
	subprocess.getstatusoutput("ansible-playbook transfer_java.yml")
	subprocess.getstatusoutput("ansible-playbook transfer_hadoop.yml")
	subprocess.getstatusoutput("ansible-playbook setup_rc.yml")

def setup_master():
	print("welcome master setup\n\n")
	pass
def setup_slave():
	print("welcome to slave setup")
	pass
	
def setup_jobtracker():
	print("welcome to job tracker setup")
	pass
	
print("\t\t\t......welcome......")
print("\t\t\t................................")

print("\t\t\t..........welcome in remote installation..........\n\n")
print('''\n\n		
			Press 0: To generate phone book
                        Press 1: To install Java and hadoop
			Press 2: To setup master
                        Press 3: To setup slave
			Press 4: To set job tracker
			

                       ''')
choice=int(input("enter you choice  :\t")) 
if choice == 0:
	phonebook()
elif choice ==1:
	install_java_hadoop()
elif choice == 2:
	setup_master() 
elif choice == 3:
	setup_slave()
elif choice == 4:
	setup_jobtracker()

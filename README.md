# hadoop-cluster
# Automate the Hadoop cluster on AWS cloud using Ansible 
The repository contains two main playbooks <i>provision.yaml</i> & <i>configuration.yaml.</i>
The playbook provision.yaml contains the role 
<b>"provision" role would provision the master and the slave instances on AWS & also copy the configuration files for master and the slave node into their respective roles<b>

The play configuration.yaml contains four roles <i>copy, install, masterconfig, slaveconfig,</i> </br>
<b>"copy" role would copy the installation packages for hadoop and jdk , </br>
"install" role would install those rpm packages on the instances ,</br>
"masterconfig" would create a directory format it and start the namenode services on master instance , </br>
"slaveconfig" woud create a directoty and start the datanode services on slave instance.<b> </br>

Note:
<ul>
<li>Clone the repository in the /root/ directory</li>
<li>Copy the ansible.cfg file into your /etc/ansible/ directory</li>
<li> Give chmod +x permissions to ec2.ini and ec2.py files in dynamic_inventory and chmod 400 to the keypair file </li>
<li>Also install & configure boto using the below commands</li>
<li> Add your keypair name in the /roles/provision/vars/main.yaml file and also give the path of it in the ansible.cfg file </li>
<li>Copy ansible.cfg file into /etc/ansible/ </li>
</ul> 

~ pip3 install boto </br>
~vim .boto </br>

[Credentials] </br>
aws_access_key_id = xxxxxxxxxxxxxx </br>
aws_secret_access_key =  xxxxxxxxxxxxxxxxxxxxx </br>

~ chmod 400 .boto

import subprocess
print("Please make sure you have ansible installed")
Running = True
def server_list():
    global server_ip_list
    server_ip_list = dict()
    print("Type done, when you dont need to add more")
    while True:
        server = input(str("Server ip :"))
        if server == "done":
            return server_ip_list
        password = input(str("Server password : (leave empty if no needed password)"))
        if password == "done":
            return server_ip_list
        elif password == "":
            server_ip_list[server] = "None"
            continue
        server_ip_list[server] = password


def server_list_2():
    global server_ip_list_2
    server_ip_list_2 = dict()
    print("Type done, when you dont need to add more")
    while True:
        server = input(str("Server ip :"))
        if server == "done":
            return server_ip_list_2
        password = input(str("Server password : (leave empty if no needed password)"))
        if password == "done":
            return server_ip_list_2
        elif password == "":
            server_ip_list_2[server] = "None"
            continue
        server_ip_list_2[server] = password

def ansible_pass_2():
    global count
    global key
    global value
    count = 0
    for key, value in server_ip_list_2.items():
        print("those are your ip and password")
        print(key, value)
        if value != "None":
            bashcommand = "exp " + value + " ssh-copy-id " + key
            print(bashcommand)
            subprocess.Popen(bashcommand.split(), stdout=subprocess.PIPE)


def ansible_pass():
    global count
    global key
    global value
    count = 0
    for key, value in server_ip_list.items():
        print("those are your ip and password")
        print(key, value)
        if value != "None":
            bashcommand = "exp " + value + " ssh-copy-id " + key
            print(bashcommand)
            subprocess.Popen(bashcommand.split(), stdout=subprocess.PIPE)

def ansible_execute():
    global key
    server_ip = list()
    for key, value in server_ip_list.items():
            server_ip.append(key)
            f=open('hosts', 'w+')
            f.writelines("[webserver] \n")
            f.writelines("%s\n" % i for i in server_ip)
            f.close()
    ansible = "ansible-playbook -i hosts csf-playbook.yml"
    subprocess.Popen(ansible.split(), stdout=subprocess.PIPE)
    print("done csf installed")



def ansible_execute_2():
    global key
    server_ip = list()
    for key, value in server_ip_list.items_2():
            server_ip.append(key)
            f=open('hosts2', 'w+')
            f.writelines("[webserver] \n")
            f.writelines("%s\n" % i for i in server_ip)
            f.close()
    ansible = "ansible-playbook -i hosts2 nagios-playbook.yml"
    subprocess.Popen(ansible.split(), stdout=subprocess.PIPE)
    print("done nagios-healthcheck installed")



while Running:

    readme = input(str("Menu \n 1. install csf on your remote servers \n 2. install nagios healthcheck on your remote servers :"))
    if readme == "1":
        server_list()
        ansible_pass()
        ansible_execute()
    elif readme == "2":
        server_list_2()
    elif readme == "exit":
        break










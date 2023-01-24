import paramiko

# Switch'lerin IP adreslerini ve SSH kullanıcı adı ve şifrelerini bir dizi içinde tutun
switches = [    {'ip': '192.168.1.10', 'username': 'admin', 'password': 'password1'},    
                {'ip': '192.168.1.11', 'username': 'admin', 'password': 'password2'},    
                {'ip': '192.168.1.12', 'username': 'admin', 'password': 'password3'},]

# Switch'leri dolaşarak SSH bağlantısı kurun ve komut gönderin
for switch in switches:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(switch['ip'], username=switch['username'], password=switch['password'])
    stdin, stdout, stderr = ssh.exec_command('show running-config')
    print(f"Switch {switch['ip']}:")
    print(stdout.read())
    ssh.close()
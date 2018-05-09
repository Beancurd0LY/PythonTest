# /usr/bin/python
# encoding:utf-8
import paramiko


def create_MATRIX_ENV_CONF(port, JMXPORT, IPADDR, HOSTNAME):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="10.8.1.213", username="root", password="dooioo")
    stdin, stdout, stderr = ssh.exec_command("cd /data0/www/htdocs/i.stanfordbiz.off.zhidaovip.com/system/")
    stdin, stdout, stderr = ssh.exec_command("ls")
    result = stdout.read()
    print(result.decode())   

 
def a (func, port, JMXPORT, IPADDR, HOSTNAME):
    return func(port, JMXPORT, IPADDR, HOSTNAME)

        
if __name__ == '__main__':
    # a = create_MATRIX_ENV_CONF(1, 1, 1, 1)
    a(create_MATRIX_ENV_CONF, 1, 1, 1, 1)
    l = "abcde"[:3]
    print l
    L1 = ['Hello', 'World', 18, 'Apple']
    L2 = [s.lower() for s in L1 if isinstance(s, str)]
    print(L2)   

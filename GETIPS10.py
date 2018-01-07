import netmiko
import time


def ssh_open_connect(ip, unit_ip):
    try:
        user_name = "your_device_username"
        pass_word = "your_device_password"
        from netmiko import ConnectHandler
        session = ConnectHandler( device_type='cisco_ios', ip=ip , username=user_name , password=pass_word)
        command_make = "sh run | inc ip address 10." #Creating Output using show command and pipe
        output = session.send_command(command_make)
        print output
        with open("IP.txt", "a") as backups_file:
             backups_file.write(output + "\n")



        backups_file.close()

    except netmiko.NetMikoAuthenticationException:
        print "%s Not connected" % ip

    except netmiko.NetMikoTimeoutException:
        print "%s Time out" % ip

start_ip = input("PLEASE WRITE START IP: ")
end_ip = input("PLEASE WRITE END IP: ")
for i in xrange(start_ip, end_ip+1): #Loop For your ip range, replace it with 182.24
    ssh_open_connect("182.24."+str(i)+".1",i)
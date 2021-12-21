'''Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только
последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.'''
import platform
import subprocess
from ipaddress import ip_address
from tabulate import tabulate


def host_range_ping():
    start_ip = input('Enter start ip-address: ')
    count = int(input('How many addresses to check: '))
    MAX_SIZE = 255
    res_list = []
    try:
        IPv4 = ip_address(start_ip)
        oktet = str(IPv4).split('.')[3]
        while count > 0:
            if int(oktet) < MAX_SIZE:
                IPv4 += 1
                count -= 1
                res_list.append(str(IPv4))
    except Exception as e:
        return 'Invalid data entry'
    return res_list


ip_list = host_range_ping()

# --------------------------------------------  task_3  -----------------------------------------------------
'''Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).
Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable
10.0.0.1
10.0.0.2
Unreachable
10.0.0.3
10.0.0.4'''

def host_range_ping_tab(lst):
    reachable = []
    unreachable = []
    for host in lst:
        command = ['ping', param, '1', str(host)]
        reply = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        code = reply.wait()
        if code == 0:
            reachable.append(host)
        else:
            unreachable.append(host)
    return reachable, unreachable


param = '-n' if platform.system().lower() == 'windows' else '-c'
addresses_list = host_range_ping_tab(ip_list)
COLUMNS = ['Reachable', 'Unreachable']
print(tabulate([addresses_list], headers=COLUMNS, stralign="center"))



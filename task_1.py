''' 1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().'''

from ipaddress import ip_address
from tabulate import tabulate


def get_ip_address(addresses):
    addresses_list = []
    for i in addresses:
        try:
            if type(i) in (str, int):
                addresses_list.append(i)
        except TypeError:
            print('Данный формат недопустим')
    return addresses_list


def host_ping(addresses_list):
    import platform
    import subprocess
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    res = []
    for host in addresses_list:
        command = ['ping', param, '1', str(host)]
        reply = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        code = reply.wait()
        if code == 0:
            res.append((host, 'Узел доступен'))
        else:
            res.append((host, 'Узел недоступен'))
    return res


addresses = ['172.217.166.110', 'google.crom', ' ', 'qwerty.com', 'qweyandex.ru', 'we1234hg',
             '127.0.0.1', '198.186.1.0', 3232235776, {'one': 1}, {1, 2}]


addresses_list = get_ip_address(addresses)
print(tabulate(host_ping(addresses_list), tablefmt='fancy_grid', stralign='center'))




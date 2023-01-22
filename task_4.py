ip_addresses = ("192.12.14.5", "192.12.14.6", "192.12.14.8", "192.12.14.9", "192.12.14.10", "192.12.14.11", "192.12.14.13", "192.12.14.14")

remove_ip = input('Введите последние цифры IP-адреса, который необходимо удалить: ')

print(f'Исходный кортеж: {ip_addresses}')

for element in ip_addresses:
    if element[-2:].strip('.') == remove_ip:
        ip_addresses = list(ip_addresses)
        ip_addresses.remove(element)
    ip_addresses = tuple(ip_addresses)

print(f'Кортеж после удаления IP-адреса: {ip_addresses}')
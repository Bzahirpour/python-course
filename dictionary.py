device_info = {
    'hostname': 'USVA3_VA3_301_312_U35_1-3-2',
    'model': 'NTK665AA',
    'sn': 'Ciena-OTN-1234-ABCD-5678-XYZ9',
    'location': 'US East, Coresite VA3, Room 301'
}
device_info_request = ''
while True:
    device_info_request = input('device info: ').lower()
    if device_info_request == 'help':
        print('''
OPTIONS:
hostname
model
sn
location
quit
''')
    elif device_info_request == 'quit': 
        exit()
    else:
        print(device_info.get(device_info_request, 'does not exist in device info, type help for options'))

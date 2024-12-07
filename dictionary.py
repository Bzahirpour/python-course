device_info = {
    'hostname': 'USVA3_VA3_301_312_U35_1-3-2',
    'model': 'NTK665AA',
    'sn': 'Ciena-OTN-1234-ABCD-5678-XYZ9',
    'location': 'US East, Coresite VA3, Room 301'
}
device_info_request = ''
while device_info_request != 'quit':
    device_info_request = input('device info: ')
    if device_info_request.lower() == 'help':
        print(
'''
hostname
model
sn
location
quit
'''
        )
    elif device_info_request.lower() == 'quit':
        exit()
    else:
        print(device_info.get(device_info_request.lower(), 'does not exist in device info, type help for options'))









device_info = {
    'hostname': 'USVA3_VA3_301_312_U35_1-3-2',
    'model': 'NTK665AA',
    'sn': 'Ciena-OTN-1234-ABCD-5678-XYZ9',
    'location': 'US East, Coresite VA3, Room 301'
}
device_info_request = input('device info: ')
print(device_info.get(device_info_request))
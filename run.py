from subprocess import check_output, Popen, call
import os
import re


values = {}
def return_values(string):
    mini = string.index("min") + 1
    maxi = string.index("max") + 1
    default = string.index("default") + 1
    return mini, maxi, default

def parse_string(string):
    lst = string.replace('=', ' ')
    lst = lst.split()
    if lst[0] == 'brightness':
        mi, ma, default = return_values(lst)
        values[lst[0]] = {'min': lst[mi], 'max': lst[ma], 'default': lst[default]}
        
    if lst[0] == 'contrast':
        mi, ma, default = return_values(lst)
        values[lst[0]] = {'min': lst[mi], 'max': lst[ma], 'default': lst[default]}
        
    if lst[0] == 'saturation':
        mi, ma, default = return_values(lst)
        values[lst[0]] = {'min': lst[mi], 'max': lst[ma], 'default': lst[default]}
        
    if lst[0] == 'white_balance_temperature':
        mi, ma, default = return_values(lst)
        values[lst[0]] = {'min': lst[mi], 'max': lst[ma], 'default': lst[default]}

    if lst[0] == 'exposure_absolute':
        mi, ma, default = return_values(lst)
        values[lst[0]] = {'min': lst[mi], 'max': lst[ma], 'default': lst[default]}

    if lst[0] == 'exposure_auto':
        pass
    if lst[0] == 'white_balance_temperature_auto':
        pass
        
#v4l2-ctl -d /dev/video0 -l                                                                 
t = check_output(['v4l2-ctl', '-l']).decode('utf-8')

for lines in t.splitlines():
    parse_string(lines) 


print(values)

def set_values(key, value):
      os.system(f'v4l2-ctl -d /dev/video0 --set-ctrl {key}={value}')
#     #call(['v4l2-ctl', '-d', 'v4l2-ctl', '--set-ctrl', f'{key}={value}' ])

set_values("saturation", 0)

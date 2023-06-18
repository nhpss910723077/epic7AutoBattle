import keyboard
import time
import uiautomator2 as u2

import imageControl as ic
import simulatorControl as sc

# 連接夜神模擬器
# simulator = u2.connect('127.0.0.1:5201')
simulator = u2.connect()

select_language = input('select en ch:')

imageControl = ic.ImageControl(simulator)
simulatorControl = sc.SimulatorControl(imageControl, simulator, select_language)

while True:
    while not simulatorControl.matchEnd():
        time.sleep(5)
        
    while not simulatorControl.clickConfirm():
        time.sleep(5)
    
    while not simulatorControl.clickRestart():
        time.sleep(5)
    
    time.sleep(5)
    
    simulatorControl.clickStart()
    
    time.sleep(5)
    
    if simulatorControl.checkLeft():
        time.sleep(5)
        simulatorControl.clickStart()
    
    time.sleep(5)



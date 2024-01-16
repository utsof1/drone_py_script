import afc_drone_kit
from pynput import keyboard
afc_drone_kit.arm_and_takeoff(2)

def on_press(key):
    try:
        if key.char == 'w' or key.char == 'a' or key.char == 's' or key.char == 'd':
            afc_drone_kit.move(key.char)

        if key.char == 'q':
            print()
            afc_drone_kit.land_and_disarm()
            afc_drone_kit.close_vehicle()
    
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as Listener:
    Listener.join()
import os
import can
import time
import sys
import select
import tty
import termios
import threading

target_current = 0
def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

def can_loop():
    os.system('sudo ifconfig can0 down')
    os.system('sudo ip link set can0 type can bitrate 1000000')
    os.system('sudo ifconfig can0 up')
    global target_current
    SUPER_CURRENT_LIMIT = 10.0; 
    CONV_CURRENT_REF_RATIO  = 10000.0 / SUPER_CURRENT_LIMIT
    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    while True:
        recv_msg = can0.recv(10.0)
        target_bit =  int(target_current*CONV_CURRENT_REF_RATIO)
        print(target_bit)
        upper = target_bit>>8&0xff
        lowwer = target_bit&0xff
        send_msg = can.Message(arbitration_id=0x200, data=[upper,lowwer,upper,lowwer,upper,lowwer,upper,lowwer],is_extended_id=False)
        can0.send(send_msg)
        print(f'Send frame: \n{send_msg}\n')
        if recv_msg is None:
            print('No message was received')
        else:
            print(f'Received frame: \n{recv_msg}\n')
        time.sleep(1)

def input_loop():
    global target_current
    while True:
        s =input("target_current:")
        if is_num(s):
            current = float(s)
            if current > 10 :
                target_current = 10
            elif current < -10:
                target_current = -10
            else:
                target_current=current
            print(current)
        else:
            print("invalid input")


if __name__ == "__main__":
    thread0 = threading.Thread(target=input_loop,name="input",args=())
    thread1 = threading.Thread(target=can_loop,name="input",args=())
    thread0.start()
    thread1.start()
    send_msg = can.Message(arbitration_id=0x200, data=[0,0,0,0,0,0,0,0],is_extended_id=False)
    os.system('sudo ifconfig can0 down')
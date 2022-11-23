# USB_CAN_DJI
## Supported environment
 - Ubuntu(20.04 LTS tested)

## Check the device
Type command below to check 'can0' device is available in system after connected device to the pc.

```bash
ifconfig -a
```

## Install tools
```bash 
sudo apt install can-utils
```
## How to
```bash
cd usb_can_dji
source usb_can/bin/activate
python3 usb_can.py
```
User can enter a number from -10 to 10.  
The number corresponds to the current value.  
To stop, use ctrl-c to terminate the process.  


## References
- [Ofiicial HP](http://wiki.inno-maker.com/display/HOMEPAGE/usb2can)
- [Official sample codes](https://github.com/INNO-MAKER/usb2can)


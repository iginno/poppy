#This repository is a modified version of the original poppy-humanoid raspoppy repository.  

#This repository aims to remove the hotspot function and accelerate the script install time by installing correct version of related package.  

1. Install rpi image using the latest one from website
1.1 You may use filezilla or winssp to copy file to pi
1.2 place the folder in home directory 
1.3 zip the hampy folder and pypot folder into hampy.zip and pypot.zip
2. run raspoppyfication.sh script  e.g. ./raspoppyfication.sh
3. Wait for install to finish
4. After finished, run this two command   
sudo apt-get install libatlas-base-dev  

sudo apt-get install libhdf5-serial-dev  

5. Then install virtual keyborad for user.

sudo apt-get install matchbox-keyboard

5.1 run commond sudo reboot

6. run poppy-services poppy-humanoid --snap 
check if there is any error occur

7. To run python script in poppy_python folder, user have to manually setup the usb latency. Run the command below:  

sudo nano /sys/bus/usb-serial/devices/ttyUSB0/latency_timer

Then change the value from 16 -> 1

8. run python poppy_python/test.py

You should see terminal output current each servo angle
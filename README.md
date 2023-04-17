#This repository is a modified version of the original poppy-humanoid raspoppy repository.  

#This repository aims to remove the hotspot function and accelerate the script install time by installing correct version of related package.  

1. Install rpi image using the latest one from website
1.1 You may use filezilla or winssp to copy file to pi
1.2 place the folder in home directory 
2. run raspoppyfication.sh script  e.g. ./raspoppyfication.sh
3. Wait for install to finish
4. After finished, run this two command   
apt-get install libatlas-base-dev  


apt-get install libhdf5-serial-dev  

5. Then install virtual keyborad for user.

sudo apt-get install matchbox-keyboard

6. run poppy-services poppy-humanoid --snap 
check if there is any error occur


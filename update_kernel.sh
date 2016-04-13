#/bin/sh

cd ~
sudo rmmod openvswitch
mkdir tempdir
cd tempdir
git clone https://github.com/BU-NU-CLOUD-SP16/Building-a-Network-Marketplace-with-XIA.git
cd Building-a-Network-Marketplace-with-XIA
cp openvswitch.h ~/XIA-for-Linux/include/uapi/linux/
cp -r openvswitch/ ~/XIA-for-Linux/net/
cd ~/XIA-for-Linux/
make clean M=net/openvswitch
make M=net/openvswitch/
sudo install -oroot -groot -m644 net/openvswitch/openvswitch.ko /lib/modules/`uname -r`/kernel/net/openvswitch
sudo modprobe openvswitch
cd ~
rm -rf tempdir

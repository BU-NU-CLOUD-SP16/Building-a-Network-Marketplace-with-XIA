# MOC-XIA

## Group members

Joseph Tierney tierneyj@bu.edu

Krystal Kallarackal krystalk@bu.edu

Nicholas Memme nmemme@bu.edu

Qiaobin Fu qiaobinf@bu.edu

Mentor: Cody Doucette doucette@bu.edu

## Project Description

The eXpressive Internet Architecture (XIA) is an experimental network architecture developed by researchers at BU at other collaborating universities. It is an alternative to the current TCP/IP-based Internet, and emphasizes that applications should be able to more clearly express their needs to the network. For example, the current Internet forces applications to say "find where this movie is, and then go retrieve it at that location." XIA allows applications to more simply say "retrieve this
movie," without caring about where the movie is stored.

In other words, XIA enables applications to more accurately express their intent. This project focuses on applying this powerful tool to allow users and applications to choose better network services, especially in open cloud environments like the Massachusetts Open Cloud (MOC). In the same way that users can choose compute and storage resources from service providers in a marketplace, we envision that users should be able to choose networking services by various vendors as well.

In this project, we will create a very simple version of a networking marketplace. Users and applications will be able to choose between different link and physical technologies that suit their needs. To accomplish this, we will expand XIA in the Linux kernel and add XIA to virtual network switch software, called Open vSwitch (OVS). Although much of the XIA code has already been written in the Linux kernel, we will be modifying it and expanding it to also fit within the constraints of
OVS. We will be coding and hacking in the kernel on both virtual machines and physical computers.

By the end of this project, participants will have gained significant experience in computer networking, cloud computing, Linux kernel programming, Linux and virtual machine configuration, etc.

## Installation and Deployment

### XIA Install
```bash
cd ~
git clone https://github.com/mengxiang0811/XIA-for-Linux.git
cd XIA-for-Linux
sudo make
sudo make install
```
For more detailed installation, please refer to the Linux XIA wiki here https://github.com/AltraMayor/XIA-for-Linux/wiki/How-to-install.
### OVS Kernel Space Install
```bash
cd ~
sudo rmmod openvswitch
git clone https://github.com/BU-NU-CLOUD-SP16/Building-a-Network-Marketplace-with-XIA.git
cd Building-a-Network-Marketplace-with-XIA
cp openvswitch.h ~/XIA-for-Linux/include/uapi/linux/
cp -r openvswitch/ ~/XIA-for-Linux/net/
cd ~/XIA-for-Linux/
make clean M=net/openvswitch
make M=net/openvswitch/
sudo install -oroot -groot -m644 net/openvswitch/openvswitch.ko /lib/modules/`uname -r`/kernel/net/openvswitch
sudo modprobe openvswitch
```

### OVS User Space Install
```bash
cd ~
git clone https://github.com/cjdoucette/ovs.git
cd ovs
sudo make
sudo make install

```
### OVS Setup
```bash
cd ~
sudo modprobe openvswitch
sudo ovsdb-server -v --remote=punix:/usr/local/var/run/openvswitch/db.sock --remote=db:Open_vSwitch,Open_vSwitch,manager_options  --pidfile --detach --log-file
sudo ovs-vsctl --no-wait init
sudo ovs-vswitchd --pidfile --detach
sudo modprobe xia_ppal_hid
sudo modprobe xia_ppal_xdp
```

### Extended Net-echo Application Install
```bash
cd ~
git clone https://github.com/mengxiang0811/net-echo.git
cd net-echo
sudo make
sudo make install
```

### Mininet Install

For the installation of Mininet, please refer to the official website: http://mininet.org/download/

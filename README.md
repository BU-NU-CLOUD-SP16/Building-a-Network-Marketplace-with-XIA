# MOC-XIA

## Group members

Joseph Tierney tierneyj@bu.edu

Krystal Kallarackal krystalk@bu.edu

Nicholas Memme nmemme@bu.edu

Qiaobin Fu qiaobinf@bu.edu

Mentor: Cody Doucette doucette@bu.edu

## Project Description

The [eXpressive Internet Architecture (XIA)](https://github.com/AltraMayor/XIA-for-Linux/wiki) is an experimental network architecture developed by researchers at BU at other collaborating universities. It is an alternative to the current TCP/IP-based Internet, and emphasizes that applications should be able to more clearly express their needs to the network. For example, the current Internet forces applications to say "find where this movie is, and then go retrieve it at that location." XIA allows applications to more simply say "retrieve this movie," without caring about where the movie is stored.

In other words, XIA enables applications to more accurately express their intent. This project focuses on applying this powerful tool to allow users and applications to choose better network services, especially in open cloud environments like the Massachusetts Open Cloud (MOC). In the same way that users can choose compute and storage resources from service providers in a marketplace, we envision that users should be able to choose networking services by various vendors as well.

In this project, we will create a very simple version of a networking marketplace. Users and applications will be able to choose between different link and physical technologies that suit their needs. To accomplish this, we will expand XIA in the Linux kernel and add XIA to virtual network switch software, called [Open vSwitch (OVS)](http://openvswitch.org/). Although much of the XIA code has already been written in the Linux kernel, we will be modifying it and expanding it to also fit within the constraints of
OVS. We will be coding and hacking in the kernel on both virtual machines and physical computers.

By the end of this project, participants will have gained significant experience in computer networking, cloud computing, Linux kernel programming, Linux and virtual machine configuration, etc.

## Where Are Projects Maintained
### XIA
The [eXpressive Internet Architecture (XIA)](https://github.com/AltraMayor/XIA-for-Linux/wiki) is an experimental network architecture aimed at allowing applications and users to more accurately express their intent. Linux XIA is a native implementation of XIA in the Linux kernel. The project website is [here](https://github.com/AltraMayor/XIA-for-Linux/wiki).

### Open vSwitch
Open vSwitch is a virtual multilayer network switch, it has two important components: (1) ovs-vswitchd, a userspace daemon that is essentially the same from one operating system and operating environment to another. (2) datapath kernel module, is usually written specially for the host operating system for performance. For more information, you can read the NSDI'15 paper ["The Design and Implementation of Open vSwitch"](http://openvswitch.org/support/papers/nsdi2015.pdf).

As we extensively modified the OVS project in both user-space and kernel datapath, the OVS user-space project is maintained [here](https://github.com/cjdoucette/ovs), and the OVS kernel datapath is maintained [here](https://github.com/BU-NU-CLOUD-SP16/Building-a-Network-Marketplace-with-XIA/tree/master/openvswitch).

### Extended net-echo Application
[net-echo](https://github.com/AltraMayor/net-echo) is an application built on top of Linux XIA. It implements a simple server (eserv) and client (ecli), where the client sends a message and the server simply echoes it back to the client. 

In the extended version, we adapt net-echo to enforce some price constraint within some time bound, i.e., only allow 5 echo messages to use the more expensive link within a minute. Any echo messages beyond those 5 would have to use the cheaper link until some time expires. The extended net-echo application is maintained [here](https://github.com/mengxiang0811/net-echo).

## Installation and Deployment

### XIA Install
```bash
cd ~
git clone https://github.com/mengxiang0811/XIA-for-Linux.git
cd XIA-for-Linux
sudo make
sudo make install
```
For more detailed installation, please refer to the Linux XIA wiki here: https://github.com/AltraMayor/XIA-for-Linux/wiki/How-to-install.
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

For the installation of Mininet, please refer to its [official website](http://mininet.org/download/).

### Wireshark-XIA
[Wireshark](https://www.wireshark.org/) is a network protocol analyzer that allows users to inspect packet data. It provides a GUI through which users can view conveniently-formatted packet information broken down by protocol. It can be tedious to try to debug Linux XIA based on raw packet bytes. Instead, users can view XIP packets using the [Wireshark with XIA support](https://github.com/AltraMayor/XIA-for-Linux/wiki/Debugging-the-Linux-kernel#Wireshark_with_XIA_support).

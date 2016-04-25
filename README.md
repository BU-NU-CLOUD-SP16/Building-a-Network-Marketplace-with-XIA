# MOC-XIA

## Group members

Joseph Tierney tierneyj@bu.edu

Krystal Kallarackal krystalk@bu.edu

Nicholas Memme nmemme@bu.edu

Qiaobin Fu qiaobinf@bu.edu

Mentor: Cody Doucette doucette@bu.edu

## Project Description

The [eXpressive Internet Architecture (XIA)](https://www.cs.cmu.edu/~xia/) is an experimental network architecture developed by researchers at BU at other collaborating universities. It is an alternative to the current TCP/IP-based Internet, and emphasizes that applications should be able to more clearly express their needs to the network. For example, the current Internet forces applications to say "find where this movie is, and then go retrieve it at that location." XIA allows applications to more simply say "retrieve this movie," without caring about where the movie is stored.

In other words, XIA enables applications to more accurately express their intent. This project focuses on applying this powerful tool to allow users and applications to choose better network services, especially in open cloud environments like the [Massachusetts Open Cloud (MOC)](http://www.bu.edu/cci/files/2012/11/MOC.pdf). In the same way that users can choose compute and storage resources from service providers in a marketplace, we envision that users should be able to choose networking services by various vendors as well.

In this project, we will create a very simple version of a networking marketplace. Users and applications will be able to choose between different link and physical technologies that suit their needs. To accomplish this, we will expand XIA in the Linux kernel and add XIA to virtual network switch software, called [Open vSwitch (OVS)](http://openvswitch.org/). Although much of the XIA code has already been written in the Linux kernel, we will be modifying it and expanding it to also fit within the constraints of
OVS. We will be coding and hacking in the kernel on both virtual machines and physical computers.

By the end of this project, participants will have gained significant experience in computer networking, cloud computing, Linux kernel programming, Linux and virtual machine configuration, etc.

## Scope and Features Of The Project

* Expand XIA in the Linux Kernel
  * Add additional features and functionality to the existing XIA code
  * Enable choice in a data center
    * Users can choose computational and storage resources from service providers in a marketplace, and can choose networking services by various vendors as well.
    * We may reuse the existing features and functionality in current XIA code.
* Port XIA to a virtual network switch software (OVS)
  * Read through pre-written XIA code to determine how it works.
  * Read through OVS code to understand how IP, HTTP, etc. are ported in order to add the necessary code and headers to port XIA as well.
  * Revise code in order to port XIA into OVS to enable a router or switch to recognize XIA much like it recognized protocols like TCP or IP.
    * XIA can act as a transport layer, network layer, and link layer protocol. In this project, we're going to be using it as a link layer protocol that switches packets based on identifiers for links. Once XIA is in place in OVS, then the other functionality it employs (OpenFlow) will work "with" XIA.
    * We need to extend OVS to support the XIP header, so that XIA can work in the data center environment.
    * Also, we need to modify and expand XIA to fit within the constraints of OVS.

* Creating an Application that utilizes XIA on OVS
  * Develop an application using XIA that displays the features and functionality of the architecture.

## Solution Concept

### Global Architectural Structure Of the Project
Below is a description of the system components that are the building blocks of the architectural design:
* XIA: an experimental network architecture created as an alternative to TCP/IP under the premise that applications should be able to more clearly express their needs to the network rather than specifying the location of where to get it from.
* OVS: a virtual multilayer network switch (Open vSwitch)

![alt tag](https://github.com/BU-NU-CLOUD-SP16/Building-a-Network-Marketplace-with-XIA/blob/master/img/ovs-xia.png)

The above figure shows the basic elements in the XIA enabled network. Assuming that both host A and host B are XIA enabled hosts, and A wants to communicate with B via a router/switch with OVS support. Like TCP/IP, the router/switch on the path from A to B needs to understand XIA, otherwise, the packets from A to B cannot be forwarded correctly, or will even be dropped. This highlights one important task in our project, i.e., porting XIA into OVS and making XIA understandable to the network.

![alt tag](https://github.com/BU-NU-CLOUD-SP16/Building-a-Network-Marketplace-with-XIA/blob/master/img/moc-xia.png)

This figure shows the MOC-XIA architecture, in which all the hosts, routers, switches, etc., are XIA enabled, i.e., this is an XIA enabled cloud. In the cloud, it enables networking as a marketplace, so that users can choose better networking services from different providers to meet their desired requirements. For instance, the user may require a networking service provider that can meet their requirements of a low latency and low jitter networking service.

### Design Implications and Discussion

* Using XIA for better expressiveness: XIA enables applications to more accurately express their intent. For instance, the current Internet forces applications to say "find where this movie is, and then go retrieve it at that location." XIA allows applications to more simply say "retrieve this movie," without caring about where the movie is stored.
* Using OVS for multi-server virtualization deployments in data centers: Open vSwitch (OVS) is a production quality, multilayer virtual switch, and enables automated and dynamic network control in large-scale Linux-based virtualization environments through programmatic extension. OVS enables the network to support XIA for creating a networking marketplace.
* Creating a networking marketplace: XIA enabled cloud allows users to choose networking services by various vendors in the same way that users choose compute and storage resources from service providers in a marketplace. This meets the users’ and applications’ need for better networking service.

## Acceptance criteria
Minimum acceptance criteria is a working implementation of XIA on OVS.
Stretch goals are:
* Develop new functionality for XIA to build a network marketplace.
* Build an application that utilizes XIA on OVS, and demonstrate its advantages.

## Release Planning
Release #1 (due by Tuesday Feb 9):
* Learn about the networking concepts, such as the Internet, XIA, Open vSwitch.
 * Basic Internet
  * A quick overview of [how the Internet works](https://www.youtube.com/watch?v=oj7A2YDgIWE)
 * Open vSwitch
  * Brief overivew of [Open vSwitch](https://en.wikipedia.org/wiki/Open_vSwitch).
  * [Detailed of Open vSwitch](https://www.usenix.org/system/files/conference/nsdi15/nsdi15-paper-pfaff.pdf) (try reading sections 1-3).
  * A [video](https://www.usenix.org/conference/nsdi15/technical-sessions/presentation/pfaff) that complements the above paper.
  * The [official website](http://openvswitch.org/).
* XIA
 * The [home page](https://github.com/AltraMayor/XIA-for-Linux/wiki) of one of the projects we'll be working on: the instantiation of XIA in the Linux kernel.
 * A (somewhat technical) [overview of XIA](https://github.com/AltraMayor/XIA-for-Linux/wiki/XIA-101).
 * A (somewhat theoretical) [overview of XIA](https://www.cs.cmu.edu/~xia/resources/Documents/XIA-nsdi.pdf).
 * A [video](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/han_dongsu_xia) that complements the above paper.

Release #2 (due by Tuesday Feb 23):
* Setup the developement environment, and show how to run XIA and OVS.

Release #3 (due by Tuesday March 15):
* Port XIA into OVS.

Release #4 (due by Tuesday March 29):
* Port XIA into OVS, release a demo to show XIA works in OVS.

Release #5 (due by Tuesday April 12):
* Write new functionality in XIA to enable choice in a datacenter.

Release #6 (final demo due by Tuesday April 26):
* Build an application on top of XIA and OVS, to allow users to choose network services for better performance.

## Project Video
We have compiled [a video explanation and demonstration](https://drive.google.com/file/d/0B-shhQisMuMZR295VkNsaW1aT2M/view?ts=571e7b45) of our project.

## Where Are Projects Maintained
### XIA
The [eXpressive Internet Architecture (XIA)](https://github.com/AltraMayor/XIA-for-Linux/wiki) is an experimental network architecture aimed at allowing applications and users to more accurately express their intent. [Linux XIA](https://github.com/AltraMayor/XIA-for-Linux/wiki) is a native implementation of XIA in the Linux kernel.

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
For more detailed installation, please refer to the [Linux XIA wiki](https://github.com/AltraMayor/XIA-for-Linux/wiki/How-to-install).
### OVS Kernel Datapath Install
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

### Wireshark-XIA Install
[Wireshark](https://www.wireshark.org/) is a network protocol analyzer that allows users to inspect packet data. It provides a GUI through which users can view conveniently-formatted packet information broken down by protocol. Users can view XIP packets using the [Wireshark with XIA support](https://github.com/AltraMayor/XIA-for-Linux/wiki/Debugging-the-Linux-kernel#Wireshark_with_XIA_support).

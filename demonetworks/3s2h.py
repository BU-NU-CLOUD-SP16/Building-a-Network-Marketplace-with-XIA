
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.cli import CLI

class Network2(Topo):

	def build(self):


		host1 = self.addHost('h1')
		host2 = self.addHost('h2')

		switch1 = self.addSwitch('s1')
		switch2 = self.addSwitch('s2')
		switch3 = self.addSwitch('s3')
		
		self.addLink(host1,switch1,delay='1ms')
		self.addLink(switch1,switch2,delay='10ms')
		self.addLink(switch1,switch3,delay='1000ms')
		self.addLink(switch2,host2,delay='50ms')
		self.addLink(switch3,host2,delay='2000ms')


topos = { 'network2' : (lambda: Network2() ) }


def startup():
   topo=Network2()
   net=Mininet(topo,link=TCLink)
   net.start()
   dumpNodeConnections(net.hosts)
   CLI(net)
   net.stop()

if __name__=="__main__":
   startup()

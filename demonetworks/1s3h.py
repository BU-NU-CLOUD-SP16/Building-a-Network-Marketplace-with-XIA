
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.util import dumpNodeConnections
from mininet.link import TCLink

class Network1(Topo):

	def build(self):
		

		host1 = self.addHost('h1')
		host2 = self.addHost('h2')
		host3 = self.addHost('h3')

		switch1 = self.addSwitch('s1')
		
		self.addLink(host1,switch1,delay='1ms')
		self.addLink(switch1,host2,delay='10ms')
		self.addLink(switch1,host3,delay='1000ms')
	

topos = { 'network1' : (lambda: Network1() ) }

def startup():
   topo=Network1()
   net=Mininet(topo,link=TCLink)
   net.start()
   dumpNodeConnections(net.hosts)
   CLI(net)
   net.stop()

if __name__=="__main__":
   startup()

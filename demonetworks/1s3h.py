
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.util import dumpNodeConnections

class Network1(Topo):

	def __init__(self):
		Topo.__init__(self)

		host1 = self.addHost('h1')
		host2 = self.addHost('h2')
		host3 = self.addHost('h3')

		switch1 = self.addSwitch('s1')
		
		self.addLink(host1,switch1)
		self.addLink(switch1,host2)
		self.addLink(switch1,host3)
	

topos = { 'network1' : (lambda: Network1() ) }

def startup():
   topo=Network1()
   net=Mininet(topo)
   net.start()
   net.configLinkStatus('h2','s1','down')
   net.configLinkStatus('h3','s1','down')
   dumpNodeConnections(net.hosts)
   CLI(net)
   net.stop()

if __name__=="__main__":
   startup()

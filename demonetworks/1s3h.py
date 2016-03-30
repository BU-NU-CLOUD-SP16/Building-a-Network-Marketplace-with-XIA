
from mininet.topo import Topo
from mininet.net import Mininet
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




from mininet.topo import Topo
from mininet.net import Mininet
class Network2(Topo):

	def __init__(self):
		Topo.__init__(self)

		host1 = self.addHost('h1')
		host2 = self.addHost('h2')

		switch1 = self.addSwitch('s1')
		switch2 = self.addSwitch('s2')
		switch3 = self.addSwitch('s3')
		
		self.addLink(host1,switch1)
		self.addLink(switch1,switch2)
		self.addLink(switch1,switch3)
		self.addLink(switch2,host2)
		self.addLink(switch3,host2)


topos = { 'network2' : (lambda: Network2() ) }



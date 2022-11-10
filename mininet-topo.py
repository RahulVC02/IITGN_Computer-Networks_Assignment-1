from mininet.topo import Topo
from mininet.link import TCLink
from mininet.node import OVSController


class MyTopo(Topo, TCLink, OVSController):

    def _init_(self):
        Topo.build(self) #Initializing the Topology

        #Adding the hosts 

        A = self.addHost('A')       
        B = self.addHost('B')
        C = self.addHost('C')
        D = self.addHost('D')

        #Adding the switches

        R1 = self.addSwitch('R1')
        R2 = self.addSwitch('R2')

        #Adding the links
        L1 = self.addLink(A, R1, cls=TCLink, bw=1000, delay='1ms')
        L5 = self.addLink(D, R1, cls=TCLink, bw=1000, delay='1ms')
        L3 = self.addLink(B, R2, cls=TCLink, bw=1000, delay='1ms')
        L4 = self.addLink(C, R2, cls=TCLink, bw=1000, delay='5ms')
        L5 = self.addLink(R1, R2, cls=TCLink, bw=500, delay='10ms')


topos = {'mytopo': (lambda: MyTopo())}

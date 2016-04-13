sudo ovs-ofctl del-flows s1

#sudo ovs-ofctl add-flow s1 priority=65535,xia,xia_version=1,xia_next_hdr=0,xia_payload_len=5,xia_hop_limit=128,xia_num_dst=2,xia_num_src=2,xia_last_node=126,xia_xid0=0x00000011-82e0476015683b23aa2c6ca1947d407e6241294b,actions=drop

#sudo ovs-ofctl add-flow s1 priority=65535,xia,xia_version=1,xia_next_hdr=0,xia_payload_len=5,xia_hop_limit=128,xia_num_dst=2,xia_num_src=2,xia_last_node=126,xia_xid0=0x00000011-14f57b16cc126f75eed7ce9055c9668fade23121,actions=drop

sudo ovs-ofctl add-flow s1 priority=65535,xia,xia_version=1,xia_next_hdr=0,xia_payload_len=5,xia_hop_limit=128,xia_num_dst=2,xia_num_src=2,xia_last_node=126,xia_xid0=0x00000017-2093723472747047808047502873423749070987,actions=drop

sudo ovs-ofctl add-flow s1 priority=65535,xia,xia_version=1,xia_next_hdr=0,xia_payload_len=5,xia_hop_limit=128,xia_num_dst=2,xia_num_src=2,xia_last_node=126,xia_xid0=0x00000017-2093723472747047808047502873423749070988,actions=drop

sudo ovs-ofctl dump-flows s1

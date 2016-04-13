cmd_net/openvswitch//vport-gre.ko := ld -r -m elf_x86_64 -T ./scripts/module-common.lds --build-id  -o net/openvswitch//vport-gre.ko net/openvswitch//vport-gre.o net/openvswitch//vport-gre.mod.o

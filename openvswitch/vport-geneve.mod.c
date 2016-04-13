#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x6b3bd222, __VMLINUX_SYMBOL_STR(module_layout) },
	{ 0x724777b5, __VMLINUX_SYMBOL_STR(dev_queue_xmit) },
	{ 0xe91a5265, __VMLINUX_SYMBOL_STR(ovs_netdev_tunnel_destroy) },
	{ 0x20b876c, __VMLINUX_SYMBOL_STR(ovs_vport_ops_unregister) },
	{ 0xaa6b594, __VMLINUX_SYMBOL_STR(__ovs_vport_ops_register) },
	{ 0x8ce5541f, __VMLINUX_SYMBOL_STR(ovs_vport_free) },
	{ 0x58d4adfa, __VMLINUX_SYMBOL_STR(ovs_netdev_link) },
	{ 0x6e720ff2, __VMLINUX_SYMBOL_STR(rtnl_unlock) },
	{ 0x36733f8b, __VMLINUX_SYMBOL_STR(dev_change_flags) },
	{ 0xa7409f9f, __VMLINUX_SYMBOL_STR(geneve_dev_create_fb) },
	{ 0xc7a4fbed, __VMLINUX_SYMBOL_STR(rtnl_lock) },
	{ 0xe1729f59, __VMLINUX_SYMBOL_STR(ovs_vport_alloc) },
	{ 0xcd279169, __VMLINUX_SYMBOL_STR(nla_find) },
	{ 0xdb7305a1, __VMLINUX_SYMBOL_STR(__stack_chk_fail) },
	{ 0x8afaebe7, __VMLINUX_SYMBOL_STR(nla_put) },
	{ 0xbdfb6dbb, __VMLINUX_SYMBOL_STR(__fentry__) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=openvswitch,geneve";


MODULE_INFO(srcversion, "D7ECAEC7EED075B88545408");

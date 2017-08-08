#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_file = 'cisco_ipsec.txt'
cisco_cfg = CiscoConfParse(cisco_file)
crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for c_map in crypto_maps:
    print
    print c_map.text
    for child in c_map.children:
        print child.text
print


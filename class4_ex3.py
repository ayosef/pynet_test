#!/usr/bin/env python
'''
Use Pexpect to retrieve the output of 'show ip int brief'
'''

import pexpect
import time
import sys
import re
from getpass import getpass

def find_prompt(ssh_conn):
    '''
    Find the current prompt
    Pexpect is non-greedy which is problematic
    '''
    ssh_conn.send('\n')
    time.sleep(1)
    ssh_conn.expect('#')
    prompt = ssh_conn.before + ssh_conn.after
    return prompt.strip()

def main():
    '''
    Use Pexpect to retrieve the output of 'show ip int brief'
    '''
    ip_addr = raw_input("Enter IP address: ")
    username = 'pyclass'
    port = 22
    password = getpass()

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 5
    time.sleep(3)
    ssh_conn.sendline('yes')
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')
    
    prompt = find_prompt(ssh_conn)

    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect(prompt)

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect(prompt)

    print '\n>>>>'
    print ssh_conn.before
    print '>>>>\n'

if __name__ == "__main__":
    main()


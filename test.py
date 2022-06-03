import argparse

p=argparse.ArgumentParser()
p.add_argument('--cmd1', action='store_const', const=lambda:'cmd1', dest='cmd')
p.add_argument('--cmd2', action='store_const', const=lambda:'cmd2', dest='cmd')

args = p.parse_args(['--cmd1'])
# Out[21]: Namespace(cmd=<function <lambda> at 0x9abf994>)

p.parse_args(['--cmd2']).cmd()
# Out[19]: 'cmd2'
p.parse_args(['--cmd1']).cmd()
# Out[20]: 'cmd1'
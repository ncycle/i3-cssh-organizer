#!/usr/bin/env python
# https://faq.i3wm.org/question/3189/how-can-i-sort-windows-inside-a-container-automatically/

import i3

currentWindow = i3.filter(focused=True)[0]

parentContainer = i3.parent(currentWindow['id'])
if parentContainer['layout'] in ['splitv', 'stacked']:
    direction = 'down'
else:
    direction = 'right'

nodes = parentContainer['nodes']

snodes = sorted(nodes, key=lambda n:n['name'])

for node in snodes[1:]:
    i3.focus(con_id=node['id'])
    i3.move('scratchpad')

i3.focus(con_id=nodes[0]['id'])

for node in snodes[1:]:
    i3.focus(con_id=node['id'])
    i3.floating('disable')

i3.focus(con_id=currentWindow['id'])

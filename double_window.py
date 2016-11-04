#/usr/bin/env python

import i3
import time
import pprint
pp = pprint.PrettyPrinter(indent=4)

currentWindow = i3.filter(focused=True)[0]
scanContainer = currentWindow
workspace_name = ''
while True:
    if scanContainer['type'] == 'workspace':
        workspace_name = scanContainer['name']
        break;
    scanContainer = i3.parent(scanContainer['id'])
print([node['name'] for node in scanContainer['nodes']])
pp.pprint(scanContainer['nodes'])


exit()
print(currentWindow['name'])
parent = i3.parent(currentWindow['id'])
parent = i3.parent(parent['id'])
print(currentWindow['type'])
print(parent['type'])
print(parent['name'])
# this_id = currentWindow['id']
# i3.focus(con_id=this_id)
# i3.move('scratchpad')
# i3.focus(con_id=this_id)
# i3.move('to workspace 10')
# i3.floating('disable')

#results = i3.filter(focused=True)
#results = i3.get_tree()
#print(len(results['nodes']))
#pp.pprint(results)

#currentWindow = i3.filter(focused=True)[0]
#print(currentWindow)
#parentContainer = i3.parent(currentWindow['id'])
#print(parentContainer)
#workspace = i3.parent(parentContainer['id'])
#print(workspace)
##for node

#parentContainer = i3.parent(currentWindow['id'])
#print(parentContainer)
#nodes = parentContainer['nodes']
#print([node['name'] for node in nodes])
#for node in nodes:
#    i3.focus(con_id=node['id'])
#    i3.move('scratchpad')
#
#i3.focus(parentContainer['id'])
#i3.focus(con_id=node['id'])
#i3.move('to workspace 10')




##if parentContainer['layout'] in ['splitv', 'stacked']:
##    direction = 'down'
##else:
##    direction = 'right'
#
#nodes = parentContainer['nodes']
##print(nodes)
#print([node['name'] for node in nodes])
#left_nodes = []
#right_nodes = []
#extra_nodes = []
#keystr = 'CSSH: kallard@db-grid-'
#for node in nodes:
#    if keystr not in node['name']:
#        extra_nodes.append(node)
#    else:
#        hostnum = node['name'][len(keystr):len(keystr)+4]
#        if int(hostnum) % 2 == 1:
#            left_nodes.append(node)
#        else:
#            right_nodes.append(node)
#left_nodes.sort(key=lambda n:n['name'])
#right_nodes.sort(key=lambda n:n['name'])
#
#print("left")
#print([node['name'] for node in left_nodes])
#print("right")
#print([node['name'] for node in right_nodes])
#print("extra")
#print([node['name'] for node in extra_nodes])
#
#left_origin = left_nodes.pop(0)
#print(left_origin)
#right_origin = right_nodes.pop(0)
#
#
#for node in left_nodes + right_nodes + extra_nodes:
#    i3.focus(con_id=node['id'])
#    i3.move('scratchpad')
#
#time.sleep(5)
#i3.focus(con_id=right_origin['id'])
#i3.move('scratchpad')
#i3.focus(con_id=left_origin['id'])
#
#i3.focus(con_id=right_origin['id'])
#i3.floating('disable')
#i3.move('right')
#time.sleep(5)
#
#i3.focus(con_id=left_origin['id'])
#
#for node in left_nodes + right_nodes + extra_nodes:
#    i3.focus(con_id=node['id'])
#    i3.floating('disable')
#    #i3.move('down')
#
#i3.focus(con_id=currentWindow['id'])
#
#
#
##snodes = sorted(nodes, key=lambda n:n['name'])
##
##for node in snodes[1:]:
##    i3.focus(con_id=node['id'])
##    i3.move('scratchpad')
##
##i3.focus(con_id=parentContainer['id'])
##i3.layout('splitv')
##
##i3.focus(con_id=nodes[0]['id'])
##
##for node in snodes[1:]:
##    i3.focus(con_id=node['id'])
##    i3.floating('disable')
##    i3.move('down')
##
##i3.focus(con_id=currentWindow['id'])

# flatten an i3-tree for a workspace into a list
import i3
import time
import pprint
import 

# reorganize windows into 2 columns by default
column_count = sys.argv[1] if len(sys.argv) > 1 else 2

def get_workspace(container):
    if container['type'] == 'workspace':
        return container
    return get_workspace(i3.parent(container['id']))

def get_leaves(node):
    if len(node['nodes']) == 0:
        return [node]
    children = []
    for child in node['nodes']:
        children.extend(get_leaves(child))
    return children

def revisualize(node, workspace_name):
    i3.focus(con_id=node['id'])
    i3.move('to workspace ' + workspace_name)
    i3.floating('disable')

currentWindow = i3.filter(focused=True)[0]
workspace = get_workspace(currentWindow)

leaves = get_leaves(workspace)

for leaf in leaves:
    # the CSSH master window goes in extra
    if 'CSSH: ' in leaf['name']:
        cssh.append(leaf)
    else:
        extra.append(leaf)
cssh.sort(key=lambda n:n['name'])
extra.sort(key=lambda n:n['name'])


for leaf in leaves:
    i3.focus(con_id=leaf['id'])
    i3.move('scratchpad')

i3.focus(con_id=workspace['id'])
i3.layout('splitv')

# base is the horizontal "ceiling" with N windows
# base descends as layers of windows are visualized
base = cssh[:column_count]
stack = cssh[column_count:]

revisualize(base[0], workspace['name'])
i3.split('v')
for leaf in base[1:]:
    revisualize(leaf, workspace['name'])
    i3.move('right')
    i3.split('v')

for idx in range(0,len(stack)):
    abscissa = idx % len(base)
    i3.focus(con_id=base[abscissa]['id'])
    revisualize(stack[idx], workspace['name'])
    base[abscissa] = stack[idx]


for leaf in extra:
    revisualize(leaf, workspace['name'])
    i3.move('down')

workspace_after = i3.filter(id=workspace['id'])[0]
cssh_container = None
for node in reversed(workspace_after['nodes']):
    for resize_iter in range(0,50):
        if node['name'] is None and len(node['nodes']) > 0:
            i3.focus(con_id=node['id'])
            i3.resize('grow up 40 px')
        else:
            i3.focus(con_id=node['id'])
            i3.resize('shrink up 40 px')

for node in extra:
    if 'CSSH ' in node['name']:
        i3.focus(con_id=node['id'])

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(workspace_after)
#for node in workspace_after['nodes']:
#    print(len(node['nodes']))
#
#for i in range(0,4):
#    for leaf in reversed(extra):
#        shrinkable = True
#        while shrinkable:
#            response = i3.resize('grow up 10 px')
#            shrinkable = response[0]
#            response = i3.resize('shrink up 10 px')
#            shrinkable = response[0]
#            print(leaf['name'])
#            print(response)
#            time.sleep(0.1)
#        print(leaf['rect']['height'])

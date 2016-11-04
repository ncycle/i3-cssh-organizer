# flatten an i3-tree for a workspace into a list
import i3
import time
import pprint

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

left, right, extra = [], [], []
for leaf in leaves:
    if 'CSSH: ' in leaf['name']:
        numerical = ''.join([c for c in leaf['name'] if c.isdigit()])
        if int(numerical) % 2 == 1:
            left.append(leaf)
        else:
            right.append(leaf)
    else:
        extra.append(leaf)
left.sort(key=lambda n:n['name'])
right.sort(key=lambda n:n['name'])
extra.sort(key=lambda n:n['name'])

print("left")
print([node['name'] for node in left])
print("right")
print([node['name'] for node in right])
print("extra")
print([node['name'] for node in extra])


for leaf in leaves:
    i3.focus(con_id=leaf['id'])
    i3.move('scratchpad')

i3.focus(con_id=workspace['id'])
i3.layout('splith')
first_left = left.pop(0)
revisualize(first_left, workspace['name'])
first_right = right.pop(0)
revisualize(first_right, workspace['name'])

time.sleep(5)

i3.focus(con_id=first_left['id'])
i3.layout('splitv')
time.sleep(5)
for leaf in left:
    revisualize(leaf, workspace['name'])

i3.focus(con_id=first_right['id'])
i3.layout('splitv')

time.sleep(5)
for leaf in right:
    revisualize(leaf, workspace['name'])

for leaf in extra:
    revisualize(leaf, workspace['name'])

#
#
#for leaf in leaves:
#    i3.focus(con_id=leaf['id'])
#    i3.move('to workspace ' + workspace_name)
#    i3.floating('disable')

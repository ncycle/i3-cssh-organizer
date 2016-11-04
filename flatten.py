# flatten an i3-tree for a workspace into a list
import i3

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
    

currentWindow = i3.filter(focused=True)[0]
workspace = get_workspace(currentWindow)
workspace_name = workspace['name']

leaves = get_leaves(workspace)
for leaf in leaves:
    i3.focus(con_id=leaf['id'])
    i3.move('scratchpad')

for leaf in leaves:
    i3.focus(con_id=leaf['id'])
    i3.move('to workspace ' + workspace_name)
    i3.floating('disable')

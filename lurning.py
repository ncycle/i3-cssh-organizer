import i3

currentWindow = i3.filter(focused=True)[0]
parentContainer = i3.parent(currentWindow['id'])
i3.focus(con_id=parentContainer['id'])
i3.layout('splitv')
nodes = parentContainer['nodes']

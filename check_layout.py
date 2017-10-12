#!/usr/bin/env python

import i3
import pprint
pp = pprint.PrettyPrinter(indent=4)

currentWindow = i3.filter(focused=True)[0]
i3.focus(con_id=currentWindow['id'])
pp.pprint(currentWindow)
height = currentWindow['rect']['height']
print(height)
print(height - 235)
#i3.resize('shrink height 10')
i3.resize('grow height 1000')

#!/usr/bin/env python

import i3

currentWindow = i3.filter(focused=True)[0]

parentContainer = i3.parent(currentWindow['id'])
print(parentContainer['layout'])

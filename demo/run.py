#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys 
sys.path.append('..')

import config
from misterhat import MisterhatServer

server = MisterhatServer(config)
server.run()

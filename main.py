#!/usr/bin/python2
"""Starts the Tweeteor Server."""
from base64 import b64encode
from ConfigParser import SafeConfigParser
import logging

from controllerGUI import Controller
from searcher import Searcher
from server import Server

if __name__ == "__main__":
    #Starts logger for debugger
    logging.basicConfig(filename = 'server.log',
                        level=logging.DEBUG,
                        format="""[%(asctime)s : %(levelname)s]
                                  [%(threadName)s] %(message)s""")
    config = SafeConfigParser()
    config.read('server.conf')
                    
    address = ('', config.getint('connection', 'port'))
    #Creates credentials for twitter api
    credentials = b64encode(config.get('auth', 'key') +
                                       ':' + config.get('auth', 'secret'))
    searcher = Searcher(credentials, address)
    searcher.start()
    controller = Controller(searcher)
    controller.start()

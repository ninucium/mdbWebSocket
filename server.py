#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modbus/TCP server

import socket
import errno
import time
from pyModbusTCP.server import ModbusServer, DataBank

if __name__ == "__main__":
    # init server
    server = ModbusServer(host='localhost', port = 502, no_block=True)
    server.start()

    # main loop
    arr = [1]
    a = 1
    while True:
        a +=1
        arr[0] = a
        DataBank.set_words(0, arr)
        time.sleep(1)

#!/usr/bin/env python

# WS server that sends messages at random intervals


import datetime, time, random, websockets, asyncio
from pyModbusTCP.client import ModbusClient

regData = 0
data = 'test1'
async def time(websocket, path):
    try:
        while True:
            now = datetime.datetime.utcnow()
            await websocket.send()
            await asyncio.sleep(1)
    except Exception as err:
        print('Sorry, an error has occured:\n{0}'.format(err))




c = ModbusClient(host='localhost', port=502)
async def modb():
    try:
        while True:
            if not c.is_open():
                if not c.open():
                    print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
                    # if open() is ok, read register (modbus function 0x03)
            if c.is_open():
                # read 10 registers at address 0, store result in regs list
                regs = c.read_holding_registers(0, 1)
                for reg in regs:
                    regData = reg
                    print(regData)
            await asyncio.sleep(1)
            # sleep 2s before next polling
    except Exeption as err:
        print(err)


ioloop = asyncio.get_event_loop()
start_server = websockets.serve(time, '127.0.0.1', 5678)
tasks = [start_server, ioloop.create_task(modb())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.run_forever()

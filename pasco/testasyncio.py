import asyncio
from bleak import BleakScanner

def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())

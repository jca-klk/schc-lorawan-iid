# SPDX short identifier: BSD-3-Clause
import argparse
from binascii import hexlify
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import cmac

def aes128_cmac(msg, key, length=4):
    c = cmac.CMAC(algorithms.AES(key), backend=default_backend())
    c.update(msg)
    mac = c.finalize()
    return mac[:length]

def args_to_bytes(arg, length):
    if "0x" in arg:
        val = int(arg, 16).to_bytes(length, "big")
    elif len(arg) == 2*length:
        val = bytes.fromhex(arg)
    else: # Try int(..., 0) conversion, or fail
        val = int(arg, 0).to_bytes(length, "big")
    return val

def main():
    parser = argparse.ArgumentParser(
            description = "SCHC-over-LoRaWAN IID computation")
    parser.add_argument("devEUI", help="LoRaWAN Device EUI")
    parser.add_argument("key", help="LoRaWAN AppSKey")
    args = parser.parse_args()

    devEUI = args_to_bytes(args.devEUI, 8)
    key = args_to_bytes(args.key, 16)

    iid = aes128_cmac(devEUI, key, length=8)
    print(hexlify(iid).decode().upper())

if __name__ == "__main__":
    main()

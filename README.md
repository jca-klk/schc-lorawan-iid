# SCHC-over-LoRaWAN IID computation

## TL;DR

```shell
$ python3 schc-lorawan-iid.py 1122334455667788 00AABBCCDDEEFF00AABBCCDDEEFFAABB
4E822D9775B26499
```

## What is this?

This Python script computes the [SCHC-over-LoRaWAN](https://tools.ietf.org/html/draft-ietf-lpwan-schc-over-lorawan) IID, as defined in section "Interface IDentifier (IID) computation".

## Requirements

Before running this script please install requirements, as documented by [pip](https://pip.pypa.io/en/latest/user_guide/#requirements-files).

You should consider runnning this script in a [virtual environment](https://docs.python.org/3/tutorial/venv.html).

```shell
python3 -m pip install -r requirements.txt
```

## Usage
```shell
usage: schc-lorawan-iid.py [-h] devEUI key

SCHC-over-LoRaWAN IID computation

positional arguments:
  devEUI      LoRaWAN Device EUI
  key         LoRaWAN AppSKey

optional arguments:
  -h, --help  show this help message and exit
```

## License
SPDX short identifier: BSD-3-Clause


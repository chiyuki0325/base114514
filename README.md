# Base114514
> 🔏 The algorithm from Shimokitazawa.

Base114514 encoding is based on Base64, but replaces each of the 64 characters with a combination of 1, 4, and 5 digits.

| Plain text | Base64 encoded | Base114514 encoded                               |
| ---------- | -------------- | ------------------------------------------------ |
| 1919810    | MTkxOTgxMA==   | 554145511114141151544551145414115541114541144114 |

### Usage

##### ➡ CLI

`base114514` cli works like `base64` command from GNU coreutils.

```bash
printf 'いいよ、来いよ' | base114514  # Encode base114514 from stdin
base114514 '野獸先輩.png'  # Encode a file to base114514
base114514 --help  # To view help message
```

##### 🐍 Python

`base114514` also works as a Python package like `base64` in Python standard library.  
You can install it from PyPI.

```python
import base114514

base114514.b114514encode('いいよ、来いよ'.encode())
base114514.b114514decode('554145511114141151544551145414115541114541144114')
```

>🛈 Tips:
>
>Base114514 is inspired by memes derived from 真夏の夜の淫夢, which should not be abused everywhere and may be offensive.
>Don't be a homo kid, start with me.

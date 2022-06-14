# Installation
```cmd
pip install ...
```

# Example
- `main.py`
```python
import pydustry

pydustry.Server("easyplay.su").get_status()
```

- `Return`
```python
Status(name='[#3bffff][*] []EasyPlay Gaming + [#3dffcb]Rating-System', map='EasyPlay.HUB', players=56, wave=1, version=126, vertype='official', ping=35)
```
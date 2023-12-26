# Installation
```cmd
pip install -U pydustry.py
```

# Example
- `main.py`
```python
import pydustry

status = pydustry.Server("easyplay.su").get_status()

print(status)
```

- `Return`
```python
Status(name='[#3bffff][*] []EasyPlay Gaming + [#3dffcb]Rating-System', map='EasyPlay.HUB', players=21, wave=1, version=146, vertype='official', gamemode=0, limit=69, desc='[royal]--- [#ffffff]Русско[#4751ff]язычный [#ff4747]Сервер [green]24\\7[royal] ---', modename='', ping=20)
```

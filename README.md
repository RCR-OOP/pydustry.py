# Installation
```cmd
pip install -U pydustry.py
```

# Example
- `main.py`
```python
import pydustry

status = pydustry.Server("rcrms.ru").get_status()

print(status)
```

- `Return`
```python
Status(
    name='[gold]RCR [#B5B8B1]- [white]Ру[blue]сс[red]кий [#B5B8B1]Сервер',
    map='RCR HUB',
    players=7,
    wave=1,
    version=146,
    vertype='official',
    gamemode=0,
    limit=0,
    desc='...',
    modename='LOBBY',
    ping=37
)
```

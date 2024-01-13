# asyncStart.py
Async library for start.ru
![p1_3273805_62dd91e0](https://github.com/aminobotskek/start/assets/94906343/35cc5b5e-0eca-4749-8f5e-68f89540923b)


# Install
```
git clone https://github.com/aminobotskek/asyncStart
```

### Example
```python3
import asyncStart
import asyncio
async def main():
	client=asyncStart.asyncStart()
	await client.login(email="",password="")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

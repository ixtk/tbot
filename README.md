Command prefix: `>`

| Command | Brief |
|--------------------|------------------------------------------|
| load/unload/reload | Load/unload/reload extension             |
| 8ball              | Get a random (yes/no) answer to question |
| fact               | Show a random fact                       |
| roll               | Generate a random number                 |
| covid              | Get Covid-19 data by country             |
| ban/kick/unban     | Moderate server                          |
>Type >help for more info

---

### Run locally

- Navigate to project folder
- Create virtual environment(optional)
```
python -m venv venv
```
- Install dependencies
```
pip install -r requirements.txt
```
- Set `BOT_TOKEN` env variable to your Discord bot token

```python
bot.run(os.getenv('BOT_TOKEN')) # run.py
```

- Run with `python run.py`

#### Other

Tweak server role and message ids
```python
    def __init__(self, bot):
        self.bot = bot
        self.role_message_ids = [856250741694136341, 856447452533751818]
        self.emoji_to_role = {
            '🟢': 856251410353618955,
            '🟡': 856251467715313704,
            '🎉': 856447097892110357
        }
```
>/src/cogs/moderation.py
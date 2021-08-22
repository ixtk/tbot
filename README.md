Command prefix: `>`

### Features
- API integration (covid-19 data, random facts)
- Reaction roles
- Custom help command

| Command | Brief |
|--------------------|------------------------------------------|
| load/unload/reload | Load/unload/reload extension             |
| 8ball              | Get a random (yes/no) answer to question |
| fact               | Show a random fact                       |
| roll               | Generate a random number                 |
| covid              | Get Covid-19 data by country             |
| ban/kick/unban     | Moderate server                          |
| serverinfo         | Display some server stats                |
| help               | List all commands by category            |

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
# /src/cogs/moderation.py

self.role_message_ids = [856250741694136341, 856447452533751818]
self.emoji_to_role = {
    '🟢': 856251410353618955,
    '🟡': 856251467715313704,
    '🎉': 856447097892110357
}
```

Allow help commands in only certain channels(based on channel id)
```python
# /src/cogs/help.py

self.help_channels = [878903467488464906, 779445592560500819]
```

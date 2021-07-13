# Kalendar
A simple Discord bot to save and fetch dates, such as birthdays.

------

### Requirements
- Python 3
- Python's Discord API. Use `pip install -U discord.py` to install.

---

### Command syntax
- **/bind** : To be used in the channel where you want the bot to send the date reminders. Requires administrator privileges.
- **/birthday set `{xx/xx or xx/xx/xxxx}` `{STD/US}`** : Will save the birthday prompted by the user. The years are optionnal. The foramt also needs to be specified (STD for DD/MM/YYYY, US for MM/DD/YYYY)
- **/birthday @user** : Displays @user's birthday.
- **/date set "{title}" {xx/xx/xxxx} {STD/EU}** : Saves a date that isn't a birthday. Works like the `/birthday set` command, except that a title is required.

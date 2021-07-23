# Kalendar
A simple Discord bot to save and fetch birth dates. When the day comes, the bot will send a reminder in every server where both the bot and the user are present in. A channel must've been set by admins for the reminders beforehand (see the %bind command)

------

#### Requirements
- Python 3
- Python's Discord API. Use `pip install -U discord.py` to install.
- DotEnv library. Use `pip install python-dotenv` to install.


---

#### Command syntax
- **%bind** : To be used in the channel where you want the bot to send the date reminders. Requires administrator privileges.
- **%kal set `xx/xx(/xxxx)` `{EU/US}`** : Will save the birthday prompted by the user. The year is optionnal. The format also needs to be specified (EU for DD/MM/YYYY, US for MM/DD/YYYY)
- **%kal fetch @user** : Displays @user's birthday.
- ~~**%date set "`{title}`" `{xx/xx/xxxx}` `{EU/US}`** : Saves a date that isn't a birthday. Works like the `/birthday set` command, except that a title is required.~~

---

#### TO-DO LIST
- [X] Design the initial structure
###### Design:
- [X] Design the Data layer & its UTs
- [X] Design the Logic layer & its UTs
- [X] Design the Input layer
###### Unit Tests:
- [X] Write Data UTs
- [ ] Write Logic UTs
###### Implementation:
- [X] Implement the Data layer
- [X] Implement the Logic layer
- [X] Implement the Input layer

--------

### Suggestions and Improvements:
- Grant the possibility to set a date that isn't a birthday

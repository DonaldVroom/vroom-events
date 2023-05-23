# VROOM events project

## Translations

flask translate init LANG to add a new language
flask translate update to update all language repositories
flask translate compile to compile all language repositories

## Cron

* * * * * cd /Users/alexpauwels/Documents/Vroom/vroom-events && . venv/bin/activate && flask emailreports >> cron.log 2>&1
#!/bin/bash
osascript -e 'tell application "Terminal"
	activate
    do script "cd ~/side/catch" in selected tab of the front window
    do script "export FLASK_APP=run.py" in selected tab of the front window
    do script "export FLASK_DEBUG=true" in selected tab of the front window
    do script "flask run" in selected tab of the front window
    
    delay 1
    tell application "System Events"
        keystroke "t" using {command down}
    end tell
    do script "cd ~/side/catch" in selected tab of the front window
    do script "psql" in selected tab of the front window
    do script "\\c newdb" in selected tab of the front window

    delay 1
    tell application "System Events"
        keystroke "t" using {command down}
    end tell
    do script "cd ~/side/catch" in selected tab of the front window
    do script "git status" in selected tab of the front window
end tell'

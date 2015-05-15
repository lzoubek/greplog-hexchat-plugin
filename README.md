Greplog
=====
A plugin that alows you grep channel/PM log files. 

### Requirements
- Python scripting interface plugin for Hexchat.
- grep binary, for linux users.

### Installation

##### Windows
- copy greplog.py into ```%appdata%\HexChat\addons```. Once there, it will load automatically.

  ##### Linux
  - run ```install.sh``` or copy greplog.py into ```~/.config/hexchat/addons```

  ### Features
  - search in current channel/PM log
  - search in given channel/PM log. This may be helpful if you're looking for something that was mentioned in PM and you don't have corresponding chat window open

  ### Usage
  - ```/greplog <pattern>``` -- Runs in context of your current channel window, finds appropriate log file and (on linux) runs ```grep``` command passing by ```pattern``` argument
  - ```/chgreplog <channel|nick> <pattern>``` -- Runs in context of your network/server, finds appropriate log file for given channel/nick and runs ```grep``` command passing by ```pattern``` argument

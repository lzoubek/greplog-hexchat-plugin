import hexchat,os,re

__author__ = "Libor Zoubek"
__email__  = "lzoubek@redhat.com"

__module_name__ = "greplog"
__module_version__ = "1.0"
__module_description__ = "grep channel / user logs"


import platform
is_linux = platform.system().find('Linux') == 0

__greplog_usage__ = "/greplog <pattern> grep for given pattern in log for current channel / network"
__cgreplog_usage__ = "/chgreplog <channel|nick> <pattern> grep for given pattern in log for given channel in current network"

__usage__ = "Usage:\n" + __greplog_usage__ + "\n" + __chgreplog_usage__

hexchat.prnt(__module_name__ + " " + __module_version__ +" module loaded!\n" + __usage__)

def error(message):
    hexchat.prnt("\00304" + message)

def cb_greplog(word, word_eol, userdata):
    if len(word) < 2:
        error(__greplog_usage__)
        return hexchat.EAT_ALL
    channel = hexchat.get_info("channel")
    return greplog(channel, word_eol[1])

def cb_ch_greplog(word, word_eol, userdata):
    if len(word) < 3:
        error(__chgreplog_usage__)
        return hexchat.EAT_ALL
    channel = word[1]
    return greplog(channel, word_eol[2])

def greplog(channel, pattern):

    logmask = hexchat.get_prefs("irc_logmask")
    logfile = logmask.replace("%n", hexchat.get_info("network")).replace("%s",hexchat.get_info("server")).replace("%c",channel)
    logfile = os.path.join(hexchat.get_info("configdir"), "logs", logfile)

    if not os.path.isfile(logfile):
        error("log-file %s does not exist" % logfile)
        return hexchat.EAT_ALL

    if is_linux:
        # on linux
        hexchat.command("exec grep '" + pattern + "' " + logfile)

    else:
        with open(logfile, "r") as f:
            for line in f:
                try:
                    if re.search(pattern, line):
                        hexchat.prnt(line)
                except:
                    if line.find(pattern) > -1:
                        hexchat.prnt(line)

    return hexchat.EAT_ALL

hexchat.hook_command("GREPLOG", cb_greplog, help = __greplog_usage__)
hexchat.hook_command("CHGREPLOG", cb_ch_greplog, help = __chgreplog_usage__)

# ip-check
Auto email messaging script. Has my public ip changed? If so, send an email to these people


## Properties
```
[p]
dev_mode        -> dev environment toggle. true = dev/local env, false = live/prod environment
last_ip         -> path to last_ip file ex: C:\Dev\ip\last_ip
log_file        -> path to log file ex: C:\Dev\ip\logfile.log
site_link       -> used in email message content
use_kill_switch -> true  = script will use kill switch feature, using the exe 'kill_switch_exe'
                   false = disable kill switch feature
kill_switch_exe -> name of exe, if this exe is running and use_kill_switch=true script will stop ex: Discord.exe

[Sender]
email           -> gmail address sending the email (must configure on google's side)
password        -> app password for above email

[TestRecipients]
recipient       -> your personal email, if dev_mode=true email will only be sent to this address

[Recipients]
recipients      -> list of people who will be sent the email if dev_mode=false
                   see project.properties.template for syntax
```

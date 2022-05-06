# ip-check
Auto email messaging script. Has my public ip changed? If so, send an email to these people


### Properties
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

### Deployment (Windows 10)

**Step 1**
Modify properties/email content/subject line, setup gmail account for automation

**Step 2**
Create the following file **run.bat** with these contents:
```
@echo off
"***\AppData\Local\Programs\Python\Python310\python.exe" "***\ip-check\ip.py"
pause
```
*"path to python exe" "path to ip.py"*

**Step 3**
- Open Windows Task Scheduler
- Click Create a Basic Task
- Set your desired name/description
- Set trigger, mine is daily, set as you please
- Set action to Start a Program - browse to run.bat which you made in Step 2

Done! Once your job is made, you can find it in the list of scheduled tasks and configure further if necessary

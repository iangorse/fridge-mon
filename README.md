# fridge-mon

### What is it?
Simply sends me a notification email when my non-smart fridge turns off!

### Background
The property where I live in has a really poor power outlets. So much that the only outlet available to plug in my fridge freezer is
located in the dining room.

This requires an extension lead from the corner of the dining room to the fridge freezer.

This is not a problem on it's own, the problem is **Dexter Gorse**

Dexter Gorse is an adorable 15 month old toddler who loves pressing switches. As you can guess - one switch is the extension cable.

After finding out the fridge freezer was turned off for the upteenth time (and not knowing how long it had been turned off), I decided to monitor it.

The problem is, my fridge freezer is not a smart fridge freezer and has zero network capabilities.

### Technicalities
To determine if the non-smart fridge was switched off was very simple. All I do, is plug in a small wifi capable device into the extension lead, and when this powers off I know my little monkey has turned the extension lead off.

An old Raspberry Pi generation 2 with USB dongle was a perfect device to fit my needs.

I also have a Raspberry Pi plugged directly into my router which acts as a PiHole device, perfect machine to monitor my Raspberry Pi fridge edition.

### How it works
Its very straight forward.

I simply ping my Raspberry Pi Fridge Edition (RPI FE from now on) continuously, and when the ping fails I send myself an email.
However, the Raspberry Pi Fridge Edition is in a pretty poor location that routinely drops wifi connection for a few seconds. I do not want to be alerted with this.

So the PiHole will detect when the RPI FE has lost connection, if it still down after 5 minutes *then* send myself a notification email.

When the RPI FE comes back on (because I switched the extension lead back on), the Monitor sends me a "Hey, fridge is back on, it was off for x amount of minutes" email.

### Installation Instructions
Clone the repo

`git clone https://github.com/iangorse/fridge-mon.git`

Copy the sample config file

`cp config-sample.json config.json`

Edit the config.json file with your favourite editor, replace variables to meet your email settings

`vim config.json`

`smtp-server` = Email SMTP server

`from` = The from address in email

`to` = The To address in email (who the recipient is)

`username` = The login name for the SMTP server

`password` = the password for the SMTP server

`server` = The target device to check if it's up or not


Update DEBUG variable to True in fridge.py for testing purposes

`vim fridge.py`


Run and switch off target server and wait for email notification! (takes couple minutes with default settings)

`python fridge.py`


Turn DEBUG mode back off once happy and re-run `fridge.py`




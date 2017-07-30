# Newsletter
A Newsletter service which accepts subscribers and mails a newsletter at a configurable interval.
The service consists of two parts. One part is a web service that manages user subscriptions. 
The other part is a script that constructs the newsletter, connects to a mail server, and sends the message to the subscriber list stored in the database.
To use, run db_create.py, and then db_migrate.py. Check config.py and update your SECRET_KEY. 
Finally, execute run.py for the web service. You'll need to set the newsletter mailer up to send on an interval, but I haven't reached that stage yet.

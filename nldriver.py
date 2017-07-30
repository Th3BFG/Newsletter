import time
import logging
import threading

# The driver for the newsletter mailer. 
# Responsible for the creation and sending of newsletters.
		# Steps to mail:
		# 1. Construct newsletter
		# 2. Fetch subscriber list
		# 3. Connect to mail server
		# 4. Send message
		# 5. Clean up
class NewsletterDriver:
	# ctor
	def __init__(self):
		logging.info('Constructing newsletter')
		





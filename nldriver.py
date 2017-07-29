import time
import logging
import threading

# The driver for the service. 
# Maintains the subscriber service and sending of newsletters
class NewsletterDriver:
	# Constants

	# ctor
	def __init__(self):
		logging.info('Starting Newsletter Driver')
		# Set condition for shutdown
		self.condition = threading.Condition()
		# Create Subscriber Service
		# Start Newsletter Sending Loop

	# Shutdown
	def shutdown(self):
		with self.condition:
			logging.info('Begining Shutdown Process')
			self.run = False
			logging.info('Notifying Threads')
			self.condition.notifyAll()


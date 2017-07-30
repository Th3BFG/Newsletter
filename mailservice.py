import sys
import logging
from optparse import OptionParser
from nldriver import NewsletterDriver

# Main entry point
def main():
	# Set up args parsing
	parser = OptionParser()
	parser.add_option("-l", "--log", dest="loglevel", default="WARNING",
				help="Set the logging level to LVL - Options: INFO, WARNING, ERROR", metavar="LVL")
	(options, args) = parser.parse_args()
	# Start logging with args
	logLvl = options.loglevel
	logging.basicConfig(format='[%(levelname)s](%(threadName)-10s):%(message)s', level=get_log_lvl(logLvl))
	# Start the newsletter service
	logging.info('Starting Newsletter Driver')
	driver = NewsletterDriver()

# Based on lvl, return enum logging level
def get_log_lvl(lvl):
	if lvl == 'INFO' or lvl == 'WARNING' or lvl == 'ERROR':
		return getattr(logging, lvl)
	else:
		# Poor formatting of lvl - set to default
		return logging.WARNING

if __name__ == '__main__':
	main()


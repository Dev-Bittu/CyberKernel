from cyberkernel.settings import DEBUG
import logging

logger = logging.getLogger('MiddleWare')
logger.setLevel(logging.DEBUG) if DEBUG else logger.setLevel(logging.WARNING)
fh = logging.FileHandler('logs/visitors.log')
formatter = logging.Formatter(
	'[*] {asctime} :: {name} :: {filename} :: {funcName} :: {lineno} :: {levelname:<8} {message}', style='{'
	)
fh.setFormatter(formatter)
logger.addHandler(fh)

class LogVisitorsMiddleware:
	def __init__(self, get_response):
		logger.info('Web server started...')
		self.get_response = get_response
	
	def __call__(self, request):
		logger.info(f'IP:{request.META.get("REMOTE_ADDR")} VISITING:{request.META.get("PATH_INFO")} QUERY_STRING:{request.META.get("QUERY_STRING")}')
		response = self.get_response(request)
		return response
		
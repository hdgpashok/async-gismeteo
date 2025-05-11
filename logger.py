from aiologger.loggers.json import JsonLogger
from aiologger.handlers.files import AsyncFileHandler



logger = JsonLogger.with_default_handlers(
    level= 'DEBUG',
    serializer_kwargs= {'ensure_ascii' : False}
)

logger.handlers.clear()
logger.add_handler(AsyncFileHandler("app.log"))
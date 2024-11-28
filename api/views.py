from django.shortcuts import render
import logging

logger = logging.getLogger("bb")


# Create your views here.
def index(request):
    logger.debug("debug信息")
    logger.info("info信息")
    logger.warning("warning信息")
    logger.error("error信息")
    return render(request, "index.html")


# login

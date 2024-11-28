from django.shortcuts import render
import logging
import time
from django.http import JsonResponse
import requests


logger = logging.getLogger("api")


def current(request):
    # 模拟调用外部API
    # 这里调用一个真实的外部API，比如 JSONPlaceholder
    # response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    response = requests.get("https://jsonplaceholder.typicode.com/posts/10")
    time.sleep(2)  # 模拟延迟
    return JsonResponse(response.json())


# Create your views here.
def index(request):
    logger.debug("debug信息")
    logger.info("info信息")
    logger.warning("warning信息")
    logger.error("error信息")
    return render(request, "index.html")

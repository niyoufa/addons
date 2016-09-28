#coding=utf-8

from tornado.options import options
from dxb.handler import TokenAPIHandler,APIHandler,ListCreateAPIHandler,\
    RetrieveUpdateDestroyAPIHandler
import libs.utils as utils
import libs.modellib as model
import models

class LinkListCreateHandler(ListCreateAPIHandler):
    model = models.LinkModel()

class LinkRetrieveUpdateDestroyHandler(RetrieveUpdateDestroyAPIHandler):
    model = models.LinkModel()

handlers = [
    (r"/api/link/list", LinkListCreateHandler),
    (r"/api/link", LinkRetrieveUpdateDestroyHandler),
]

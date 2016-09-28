#coding=utf-8

from tornado.options import options
from dxb.handler import TokenAPIHandler,APIHandler,ListCreateAPIHandler,\
    RetrieveUpdateDestroyAPIHandler
import libs.utils as utils
import libs.modellib as model
import models

class LinkListCreateHandler(ListCreateAPIHandler):
    model = models.LinkModel()

    def get(self):
        try:
            keyword = self.get_argument("keyword","")
            if keyword != "":
                self.mg_query_params.update({
                    "title":{"$regex":keyword}
                })
        except Exception, e:
            result = utils.reset_response_data(0, str(e))
            self.write(result)
            self.finish()
            return
        ListCreateAPIHandler.get(self)

class LinkRetrieveUpdateDestroyHandler(RetrieveUpdateDestroyAPIHandler):
    model = models.LinkModel()

handlers = [
    (r"/api/link/list", LinkListCreateHandler),
    (r"/api/link", LinkRetrieveUpdateDestroyHandler),
]

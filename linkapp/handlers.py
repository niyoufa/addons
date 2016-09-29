#coding=utf-8

import datetime

from tornado.options import options
from dxb.handler import TokenAPIHandler,APIHandler,ListCreateAPIHandler,\
    RetrieveUpdateDestroyAPIHandler
import libs.utils as utils
import libs.modellib as model
import models

class LinkListCreateHandler(ListCreateAPIHandler):
    model = models.LinkModel()

    def get(self):
        result = utils.init_response_data()
        try:
            keyword = self.get_argument("keyword","")
            if keyword != "":
                self.mg_query_params.update({
                    "title":{"$regex":keyword}
                })
            self.mg_sort_params = {
                "last_read_time":-1,
                "count":-1,
            }
        except Exception, e:
            result = utils.reset_response_data(0, str(e))
            self.write(result)
            self.finish()
            return
        ListCreateAPIHandler.get(self)

class LinkRetrieveUpdateDestroyHandler(RetrieveUpdateDestroyAPIHandler):
    model = models.LinkModel()

class LinkCountHandler(APIHandler):
    model = models.LinkModel()

    mp_require_params = ["id"]
    mp_update_params = ["id"]

    def get(self):
        result = utils.init_response_data()
        try:
            _id = self.get_argument("_id")
            link = self.model.search({"_id":utils.create_objectid(_id)})
            if link:
                count = link.get("count",0) + 1
                last_read_time = str(datetime.datetime.now())
                query_params = {"_id":utils.create_objectid(_id)}
                update_params = {"count":count,"last_read_time":last_read_time}
                self.model.update(query_params,update_params)
        except Exception, e:
            result = utils.reset_response_data(0, str(e))
            self.write(result)
            self.finish()
            return
        self.finish(result)

handlers = [
    (r"/api/link/list", LinkListCreateHandler),
    (r"/api/link", LinkRetrieveUpdateDestroyHandler),
    (r"/api/link/count", LinkCountHandler),
]

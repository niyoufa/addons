#coding=utf-8

import libs.modellib as model
import libs.utils as utils

class LinkModel(model.BaseModel,model.Singleton):
    __name = "newbie.link"

    def __init__(self):
        model.BaseModel.__init__(self,LinkModel.__name)
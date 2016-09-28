#coding=utf-8

import libs.modellib as model
import libs.utils as utils

class CheckCode(model.BaseModel,model.Singleton):
    __name = "dxb.checkcode"

    def __init__(self):
        model.BaseModel.__init__(self,CheckCode.__name)

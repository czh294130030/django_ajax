# Django 查询结果转换为JSON
def model2json(data):
    data.__dict__.pop("_state");
    rData = data.__dict__;
    return rData;

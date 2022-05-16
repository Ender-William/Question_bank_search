
def flatten(listText):
    def _flatten(item):
        if isinstance(item, dict):
            for value in item.values():
                yield from _flatten(value)
        else:
            yield item

    return [list(_flatten(d)) for d in listText]

def DictToList(Jso):
    value_list = list(Jso.values())
    return value_list
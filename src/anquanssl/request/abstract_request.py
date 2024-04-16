class AbstractRequest(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        self[key] = value

    def __getitem__(self, key):
        return self[key]

    def __delitem__(self, key):
        del self[key]

    def __contains__(self, key):
        return key in self

    def toArray(self):
        return dict(self)
__author__ = 'Howie'


class Formatter:

    @classmethod
    def format(cls, url, title, body):
        para = dict()
        para["url"] = url
        para["title"] = title
        para["body"] = body
        return para
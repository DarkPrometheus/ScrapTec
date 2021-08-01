""" Base class for web resource """

from Fetcher import fetch


def flatten(a_list):
    """ Convert a list of list into a one dimentional list """
    length = len(a_list)
    while length > 0:
        current = a_list.pop(0)
        if isinstance(current, list):
            a_list.extend(current)
        else:
            a_list.push(current)
        length -= 1

    return a_list


class Resource:
    """ Web Resource """

    def __init__(self, url, xpath,
                 validation=None, name_extractor=None,
                 url_extractor=None):
        self.url = url
        self.xpath = xpath
        self.content = None
        self.result = None
        self.name_extractor = name_extractor
        self.url_extractor = url_extractor
        self.val_func = validation

    def fill(self, content, xpath=None):
        """ set the resource content """

        self.content = content

        if xpath is None:
            xpath = self.xpath

        self.result = content.xpath(xpath)
        return self.result

    def fetch(self):
        """ Fetchs the content """
        content = self.fill(fetch(self.url))

        if content is None:
            print('Invalid result')
            return None

        content = list(filter(self.val_func, content))

        if self.url_extractor and self.name_extractor:
            def format_elm(elm):
                return self.name_extractor(elm), self.url_extractor(elm)

            content = list(map(format_elm, content))

        self.result = content
        return content

    def set_name_extractor(self, func):
        """ Setter """
        self.name_extractor = func

    def set_url_extractor(self, func):
        """ Setter """
        self.url_extractor = func

    def set_validation(self, func):
        """ Setter """
        self.val_func = func


class ResourceList:
    """ Resource List """

    def __init__(self, ls, validation=None):
        self.list = ls

        if validation is not None:
            for element in self.list:
                if element.val_func is None:
                    element.set_validation(validation)

    def fetch(self):
        """ Call fetch func for each element """
        return flatten(list(map(
            lambda elm: elm.fetch(),
            self.list)))

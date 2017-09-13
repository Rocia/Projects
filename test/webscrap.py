import pprint, simplejson, sys,subprocess,json
import urllib3, certifi,re
from bs4 import BeautifulSoup as Soup
from datetime import datetime
 
def attribute_checker(operator, attribute, value=''):
    """
    Takes an operator, attribute and optional value; returns a function that
    will return True for elements that match that combination.
    """
    return {
        '=': lambda el: el.get(attribute) == value,
        # attribute includes value as one of a set of space separated tokens
        '~': lambda el: value in el.get(attribute, '').split(),
        # attribute starts with value
        '^': lambda el: el.get(attribute, '').startswith(value),
        # attribute ends with value
        '$': lambda el: el.get(attribute, '').endswith(value),
        # attribute contains value
        '*': lambda el: value in el.get(attribute, ''),
        # attribute is either exactly value or starts with value-
        '|': lambda el: el.get(attribute, '') == value \
            or el.get(attribute, '').startswith('%s-' % value),
    }.get(operator, lambda el: el.has_key(attribute))
 
 
def select(soup, selector):
    """
    soup should be a BeautifulSoup instance; selector is a CSS selector 
    specifying the elements you want to retrieve.
    """
    tokens = selector.split()
    current_context = [soup]
    for token in tokens:
        m = attribselect_re.match(token)
        if m:
            # Attribute selector
            tag, attribute, operator, value = m.groups()
            if not tag:
                tag = True
            checker = attribute_checker(operator, attribute, value)
            found = []
            for context in current_context:
                found.extend([el for el in context.findAll(tag) if checker(el)])
            current_context = found
            continue
        if '#' in token:
            # ID selector
            tag, id = token.split('#', 1)
            if not tag:
                tag = True
            el = current_context[0].find(tag, {'id': id})
            if not el:
                return [] # No match
            current_context = [el]
            continue
        if '.' in token:
            # Class selector
            tag, klass = token.split('.', 1)
            if not tag:
                tag = True
            found = []
            for context in current_context:
                found.extend(
                    context.findAll(tag,
                        {'class': lambda attr: attr and klass in attr.split()}
                    )
                )
            current_context = found
            continue
        if token == '*':
            # Star selector
            found = []
            for context in current_context:
                found.extend(context.findAll(True))
            current_context = found
            continue
        # Here we should just have a regular tag
        if not tag_re.match(token):
            return []
        found = []
        for context in current_context:
            found.extend(context.findAll(token))
        current_context = found
    return current_context
 
def monkeypatch(BeautifulSoupClass=None):

    if not BeautifulSoupClass:
        from BeautifulSoup import BeautifulSoup as BeautifulSoupClass
    BeautifulSoupClass.findSelect = select
 
def unmonkeypatch(BeautifulSoupClass=None):
    if not BeautifulSoupClass:
        from BeautifulSoup import BeautifulSoup as BeautifulSoupClass
    delattr(BeautifulSoupClass, 'findSelect')
pp = pprint.PrettyPrinter(indent=4)

def download_content_source(url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    response = http.request('GET', url)
    return response.data.decode('utf-8')

tag_re = re.compile('^[a-z0-9]+$')
 
attribselect_re = re.compile(r'^(?P<tag>\w+)?\[(?P<attribute>\w+)(?P<operator>[=~\|\^\$\*]?)' + r'=?"?(?P<value>[^\]"]*)"?\]$')
contenturl = download_content_source("http://Sakthivel.J:Pass@2511@inviewapp.cch.com/lbautolog/Pages/LogSearch.aspx")
content = download_content_source("http://inviewapp.cch.com/lbautolog/Pages/LogSearch.aspx")      
soup = Soup(content, "html.parser")
#title = select(soup , ".contest-info h1")[0].contents[0]
print(soup.prettify().encode('utf-8'))
#data = urllib3.urlopen("http://Sakthivel.J:Pass@2511@inviewapp.cch.com/lbautolog/Pages/LogSearch.aspx")
#url = urllib3.urlopen("http://inviewapp.cch.com/lbautolog/Pages/LogSearch.aspx")    
#content = url.read()    
#soup = Soup(content)
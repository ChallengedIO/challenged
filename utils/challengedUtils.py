import urllib.request
import xml.etree.ElementTree
import os.path

DEBUG = False

class Parser:
    def __init__(self, x):
        self.x = x

class Loader:
    def __init__(self, x):
        self.x = x

class Downloader:
    def __init__(self, x):
        self.x = x

class Initializer:
    def __init__(self, x):
        self.x = x

class Daemonizer:
    def __init__(self, x):
        self.x = x

class Challenge:
    def __init__(self, x):
        self.x = x

def main():
    if DEBUG:
        try:
            global events
            global xml_root
            global xml_cmnpfx
            global tmp_ele
        except:
            pass

    endpoint = 'http://s3.amazonaws.com/ctf-challenges/'
    events = dict()
    opener = urllib.request.build_opener()

    #Query and proc CTF events
    #TODO: Move this to a processor class or function
    xml_req = opener.open(endpoint + '?prefix=&delimiter=/')
    xml_str = xml_req.read().decode('utf-8')
    xml_root = xml.etree.ElementTree.fromstring(xml_str)
    xml_cmnpfx = xml_root.findall('./')

    for ele in xml_cmnpfx:                         
        try:
            ele.tag.index('CommonPrefix')
            events[ele.getchildren()[0].text.strip('//')] = {}
        except:
            pass

    #Query and proc CTF event years
    for eve in events:
        prfx = eve + '/'
        query_str = endpoint + '?prefix=' + prfx + '&delimiter=/'
        xml_req = opener.open(query_str)
        xml_str = xml_req.read().decode('utf-8')
        xml_root = xml.etree.ElementTree.fromstring(xml_str)
        xml_cmnpfx = xml_root.findall('./')
        for ele in xml_cmnpfx:                         
            try:
                ele.tag.index('CommonPrefix')
                tmp_path = ele.getchildren()[0].text.strip('//')
                eve_yr = os.path.basename(tmp_path)
                events[eve][eve_yr] = {}
            except:
                pass

    #Query and proc CTF event categories
    for eve in events:
        for eve_yr in events[eve]:
            prfx = eve + '/' + eve_yr + '/'
            query_str = endpoint + '?prefix=' + prfx + '&delimiter=/'
            xml_req = opener.open(query_str)
            xml_str = xml_req.read().decode('utf-8')
            xml_root = xml.etree.ElementTree.fromstring(xml_str)
            xml_cmnpfx = xml_root.findall('./')
            for ele in xml_cmnpfx:                         
                try:
                    ele.tag.index('CommonPrefix')
                    tmp_path = ele.getchildren()[0].text.strip('//')
                    cat = os.path.basename(tmp_path)
                    events[eve][eve_yr][cat] = {}
                except:
                    pass

    #Query and proc CTF event difficulties
    for eve in events:
        for eve_yr in events[eve]:
            for cat in events[eve][eve_yr]:
                prfx = eve + '/' + eve_yr + '/' + cat + '/'
                query_str = endpoint + '?prefix=' + prfx + '&delimiter=/'
                xml_req = opener.open(query_str)
                xml_str = xml_req.read().decode('utf-8')
                xml_root = xml.etree.ElementTree.fromstring(xml_str)
                xml_cmnpfx = xml_root.findall('./')
                for ele in xml_cmnpfx:                         
                    try:
                        ele.tag.index('CommonPrefix')
                        tmp_path = ele.getchildren()[0].text.strip('//')
                        dif = os.path.basename(tmp_path)
                        events[eve][eve_yr][cat][dif] = {}
                    except:
                        pass
    #Process user request

if __name__ == '__main__':
  main()

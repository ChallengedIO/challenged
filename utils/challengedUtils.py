import urllib.request
import xml.etree.ElementTree
import os.path
import tempfile

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
        self.event = x[0]
        self.year = x[1]
        self.category = x[2]
        self.difficulty = x[3]
        self.name = x[4]

def main():
    if DEBUG:
        try:
            global challenges
        except:
            pass

    endpoint = 'http://s3.amazonaws.com/ctf-challenges/'
    xmltag_contents = '{http://s3.amazonaws.com/doc/2006-03-01/}Contents'
    xmltag_key = '{http://s3.amazonaws.com/doc/2006-03-01/}Key'
    regex_fullpath = '^([^\/]+\/){5}$'
    regex_partpath = '([^\/]+)\/' 
    tmpfile_manifest = tempfile.TemporaryFile()
    challenges = []

    #Download current ListBucketResult
    xml_req = urllib.request.urlopen(endpoint + '?prefix=&delimiter=')

    tmpfile_manifest.write(xml_req.read())
    tmpfile_manifest.seek(0)

    xml_root = xml.etree.ElementTree.parse(tmpfile_manifest)

    tmpfile_manifest.close()
    print('Updated database...')

    #Filter out the non-sense
    for e in xml_root.findall(xmltag_contents):
        for k in e.findall(xmltag_key):
            if re.search(regex_fullpath, k.text) is not None:
                m = re.findall(regex_partpath, k.text)
                new_challenge = Challenge(m)
                challenges.append(new_challenge)

    print('Loaded {} challenges!!!'.format(len(challenges)))
    '''
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
                        break
                    except:
                        pass
    #Process user request
    '''

if __name__ == '__main__':
  main()

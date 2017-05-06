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

def search_by_property(q, p, l):
    tmp = []
    #TODO: Figure out a more streamlined way to resolve this if more \
        #properties get added
    prop_muxer = {
        'event' : lambda c:  c.event,
        'year' : lambda c:  c.year,
        'category' : lambda c:  c.category,
        'difficulty' : lambda c:  c.difficulty,
        'name' : lambda c:  c.name,
    }
    func = prop_muxer.get(p, lambda: None)

    if func == None:
        raise InputError('Could not resolve query parameter.')

    for c in l:
        if func(c) == q:
            tmp.append(c)
    return tmp

def print_challenges_list(l):
    for c in l:
        print('{')
        print("\tName: {}".format(c.name))
        print("\tCategory: {}".format(c.category))
        print("\tDifficulty: {}".format(c.difficulty))
        print("\tEvent: {}".format(c.event))
        print("\tYear: {}".format(c.year))
        print('}')

#TODO: Add or refactor a search function that takes a list of parameters

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
    print('Updating and indexing database...')
    print('Go give yourself a well deserved break 🌯 ☕️')
    xml_req = urllib.request.urlopen(endpoint + '?prefix=&delimiter=')

    tmpfile_manifest.write(xml_req.read())
    tmpfile_manifest.seek(0)

    print('Database updated 👌')

    xml_root = xml.etree.ElementTree.parse(tmpfile_manifest)

    tmpfile_manifest.close()

    #Filter out the non-sense
    for e in xml_root.findall(xmltag_contents):
        for k in e.findall(xmltag_key):
            if re.search(regex_fullpath, k.text) is not None:
                m = re.findall(regex_partpath, k.text)
                new_challenge = Challenge(m)
                challenges.append(new_challenge)

    print('Database indexed 👌')
    print('Loaded {} challenges 👌'.format(len(challenges)))

    print('Get nosql-160 challenge')
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print_challenges_list(search_by_property('nosql-160', 'name',  challenges))
    print()

    print('Get all pwn challenges')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    print_challenges_list(search_by_property('pwn', 'category',  challenges))
    print()

    print('Get all level 1 challenges')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print_challenges_list(search_by_property('1', 'difficulty',  challenges))
    print()

    print('Get all challenges from all 9447 event(s)')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print_challenges_list(search_by_property('9447', 'event',  challenges))
    print()

    print('Get all challenges from 2014')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print_challenges_list(search_by_property('2014', 'year',  challenges))
    print()

if __name__ == '__main__':
  main()

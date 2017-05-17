#! /usr/bin/python3
# -*- coding: utf-8 -*-

# This code allows the game client to operate cleaner by "hiding all the bodies" here.

import re
import urllib.request
import xml.etree.ElementTree
import os.path
import tempfile

import utils.CIODownloader as CIODownloader
import utils.CIOInitializer as CIOInitializer
import utils.CIODaemonizer as CIODaemonizer

endpoint        = 'http://s3.amazonaws.com/ctf-challenges/'
recipe_path_fmt = '{}/{}/{}/{}/{}/recipe.xml'
xmltag_contents = '{http://s3.amazonaws.com/doc/2006-03-01/}Contents'
xmltag_key      = '{http://s3.amazonaws.com/doc/2006-03-01/}Key'
regex_fullpath  = '^([^\/]+\/){5}$'
regex_partpath  = '([^\/]+)\/' 
files_path_fmt  = '({}\/{}\/{}/{}/{}\/[^\/]+$)'

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

def update_manifest():
    """ Update challenge list from S3 bucket """
    xml_req = urllib.request.urlopen(endpoint + '?prefix=&delimiter=')

    manifest = tempfile.TemporaryFile()
    manifest.write(xml_req.read())
    manifest.seek(0)

    xml_root = xml.etree.ElementTree.parse(manifest)
    manifest.close()

    challenges = []

    # Filter out the non-sense
    for e in xml_root.findall(xmltag_contents):     
        for k in e.findall(xmltag_key):
            if re.search(regex_fullpath, k.text) is not None:
                m = re.findall(regex_partpath, k.text)
                nc = Challenge(m)
                challenges.append(nc)
    return challenges

def get_recipe_url(c):
    recipe_url_fmt = endpoint + '{}/{}/{}/{}/{}/recipe.xml'
    return recipe_url_fmt.format(c.event, c.year, c.category, c.difficulty, \
                                 c.name)
    
def search_by_property(q, p, l):

    '''    
    # More examples:
    
    print('Get nosql-160 challenge')
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    CIOUtils.print_challenges_list(CIOUtils.search_by_property('nosql-160', 'name',  challenges))
    print()

    print('Get all level 1 challenges')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    CIOUtils.print_challenges_list(CIOUtils.search_by_property('1', 'difficulty',  challenges))
    print()

    print('Get all challenges from all 9447 event(s)')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    CIOUtils.print_challenges_list(CIOUtils.search_by_property('9447', 'event',  challenges))
    print()

    print('Get all challenges from 2014')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    CIOUtils.print_challenges_list(CIOUtils.search_by_property('2014', 'year',  challenges))
    print()
    '''

    tmp = []
    # TODO: Figure out a more streamlined way to resolve this if more \
    # properties get added
    prop_muxer = {
        'event'      : lambda c : c.event,
        'year'       : lambda c : c.year,
        'category'   : lambda c : c.category,
        'difficulty' : lambda c : c.difficulty,
        'name'       : lambda c : c.name,
    }
    func = prop_muxer.get(p, lambda: None)

    if func == None:
        raise InputError('Could not resolve query parameter.')

    for c in l:
        if func(c) == q:
            tmp.append(c)
    return tmp

# TODO: Determine if this should be resolved in the recipe
def get_challenge_files(c, r):
    regex_file = files_path_fmt.format(c.event, c.year, c.category, \
                                       c.difficulty, c.name)
    print(regex_file)
    for e in xml_root.findall(xmltag_contents):
        for k in e.findall(xmltag_key):
            if re.search(regex_file, k.text) is not None:
                print(k.text)

def get_challenge_recipe(c):
    print(get_recipe_url(c))

def print_challenges_list(l):
    for c in l:
        print('{')
        print("\tName: {}".format(c.name))
        print("\tCategory: {}".format(c.category))
        print("\tDifficulty: {}".format(c.difficulty))
        print("\tEvent: {}".format(c.event))
        print("\tYear: {}".format(c.year))
        print('}')




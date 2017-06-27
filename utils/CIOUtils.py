#! /usr/bin/python3
# -*- coding: utf-8 -*-

# This code allows the game client to operate cleaner by 'hiding all the bodies' here.

import requests
import re
import urllib.request
import xml.etree.ElementTree
import os.path
import tempfile
import base64
import subprocess

from utils.CIODownloader import CIODownloader as CIODownloader
from utils.CIOInitializer import CIOInitializer as CIOInitializer
from utils.CIODaemonizer import CIODaemonizer as CIODaemonizer

endpoint        = 'https://s3.amazonaws.com/ctf-challenges/'
recipe_path_fmt = '{}/{}/{}/{}/{}/recipe.xml'
xmltag_contents = '{http://s3.amazonaws.com/doc/2006-03-01/}Contents'
xmltag_key      = '{http://s3.amazonaws.com/doc/2006-03-01/}Key'
regex_fullpath  = '^([^\/]+\/){5}$'
regex_partpath  = '([^\/]+)\/' 
files_path_fmt  = '({}\/{}\/{}/{}/{}\/[^\/]+$)'

class Challenge:
    def __init__(self, x):
        self.event = x[0]
        self.year = x[1]
        self.category = x[2]
        self.difficulty = x[3]
        self.name = x[4]

class Recipe:
    def __init__(self, recipe_xml_root):
        #Metadata
        self.metadata = dict()
        self.metadata['event'] = \
        recipe_xml_root.find('metadata').find('event').text
        self.metadata['year'] = \
        recipe_xml_root.find('metadata').find('year').text
        self.metadata['category'] = \
        recipe_xml_root.find('metadata').find('category').text
        self.metadata['difficulty'] = \
        recipe_xml_root.find('metadata').find('level').text
        self.metadata['name'] = \
        recipe_xml_root.find('metadata').find('name').text
        self.metadata['points'] = \
        recipe_xml_root.find('metadata').find('points').text

        #Temp dir
        self.dir = \
        tempfile.TemporaryDirectory(prefix=self.metadata['name'] + \
        '_')

        #Downloader
        self.downloader = []
        e_list = recipe_xml_root.find('downloader').findall('element')
        for e in e_list:
            url = e.find('url').text
            sha = e.find('sha256').text
            tmp_obj = {'url': url, 'sha': sha}
            self.downloader.append(tmp_obj)

        #Initializer
        self.initializer = ''
        e_file_xml_root = \
        recipe_xml_root.find('initializer').find('install').find('vagrantfile')
        e_file_text = base64.b64decode(e_file_xml_root.text.strip())
        vagrant_file = open(os.path.join(self.dir.name, \
        'Vagrantfile'), 'wb')
        vagrant_file.write(e_file_text)
        vagrant_file.close()

        #Daemonizer
        self.daemonizer = []
        e_list = \
        recipe_xml_root.find('daemonizer').find('cmd').findall('element')
        for e in e_list:
            self.daemonizer.append(e.text)

def update_manifest():
    ''' Update challenge list from S3 bucket '''
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

#TODO: Depricate in favor for CIODownloader, which parses recipe
def get_recipe_url(c):
    recipe_url_fmt = endpoint + '{}/{}/{}/{}/{}/recipe.xml'
    return recipe_url_fmt.format(c.event, c.year, c.category, c.difficulty, \
                                 c.name)

def from_recipe_url(u):
    xml_req = urllib.request.urlopen(u)
    xml_root = xml.etree.ElementTree.fromstring(xml_req.read())
    #print(xml_req.read())
    return Recipe(xml_root)
    
def search_by_property(q, p, l):
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
        print('\tName: {}'.format(c.name))
        print('\tCategory: {}'.format(c.category))
        print('\tDifficulty: {}'.format(c.difficulty))
        print('\tEvent: {}'.format(c.event))
        print('\tYear: {}'.format(c.year))
        print('}')

#Returns a list of unique member values on a list of Challenge objs
def get_unique_properties(p, l):
    result = set()
    for c in l:
        found_prop = {
            'name': lambda c: c.name,
            'category': lambda c: c.category,
            'difficulty': lambda c: c.difficulty,
            'event': lambda c: c.event,
            'year': lambda c: c.year,
        }[p](c)
        result.add(found_prop)
    return list(result)


def fetch(category, difficulty):
    c = CIODownloader()
    r = requests.get(c.url)

    return c

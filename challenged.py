#! /usr/bin/python3
# -*- coding: utf-8 -*-

import re
import urllib.request
import xml.etree.ElementTree
import os.path
import tempfile

import utils.challengedUtils as CIOUtils


endpoint = 'http://s3.amazonaws.com/ctf-challenges/'
recipe_path_fmt = '{}/{}/{}/{}/{}/recipe.xml'
xmltag_contents = '{http://s3.amazonaws.com/doc/2006-03-01/}Contents'
xmltag_key = '{http://s3.amazonaws.com/doc/2006-03-01/}Key'
regex_fullpath = '^([^\/]+\/){5}$'
regex_partpath = '([^\/]+)\/' 
files_path_fmt = '({}\/{}\/{}/{}/{}\/[^\/]+$)'

# This is the client, code should be focused on user-interaction only and 
# handling the interface between the core and the user

def main():
    if __debug__:
        try:
            global xml_root
            global challenges
        except:
            pass

    tmpfile_manifest = tempfile.TemporaryFile()
    challenges = []

    #Download current ListBucketResult
    print('Updating and indexing database')
    print('Go take a well deserved break 🌯 ☕️')
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
                nc = CIOUtils.Challenge(m)
                challenges.append(nc)

    print('Database indexed 👌')
    print('Loaded {} challenges 👌'.format(len(challenges)))
    
    print('Get all pwn challenges')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    CIOUtils.print_challenges_list(CIOUtils.search_by_property('pwn', 'category',  challenges))
    print()

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

    print('Get all files from nosql-160 challenge')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    cur_c = CIOUtils.search_by_property('europe02-120', 'name',  challenges)[0]
    #get_challenge_files(cur_c, xml_root)
    CIOUtils.get_challenge_recipe(cur_c)

if __name__ == '__main__':
  main()
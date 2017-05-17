#! /usr/bin/python3
# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree
import os.path
import tempfile

import utils.challengedUtils as CIOUtils

# This is the client, code should be focused on user-interaction only and 
# handling the interface between the core and the player. To reduce complexity, the client should
# not handle any flags/options directly. Instead, emulate game design
# concepts and challenge the player.

#  1) Greet the player
#  2) Difficulty?
#  3) Update challenge list from S3 bucket
#  4) Index challenge list
#  5) Fetch challenge via CIODownloader
#  6) Provision OS for challenge via CIOInitializer
#  7) Execute challenge as a service, send player info via CIODaemonizer

def main():
    # 1) Greet the player
    print('READY PLAYER ONE')

    # 2) Difficulty?
    print ('SELECT DIFFICULTY [1-5]')
    
    # 3) Update challenge list
    print('[+] UPDATING DATABASE')

    challenges = CIOUtils.update_manifest()

    print('Loaded {} challenges 👌'.format(len(challenges)))
    
    # 5) Fetch challenge via CIODownloader

    #print('Get all pwn challenges')
    #print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    #CIOUtils.print_challenges_list(CIOUtils.search_by_property('pwn', 'category',  challenges))
    #print()

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

	#  6) Provision OS for challenge via CIOInitializer 
	#  7) Execute challenge as a service, send player info via CIODaemonizer


if __name__ == '__main__':
	if __debug__:
	    try:
	        global xml_root
	        global challenges
	    except:
	        pass

	main()

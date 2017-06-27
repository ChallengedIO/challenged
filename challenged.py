#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.CIOUtils as CIOUtils

# This is the client, code should be focused on user-interaction only and 
# handling the interface between the core and the player. To reduce complexity, the client should
# not handle any flags/options directly. Instead, emulate game design
# concepts and challenge the player.

#  1) Greet the player
#  2) Update challenge list from S3 bucket
#  3) Difficulty/Category? 
#  4) Fetch challenge via CIODownloader
#  5) Provision OS for challenge via CIOInitializer
#  6) Execute challenge as a service, send player info via CIODaemonizer

#TODO: Replace with a challenge obj that can be used as a query param
LEVEL = ''
CATEGORY = ''
NAME = ''
EVENT = ''
YEAR = ''

def select_level(challenges):
    print ('Available levels:')
    unq_lvls = sorted(CIOUtils.get_unique_properties('difficulty', \
                                              challenges))
    i = 0
    for lvl in unq_lvls:
        print('{}: {}'.format(i, lvl))
        i += 1

    sel = int(input('SELECT LEVEL [0-{}]: '.format(len(unq_lvls))))
    if sel not in range(0, len(unq_lvls)):
        raise ValueError
    global LEVEL
    LEVEL = unq_lvls[sel]

def select_category(challenges):
    print ('Available categories:')
    unq_cats = sorted(CIOUtils.get_unique_properties('category', \
                                              challenges))
    i = 0
    for cat in unq_cats:
        print('{}: {}'.format(i, cat))
        i += 1

    sel = int(input('SELECT CATEGORY [0-{}]: '.format(len(unq_cats))))
    if sel not in range(0, len(unq_cats)):
        raise ValueError
    global CATEGORY
    CATEGORY = unq_cats[sel]
    
def main():
    # 1) Greet the player
    print('[+] READY PLAYER ONE')

    # 2) Update Manifest
    print('[+] UPDATING CHALLENGES')
    challenges = CIOUtils.update_manifest()
    print('[+] {} CHALLENGES LOADED 👌'.format(len(challenges)))
    
    while True:
        try:
            # 2) LEVEL/CATEGORY
            select_level(challenges)
            select_category(challenges)
        except ValueError:
            print('naughty boy. naughty, naughty naughty!')
            continue

        filtered_chals = challenges
        filtered_chals = CIOUtils.search_by_property(CATEGORY, 'category', filtered_chals)
        filtered_chals = CIOUtils.search_by_property(LEVEL, 'difficulty', filtered_chals)
        print('filtered on: {} and {}'.format(CATEGORY, LEVEL))
        CIOUtils.print_challenges_list(filtered_chals)
        # 5) Fetch challenge via CIODownloader
        #challenge = CIOUtils.fetch(CATEGORY, difficulty)
        #print (challenge.url)

if __name__ == '__main__':
	if __debug__:
	    try:
	        global xml_root
	        global challenges
	        print (challenges)
	    except:
	        pass
	main()

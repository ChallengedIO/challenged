#! /usr/bin/python3
# -*- coding: utf-8 -*-

import utils.challengedUtils as CIOUtils

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

CATEGORY = "PWN"

def main():
    # 1) Greet the player
    print('[+] READY PLAYER ONE')

    # 2) Update Manifest
    print('[+] UPDATING CHALLENGES')
    challenges = CIOUtils.update_manifest()
    print('[+] {} CHALLENGES LOADED 👌'.format(len(challenges)))
    
    # 2) DIFFICULTY/CATEGORY
    while True:
	    try:
	    	dontoverflowmebro = input('SELECT DIFFICULTY [1-5]: ')
	    	if dontoverflowmebro is "1":
	    		print ('[+] DIFFICULTY SET TO {}'.format(dontoverflowmebro)) #set Challenge.difficulty=1 - define func to handle this in utils
	    		break
	    	elif dontoverflowmebro is "2":
	    		print ('[+] DIFFICULTY SET TO {}'.format(dontoverflowmebro))
	    		break
	    	elif dontoverflowmebro is "3":
	    		print ('[+] DIFFICULTY SET TO {}'.format(dontoverflowmebro))
	    		break
	    	elif dontoverflowmebro is "4":
	    		print ('[+] DIFFICULTY SET TO {}'.format(dontoverflowmebro))
	    		break
	    	elif dontoverflowmebro is "5":
	    		print ('[+] DIFFICULTY SET TO {}'.format(dontoverflowmebro))
	    		break
	    except ValueError:
	    	print('naughty boy. naughty, naughty naughty!')
	    	break

	# TODO: Include additional categories as they become available, hold ya horses! 
    print ('[+] CATEGORY SET TO {}'.format("pwn").upper())

    # 5) Fetch challenge via CIODownloader
    challenge = CIOUtils.fetch(CATEGORY, dontoverflowmebro)
    print (challenge.url)

if __name__ == '__main__':
	if __debug__:
	    try:
	        global xml_root
	        global challenges
	        print (challenges)
	    except:
	        pass

	main()


    #print('Get all pwn challenges')
    #print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    #CIOUtils.print_challenges_list(CIOUtils.search_by_property('pwn', 'category',  challenges))
    #print()

	'''
    print('Get all files from nosql-160 challenge')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    cur_c = CIOUtils.search_by_property('europe02-120', 'name',  challenges)[0]
    get_challenge_files(cur_c, xml_root)
    CIOUtils.get_challenge_recipe(cur_c)
	'''

	#  6) Provision OS for challenge via CIOInitializer 
	#  7) Execute challenge as a service, send player info via CIODaemonizer


#usage
#python3 coex.py combo.txt extracted.txt

from sys import argv
import re

script , combo_file , ex_file = argv

cfile = open(combo_file)
xfile = open(ex_file, 'w')
def rexmail(cfile):
	rexmail = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+:[a-zA-Z0-9._-]+')
	cfile = rexmail.findall(cfile.read())
	
	lenofclist = len(cfile)
	for i in range(lenofclist):
		xfile.write("\n")
		xfile.write(str(cfile[i]))
		
	print("[+]*********EXTRACTING DONE***********[+]\n")
	print("[+]*********CHECK extracted.txt FILE FOR EMAIL:PASS COMBOS*************[+]\n")




def header():
	print('''
			made with <3

 _______           ___    ___      _________        ________          ________          ________          _________        ________          ________     
|\  ___ \         |\  \  /  /|    |\___   ___\     |\   __  \        |\   __  \        |\   ____\        |\___   ___\     |\   __  \        |\   __  \    
\ \   __/|        \ \  \/  / /    \|___ \  \_|     \ \  \|\  \       \ \  \|\  \       \ \  \___|        \|___ \  \_|     \ \  \|\  \       \ \  \|\  \   
 \ \  \_|/__       \ \    / /          \ \  \       \ \   _  _\       \ \   __  \       \ \  \                \ \  \       \ \  \\\  \       \ \   _  _\  
  \ \  \_|\ \       /     \/            \ \  \       \ \  \\  \|       \ \  \ \  \       \ \  \____            \ \  \       \ \  \\\  \       \ \  \\  \| 
   \ \_______\     /  /\   \             \ \__\       \ \__\\ _\        \ \__\ \__\       \ \_______\           \ \__\       \ \_______\       \ \__\\ _\ 
    \|_______|    /__/ /\ __\             \|__|        \|__|\|__|        \|__|\|__|        \|_______|            \|__|        \|_______|        \|__|\|__|
                  |__|/ \|__|                                                                                                                             
                                                                                                       EMAIL:PASS extractor from any txt file .                                                   
                                                                                                                                                          

''')


header()

rexmail(cfile)









 



	





	

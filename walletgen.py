import os
from bitcoin import * #pip3 install bitcoin, pybitcointools #https://github.com/vbuterin/pybitcointools
	
def main():
	"""Main interface"""
	
	print("Bitcoin wallet generator\n\n Created by: Prematrix\nhttps://github.com/prematrix/BitcoinWalletGen")
	print("**WARNING: make sure that u don't have a privatekey.txt file in this directory. If so, it will be overwritten.")
	while True:
		choise = input("\n1. Single-sig\n2. Multi-sig\nChoise: ")
		if choise == "1" or choise.lower() == "single-sig":
			walletgen()
		elif choise == "2" or choise.lower() == "multi-sig":
			multiwalletgen()
			
def walletgen():
	"""Method that generates a singe-signature wallet"""
	
	#Creating a private key and address
	priv = random_key()
	addr = pubtoaddr(privtopub(priv))
	writer("privatekey", priv)
	writer("address", addr)
	print("**Address and private key have been generated. Check the working directory")
	
def multiwalletgen():
	"""Method that generaates a multi-signature wallet"""
	
	nos = int(input("\nHow many keys need to be created: "))
	nons = int(input("How many keys are needed for a transaction: "))
	
	#User input error checking
	if nons > nos:
		print("\n**The number of needed keys can't be higher than the number of total keys")
		return
		
	if nons < 0 or nos < 0:
		print("\n**Negative numbers are not allowed")
		return
		
	keys = []
	# Generating the needed private keys
	for x in range(1, nos + 1):
		priv = random_key()
		keys.append(priv)
		writer("privatekey" + str(x), priv)
	
	# Creating the multisignature script and writing the address to a file
	scr = mk_multisig_script(keys, nons, nos)
	writer("multisig-address", scriptaddr(scr))
		
def writer(name, text):
	"""Method that writes to files
	
	Keyword arguments:
    name -- the name for the file
    text -- the string that is writed to the file
	"""
	
	file = open(name + '.txt', "w")
	file.write(text)
	file.close()
	
main()
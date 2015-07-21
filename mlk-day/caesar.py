# A simple Caesar Cipher

"""
	The Caesarian Cipher was the first encryption algorithm
	Each letter of the alphabet is represented by a number and then we can shift
	the message a certain number of letters 

	ex. if ABC is represented by 1, 2, 3 and we shift the message by 5 
	then the numbers are now 6, 7, 8 and we can turn those back into the letters of 
	the alphabet that corresponds to 6, 7, 8

	and our new letter is FGH
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,./1234567890"
alpha_len = len(alphabet) # keep track of the string for modulo

def encode(message, key):
	new_msg = ""

	for i in message:
		if i == " ":
			new_msg += " "
		else:
			new_letter_pos = (alphabet.index(i) + key) % alpha_len
			new_msg += alphabet[new_letter_pos]

	return new_msg

def decode(message, key):
	new_msg = ""

	for i in message:
		if i == " ":
			new_msg += " "
		else:
			new_letter_pos = (alphabet.index(i) - key) % alpha_len
			new_msg += alphabet[new_letter_pos]

	return new_msg


def main ():
	method = raw_input("Encode (e) or Decode (d): ")

	your_message = raw_input("What is your message: ")
	your_key = int(raw_input("What is your key: "))

	if method == 'e':
		encoded_msg = encode(your_message, your_key)
		print encoded_msg
	elif method == 'd':
		decoded_msg = decode(your_message, your_key)
		print decoded_msg
	else:
		print "Sorry I didn't catch that, use lowercase letters (e) or (d)."

if __name__ == '__main__':
	main()

"""
encoding and decoding ascii letter to/from bin, hex or oct

"""
def isbin(num):
    
	num = num.split()
	for i in range(len(num)):
		if set(num[i]) == set(['0', '1']):
			return True
		else:
			return False
def to_enc():

    text=input("Enter text to convert: ")
    prompt_encoding = input("Specify encoding (bin, hex or oct): ").lower()
    encoding = {'bin':bin, 'hex':hex, 'oct':oct}
    convert_to_num = [ord(alpha) for alpha in text]
    
    if prompt_encoding in encoding.keys():
        for to_enc in convert_to_num:
            print('0' + encoding[prompt_encoding](to_enc)[2:] 
            if prompt_encoding=='bin' else encoding[prompt_encoding](to_enc), end=' ')
    else:
        print('Encoding not supported')

def to_alpha():
    
    text=input("Enter enc to convert: ")
    encoding = ['bin', 'hex', 'oct']

    if not text.isalpha():
        convert_to_alpha = [chr(eval(num[0] + 'b' + num[1:] if isbin(num) else num)) for num in text.split()]
        for to_alpha in convert_to_alpha:
            print(to_alpha, end=' ')
    else:
        prin('Decoding not supported')

if __name__ == '__main__':
    
   print("""
            [1] Convert text to hex, bin or oct,
            [2] Convert hex, bin or oct to text""")
    
   select = input('\nSelect: ')
   if select == '1':
        to_enc()
   elif select == '2':
        to_alpha()
   else:
        print('Invalid')

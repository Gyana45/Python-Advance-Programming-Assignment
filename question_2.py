"""Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"

Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"
encrypt("burak") ➞ "k0r3baca"

"""

def encrypt():
    try:
        vowel={'a':0,'e':1,'i':2,'o':3,'u':4}
        s=str(input('Enter a string: '))
        #step-1
        reverse_s=s[::-1]
        #step-2
        new_s=''
        for i in reverse_s:
            if i.lower() in vowel:
                new_s+=str(vowel[i.lower()])
            else:
                new_s+=i
        #step-3        
        resulted_s=new_s+ 'aca'
        print('Final output: ',resulted_s)   
    except Exception as e:
        print('Error: ',e)
               
encrypt()
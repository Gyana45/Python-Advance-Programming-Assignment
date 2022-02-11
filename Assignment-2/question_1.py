'''
Write a function that takes a positive integer num and calculates how many
dots exist in a pentagonal shape around the center dot on the Nth iteration.
In the image below you can see the first iteration is only a single dot. On the
second, there are 6 dots. On the third, there are 16 dots, and on the fourth
there are 31 dots.

ex:pentagonal(3)=16
'''
#formala=(5n^2-5n+2)//2

def pentagonal():
    try:
        n=int(input('Enter the Centered pentagonal number:'))
        result=(5 * n * n - 5 * n + 2) // 2
        print( str(n) +'th Centered pentagonal number: ' + str(result))

    except Exception as e:
        print('Enter a valid integer')


pentagonal()
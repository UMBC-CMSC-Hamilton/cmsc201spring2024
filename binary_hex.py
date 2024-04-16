"""

Little different than most of our coding lectures

Three different number systems. Binary, Hexadecimal, Decimal
    Really Binary <-> Hex kind of the same thing
    Decimal is the weird one.
    
    How do we encode numbers inside of a computer?
        Memory cell can be either on or off.
        distinguish 3.3 V from 5 (on) V vs 1.67 vs 0 (off)
    bits are 0 or 1 they are modeled by the on/off state of a circuit
    we make everything out of bits.
    eight bits in a row = byte
    
    0011 0111 1 byte = 8 bits (normally put a space between each 4 bit nibble)
    0101 0001 0101 0010 1001 1010 (24 bits)
    
    In decimal we have numbers like this:
    
    decimal = base 10 system, every digit is one more power of 10
    
    472 = 4 * 100 + 7 * 10 + 2 * (10^0 = 1)
    3855 = 3 *10^3 + 8 * 10^2 + 5 * 10^1 + 5 * 10^0
    
    notice that in decimal how many digits do we have? 10 digits 0-9
    no such thing as a 10 digit, what is this really? 1 digit 0 digit
    
    
    all the same in binary except base = 2
    binary digit = bit
    how many bits are there? 0 , 1, no such thing as 2
    
    1001b = 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0
         = 8 + 1 = 9d
    
    1001 (ambiguous)
    
    
    0101b = 1 * 2^0 + 0 * 2^1 + 1 * 2^2 + 0 * 2^3
         = 1 + 4 + 0 = 5d
   128 64 32 16    8  4  2  1
    0  1  1  0     1  1  1  0
   64 + 32 + 8 + 4 + 2 = 110d
   
   1001 1101
   128 + 16 + 8 + 4 + 1 = 130 + 20 + 4 + 2 + 1 = 157
   2048  1024 512 256
   1     1    0    0   0111 1000
   
   2048 + 1024 + 64 + 32 + 16 + 8 = 3072 + 96 + 24 = 3192

    One last comment about binary.
        OS's are in 64 bits what does that mean?
        1 meaning is that the registers in the processor contain 64 bit numbers
        2nd meaning is the address width is 64 bits.
            that's the amount of ram that you can theoretically have
            tons of ram in 64 bits, probably we won't run out in our lifetimes
        
    0011 1100 0101 0011 0011 1100 0101 0011 0011 1100 0101 0011 0011 1100 0101 0011
    
    
    4 bits, 8 bits, 12 bits max
    we've done binary to decimal
    
    Let's talk about converting from decimal to binary
    
    73
    
    go until the number is 0
        if the number is odd we add a 1 to the left side of the number
        if the number is even we add a 0 to the left side of the number
        
        number //= 2
    73 is odd == > 36 even ==> 18 even ==> 9 (odd) ==> 4 (even) ==> 2 (even)
    ==> 1 (odd)
    0100 1001
    64 + 8 + 1 = 72 + 1 = 73 yep
    
    182 into binary
    182 even => 91 (odd) ==> 45 (odd) ==> 22 (even) ==> 11 (odd) ==> 5(odd)
    ==> 2 ==> 1
    1011 0110
    
    128 + 32 + 16 + 4 + 2 = 20 + 130 + 32 = 182 (correct)
    
    3273 (odd) ==> 1636 (even) ==> 818 (even) => 409 (odd) ==> 204 (even)
        ==> 102 (even) ==> 51 (odd) ==> 25 (odd) ==> 12 (even) ==> 6 (even)
        ==> 3 (odd) ==> 1(odd) ==> 0
    1100 1100 1001
    2048 + 1024 + 128 + 64 + 8 + 1
    3072 + 128 + 64 + 1 = 3072 + 192 + 9 = 3273
    
    477 to binary
    
    477 odd ==> 238 (even) ==> 119 (odd) ==> 59 (odd) ==> 29 (odd) ==>
        14 (even) ==> 7 ==> 3 ==> 1
    0001 1101 1101
    256 + 128 + 64 + 16 + 8 + 4 + 1
    
"""
# always stores in binary
x = 57  # even though we wrote this number in decimal the computer doesn't know that


"""

What the heck is hex?

    Aren't binary numbers long?
        yes
    Wouldn't it be nice if there was a better way to write them in a compact form?
        yes, also wow
    Hey I got something for you, it's hex.
    
    hexadecimal is base 16
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
    
        both dec/hex            dec     hex
    0000    0           1000    8       8
    0001    1           1001    9       9
    0010    2           1010    10      a A
    0011    3           1011    11      b B
    0100    4           1100    12      c C
    0101    5           1101    13      d D
    0110    6           1110    14      e E
    0111    7           1111    15      f F
    rule for adding in binary is 1 + 1 = 0 carry a 1
    1 + 0 = 0 + 1 = 1, 0 + 0 = 0
    
    0xfffff <- programmer is setting every bit to 1
    1111 1111 1111 1111 1111
    0xaf53b -> binary
    1010 1111 0101 0011 1011
    
    binary <--> hex
    
    1100 0110 0011 1010 0011 0000 1111
    0xc63a30f
    [the 0x are not really part of the number, they're a symbol that says
        I am hex]
        
    0xc64
    0xC64
    
    1100 0110 0100
    
    Hardest one... converting from hex <-> dec
    16's  1's
    a     4 convert that into decimal
    10 * 16 + 4 * 1 = 164
    
    256 16  1
    3   f   2 into decimal
    3 * 256 + 15 * 16 + 1 = 768 + 240 + 2 = 1010dec
    
    4096  256   16   1
    5     7     f    3
    5 * 4096 + 7 * 256 + 15 * 16 + 3 = 22515
    
    
    dec -> hex
"""

"""
Talk about hex again.
    bin     dec hex     bin     dec hex
    0000    0   0       1000    8   8
    0001    1   1       1001    9   9
    0010    2   2       1010    10  a/A
    0011    3   3       1011    11  b/B
    0100    4   4       1100    12  c/C
    0101    5   5       1101    13  d/D
    0110    6   6       1110    14  e/E
    0111    7   7       1111    15  f/F

Reminder in python if you want to enter a number in hex:

    0x[the number]
    ac12 = hex number and a legal variable name
    0xac12
    [not allowed to start a variable with a number]
    
    0x[hex]
    0b[0's and 1's]
    
    _1_object
    one_object

How do we convert from hex to decimal?

    Hard way (no easy way):
        0x3d4af
        15 + 10 * 16 + 4 * 16^2 + 13 * 16^3 + 3 * 16^4
        15 + 160 + 1024 + 13 * 4096 + 3 * 65536
        = 251,055
    0x9c (another way)
        1001 1100
        4 + 8 + 16 + 128 = 10 + 16 + 130 = 156
        9 * 16 + 12 = 144 + 12 = 156 yes

    decimal to hex:
        algorithm to convert from decimal into hex
        until number == 0
            mod by 16 ==> convert into a digit
            divide by 16
        
        You can always convert to binary and then use the table
        
        783 into hex
        783 into binary
        
        194 = 200 - 6
        96 = 100 - 4
        
        00783 (odd) => 391 (odd) => 195 (odd) => 97 => 48 (even)
            24 => 12 => 6 => 3 (odd) => 1 (odd)
        0011 0000 1111
        0x30f (yep it's 30f)
        
        783 % 16 on paper
            = 15 ==> f
        783 / 16 = 48
            48 % 16 = 0
            48 / 16 = 3
        last digit is 3
        0x30f
"""

def number_into_hex(the_num):
    hexits = {
        0: '0', 1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'a', 11: 'b',
        12: 'c', 13: 'd', 14: 'e', 15: 'f'
    }
    result = ''
    if the_num == 0:
        result = '0'
    
    while the_num != 0:
        current_digit = the_num % 16
        result = hexits[current_digit] + result
        # why don't we use += instead?
        the_num //= 16
    return '0x' + result


num = int(input('What number to convert? '))
while num != -1:
    print(number_into_hex(num), hex(num))
    num = int(input('What number to convert? '))


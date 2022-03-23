# python-password-generator
This is an advanced password generator in python.
--
It can:
Generate random password based on specified arguments.
Generate passwords from the specified characters.
Generate passwords from dictionaries.
And also with the help of arguments, you can set parameters such as the number of passwords, whether it will include characters, numbers, punctuation and how long it should.
---
Example

Generates 4 random passwords with a length of 12 letters, numbers, punctuation.

`python passgen.py 12 -l -n -p -rep 4`

Result:
```
\`QPn(Yf)\fG
@jPBDlTTP3bg
>bb+jtveT*o5
X/f\&A:@g#T8
```
Generates 4 random passwords with a length of 12 letters.

`python passgen.py 12 -l -rep 4`

Result:
```
lbhAMnViVGtw
qkZeBDjnYXnH
XGMnzhiZDejO
vXiqHktlFblK
```
Generates 4 random passwords from the specified characters of length 12.

`python passgen.py 12 -res qwertyuiop -rep 4`

Result:
```
qrewwwreuqep
reiryptiqutq
qqireperpyqq
rqowtptruquo
```
Generates 4 random passwords from a dictionary with a length of 2 elements. 
In this function, the length affects the number of elements taken from the dictionary.

`python passgen.py 2 -genBD Words.txt -rep 4`

Result:
```
pondroot
creampretty
drawgrand
worthurban
```

import re
# import regular expressions from python builtin
patterns = [r'^this is', 'oof']
#define what we are looking for
text = 'this is a simple test of regex'
for pattern in patterns:
    print('looking if "%s" in "%s" --->') % (pattern, text)
    if re.search(pattern,text):
        print('found a match!')
    else:
        print('no match')


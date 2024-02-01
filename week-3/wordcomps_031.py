#!/usr/bin/env python3

import sys
words = [word.strip() for word in sys.stdin]

len17 = [i for i in words if len(i) == 17]
print(f'Words containing 17 letters: {len17}')
len18pls = [i for i in words if len(i) >= 18]
print(f'Words containing 18+ letters: {len18pls}')
foura = [i for i in words if i.lower().count('a') == 4]
print(f"Words with 4 a's: {foura}")
twoplsqs = [i for i in words if i.lower().count('q') >= 2]
print(f"Words with 2+ q's: {twoplsqs}")
containcie = [i for i in words if 'cie' in i.lower()]
print(f'Words containing cie: {containcie}')
anag = [i for i in words if sorted(i.lower()) == sorted('angle') and i != "angle"]
print(f'Anagrams of angle: {anag}')
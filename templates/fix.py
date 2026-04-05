import os
import re

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r') as f:
            content = f.read()
        content = re.sub(r"' %} \"", '"', content)
        with open(filename, 'w') as f:
            f.write(content)
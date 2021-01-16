from tqdm import tqdm
import requests
import os
os.chdir('C:\\Users\\Mgcoder\\Desktop')
url = 'http://download1078.mediafire.com/1360a1m4o2rg/93pjtme3e2qey9x/www.goeagle.pk_W3+Resources_2021.rar'
res = requests.get(url, stream=True)
res.raise_for_status()

total_size = int(res.headers['content-length'])
with open('w3.rar', 'wb') as f:
    with tqdm(total=total_size, desc='W3School Download ', unit='B', unit_divisor=1024, unit_scale=True) as pbar:
        for chunk in res.iter_content(4096):
            f.write(chunk)
            pbar.update(len(chunk))
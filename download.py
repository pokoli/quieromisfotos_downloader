import os
import urllib
import urllib2
from argparse import ArgumentParser

from bs4 import BeautifulSoup


def download(url, output):
    soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")

    for row in soup.find_all('div', 'cuadro_evento'):
        for a in row.find_all('a'):
            onclick = a.get('onclick')
            if not onclick or not onclick.startswith('cargarFotoFiltros'):
                continue
            start_idx = len('cargarFotoFiltros(/')
            end_idx = onclick.index('&')
            photo_url = 'http://www.quieromisfotos.com/' + onclick[start_idx:end_idx]
            name = photo_url.split('/')[-1]
            print "Downloading %s" % photo_url
            urllib.urlretrieve(photo_url, os.path.join(output, name))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('url', help="Url where you want to download fotos")
    parser.add_argument('folder', help='Where to store the fotos')

    args = parser.parse_args()
    download(args.url, args.folder)

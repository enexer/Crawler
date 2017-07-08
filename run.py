from bs4 import BeautifulSoup
import re
import urllib.request


lista = []

def funkcja(url, url2, depth, cont):

    print("to", url, "from", url2, "depth", depth)

    if cont in url and url not in lista and depth<2:
        print("~~~~~~o", url, "!!from", url2, "!!!depth", depth)
        try:
            lista.append(url)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            soup = BeautifulSoup(response.read(), "html.parser")
            depth += 1
            for link in soup.findAll('a'):
                # print("X ",link.get('href'))
                z = link.get('href')
                if (z is None) or (len(z) < 10) or "pdf" in z or "jpg" in z or "photos" in z or "png" in z:
                    continue
                else:
                    # print("XXX: ", z)
                    if cont in z or "http" in z:
                        funkcja(z, url, depth, cont)
                    else:
                        funkcja(cont+z, url, depth, cont)

                    # if cont not in z and "http" not in z:
                    #     funkcja(cont + z, url, depth, cont)
                    # else:
                    #     funkcja(cont, url, depth, cont)


        except IOError:
            print ('cannot open')
    return

url = "http://www.ur.edu.pl/"
funkcja(url, "start", 0, url);

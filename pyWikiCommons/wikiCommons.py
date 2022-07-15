import requests
import argparse
import logging
import os, getpass
from urllib.parse import unquote
from props import *

log = logging.getLogger(__name__)

USER_AGENT_HEADER = {'User-Agent': 'pyWikiCommons/{} ({}; {})'.format(pyWikiCommons.__version__,
                                       'https://github.com/amckenna41/pyWikiCommons', getpass.getuser())}
BASE_URL = "https://commons.wikimedia.org/w/api.php?action=query"


def download_commons_image(filename, outputFolder="wikiCommonsOutput", 
  format='json', props=['imageinfo'], iiprops=["url"], decode=True):
    """
    
    """
    valid_props = []
    valid_iiprops = []

    for prop in props:
      if (prop not in ALL_PROPS):
        print('Input property not in available props {}').format(prop)
      else:
        valid_props.append(prop)
    
    #if >1 prop or iiprop then seperate by |
    for iiprop in iiprops:
      if (iiprop not in IMAGEINFO_IIPROPS):
        print('Input iiproperty not in available iiprops {}').format(iiprop)
      else:
        valid_iiprops.append(iiprop)
    
    if (format not in FORMAT):
      format = "json"
    
    request_url = BASE_URL + "&format=" + format + "&titles=" + filename + "&prop=" + valid_props + "&iiprop=" + valid_iiprops

    response = requests.get(request_url).json()

    file_url = response['query']['pages'].popitem()[1]['imageinfo'][0]['url']

    new_response = requests.get(file_url, stream=True, headers=USER_AGENT_HEADER)

    if not (os.path.isdir(outputFolder)):
        os.mkdir(outputFolder)
    
    #decode any unicode characters
    if (decode):
      filename = unquote(filename)

    #remove any leading or trailing whitespace
    filename = filename.strip()

    #remove the file string from filename
    if (filename[:5] == "File/"):
      filename = filename[5:]

    #create file
    file = open(os.path.join(outputFolder, filename), "wb")
    #write image to file
    file.write(new_response.content)
    #close file
    file.close()

    print(f'File ({filename}) successfully saved to {outputFolder}')

def get_commons_url(filename, format="json"):
  """
  
  """
  request_url = BASE_URL + "&format=" + format + "&titles=" + filename + "&prop=imageinfo&iiprop=url"

  response = requests.get(request_url).json()

  file_url = response['query']['pages'].popitem()[1]['imageinfo'][0]['url']

  return file_url
  
# if __name__ == '__main__':

#   parser = argparse.ArgumentParser(description='')

#   parser.add_argument('-filename', '--filename', type=str, required=False, default="", help='')
#   parser.add_argument('-output', '--output', type=str, required=False, default="", help='')

#   #parse input args
#   args = parser.parse_args()
#   filename = args.filename
#   outputFolder = args.output

#   download_commons_image(filename, outputFolder)

'''
https://commons.wikimedia.org/w/api.php?action=help&modules=query%2Bimageinfo
https://github.com/mwclient/mwclient/tree/master/mwclient
https://www.mediawiki.org/wiki/API:Imageinfo
https://github.com/wikimedia/mediawiki-api-demos/tree/master/python
https://en.wikipedia.org/wiki/Special:ApiSandbox#action=query&titles=Main%20page&format=json

# base_url2 = "https://en.wikipedia.org/w/api.php?action=query&format=json&titles=File:Flag_of_Torba_(Vanuatu)_Province.svg&prop=imageinfo&iiprop=url"

List of iiProps:

Values (separate with | or alternative)

'''
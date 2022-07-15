
"""
List of properties, actions and query parameters that can be used with the Wikimedia API:
https://commons.wikimedia.org/w/api.php 

"""
# https://www.mediawiki.org/wiki/API:Data_formats
FORMAT=[
    "json",
    "xml",
    "yaml"
]

ACTIONS=[
    "query"
]

ALL_PROPS=[ 
    "categories",
    "categoryinfo",
    "cirrusbuilddoc",
    "cirruscompsuggestbuilddoc",
    "cirrusdoc",
    "contributors",
    "coordinates",
    "deletedrevisions",
    "duplicatefiles",
    "entityterms",
    "extlinks",
    "extracts",
    "fileusage",
    "globalusage",
    "imageinfo",
    "imagelabels",
    "images",
    "info",
    "iwlinks",
    "langlinks",
    "links",
    "linkshere",
    "mmcontent",
    "pageimages",
    "pageprops",
    "pageterms",
    "pageviews",
    "redirects",
    "revisions",
    "stashimageinfo",
    "templates",
    "transcludedin",
    "transcodestatus",
    "videoinfo",
    "wbentityusage"
]

IMAGEINFO_IIPROPS=[
    "timestamp",
    "user",
    "userid",
    "comment",
    "parsedcomment",
    "canonicaltitle",
    "url",
    "size",
    "dimensions",
    "sha1",
    "mime",
    "thumbmime",
    "mediatype",
    "metadata",
    "commonmetadata",
    "extmetadata",
    "archivename",
    "bitdepth",
    "uploadwarning",
    "badfile"
]
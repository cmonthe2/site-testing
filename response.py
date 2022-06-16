import urllib.request
import urllib.error
import sys
import asyncio


def get_url_from_file(filename):
    """
    Description: Read file line by line and return the urls
    :param filename: the name of the file
    """
    urls = set()
    with open(filename, 'r') as file:
        for line in file:
            urls.add(line)  #todo add url validation regex
    return urls


def get_urls(url_args):
    """return a set of URLs"""
    if url_args is not None:
        urls = set()
        try:
            for i in url_args:
                urls.add(i)
            return urls
        except ValueError:
            print("Unexpected argument error")
    else:
        print("Please specify at least one url")
        sys.exit(3)


async def check_response(url, ssl_context):
    """Check the response of url and returns exception type if error"""
    try:
        response_code = urllib.request.urlopen(url, context=ssl_context).getcode()
    except urllib.error.URLError as e:
        response_code = 404
    if response_code == 200:
        status = "active"
    else:
        status = "inactive"
    print("{}  {}".format(url, status))

import urllib.request
import urllib.error
def read_file(filename,ssl_context):
    '''Read file line by line and calls the function to check response'''
    with open(filename , 'r') as file:
        for line in file:
            check_response(line,ssl_context)

def check_response(url,ssl_context):
    '''Check the response of url and returns exception type if error'''
    try:
        response_code=urllib.request.urlopen(url,context=ssl_context).getcode()
    except urllib.error.URLError as e:
        response_code=404
    if response_code==200:
        status="active"
    else:
        status="inactive"
    print("{}  {}".format(url,status))

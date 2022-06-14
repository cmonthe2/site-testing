import argparse
import ssl
from response import read_file
from response import check_response
parser = argparse.ArgumentParser()
parser.add_argument("--infile", "-f", type=str, required=False)
parser.add_argument("--url", "-u" , type=str,required=False)
args = parser.parse_args()
filename=args.infile
url=args.url
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False             # python3.6+ don't work with ssl certifcates without any library so making ssl_cert as none.
ssl_context.verify_mode = ssl.CERT_NONE
if(url and filename):
    check_response(url,ssl_context)
    read_file(filename,ssl_context)
elif(url):
    check_response(url,ssl_context)
elif(filename):
    read_file(filename,ssl_context)
else:
    print("You haven't passed url or file")

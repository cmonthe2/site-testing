import argparse
import ssl
import asyncio
import time
from utility import get_url_from_file, check_response, get_urls, check_response_sync
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def parse_args():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--infile", "-f", type=str, required=False)
        parser.add_argument("--url", "-u", nargs='*', required=False)
        parser.add_argument("--asyncc", "-a", action='store_true')
    except Exception as e:
        print(e)
    return parser.parse_args()


def async_execute(urls, ssl_context):
    # creating tasks for asynchronous execution
    tasks = []
    for url in urls:
        tasks.append(asyncio.Task(check_response(url, ssl_context)))
    yield from asyncio.gather(*tasks)


def main():
    try:
        args = parse_args()
    except Exception as e:
        print(e)
    try:
        filename = args.infile
        url_args = args.url
    except Exception as e:
        print(e)
    ssl_context = ssl.create_default_context()
    # python3.6+ don't work with ssl certifcates without any library so making ssl_cert as none.
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    urls = []
    if url_args and filename:
        urls = get_urls(url_args) + get_url_from_file(filename)
    elif url_args:
        urls = get_urls(url_args)
    elif filename:
        urls = get_url_from_file(filename)
    else:
        print("You haven't passed url or file")

    if args.asyncc:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(async_execute(urls, ssl_context))
    else:
        for url in urls:
            check_response_sync(url, ssl_context)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Time taken(in second): ", end - start)

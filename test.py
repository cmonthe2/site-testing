import argparse
import ssl
import asyncio
from response import get_url_from_file, check_response, get_urls


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", "-f", type=str, required=False)
    parser.add_argument("--url", "-u", nargs='*', required=False)
    return parser.parse_args()


def main():
    args = parse_args()
    filename = args.infile
    url_args = args.url
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

    # creating tasks for asynchronous execution
    tasks = []
    for url in urls:
        tasks.append(asyncio.Task(check_response(url, ssl_context)))
    yield from asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
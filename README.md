# # Web Connectivity Tester

This module is created to check the response of any website.In this you can provide the 
individual url or file containing multiple urls(one in each line) and it will return the 
http response code.

## How to use?

Use the package in following manner:

```bash
python3 main.py --url https://abc.xyz
```
OR
```bash
python3 main.py -u https://abc.xyz
```
OR
```bash
python3 main.py --infile /user/url.txt 
```
## Output                                                     
   https://abc.com  active , Where active or inactive are  the response for https://abc.com
   
   
 # Python Async Examples

# Quickstart

```bash
git clone https://github.com/PatrickAlphaC/async-python
cd async-python
pip install -r requirements.txt
```
Get a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and set it as an [environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). If you're unfamiliar with environment variables, set it in your `.env` file.

```bash
export ALPHAVANTAGE_API_KEY='YOUR KEY HERE'
```

The free Alpha Vantage API key is rate limited to 5 API calls/minute. If you'd like to speed test APIs, you can swap it out for a different API, like [this json dummy api.](https://jsonplaceholder.typicode.com/)

Then run:
```
python av_requests.py
```
And you'll get an output like:
```
Timer started...
It took 1.1849939823150635 seconds to make 5 API calls
```

To run it async, run:
```
python av_async_run.py 
```
and you'll get an output like:
```
Timer started...
Time to make 5 API calls with tasks, it took: 0.400589227676391

# Web Connectivity Tester

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
For multiple files
```bash
python3 main.py -u https://abc.xyz https://xyz.com
```
Use the asyncc flag for asynchronous processing. We use 2Cs to avoid conflict with the async keyword in python
```bash
python3 main.py -u https://abc.xyz https://xyz.com --asyncc
```
## Output                                                     
   https://abc.com  200, Where 200 is the response for https://abc.com

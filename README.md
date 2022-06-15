# # Web Connectivity Tester

This module is created to check the response of any website.In this you can provide the 
individual url or file containing multiple urls(one in each line) and it will return the 
http response code.

## How to use?

git clone repo
cd site-testing
pip install -r requirements.txt

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

 python3 main.py --infile filename 
```
## Output                                                     
   https://abc.com  active , Where active or inactive are  the response for https://abc.com

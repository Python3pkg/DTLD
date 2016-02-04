# DTLD
Custom Top Level domain extractor

This is an example of a top level domain : wxyz.com or qbcd.net

How it works
DTLD extracts the root domain. It works by extracting from http|https|www protocol URLS

Example Code:

 from DTLD.dtld.main import TopLevelDomain as tld
 
 url = 'http://github.com'
 
 App = tld.TopLevelDomain(url)
 
 domain = App.get_top_level_domain()
 
 print(domain)
 
 >>github.com
 
 

 
 
 

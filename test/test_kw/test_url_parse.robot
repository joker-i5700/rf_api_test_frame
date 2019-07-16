*** Setting ***    
Library    TestLibrary

*** Variable ***
${HOST}    http://127.0.0.1:5000
${URL}    http://127.0.0.1:5000/tools.test.com/AutoTest/ABCD.12345.FILE?start=500&aa=222&end=150000&read=100&cdf=we2&skip=200&type=readskip
@{PATH}   127.0.0.1:5000    tools.test.com    AutoTest    ABCD.12345.FILE
&{PARAM}   action=DemoAction    version=2.0    timestamp=2019-01-01T15:34:00

*** Test Cases ***
test_kw_generate_url
    ${ret}    kw generate url    @{PATH}     &{PARAM}
    Should Be Equal As Strings    ${ret}    127.0.0.1:5000/tools.test.com/AutoTest/ABCD.12345.FILE?action=DemoAction&version=2.0&timestamp=2019-01-01T15:34:00
    
test_kw_parse_url
    ${ret}    kw parse url    ${URL}
    Should Be Equal As Strings    ${ret}[0]    {'hostname': '127.0.0.1', 'netloc': '127.0.0.1:5000', 'path': '/tools.test.com/AutoTest/ABCD.12345.FILE', 'port': 5000, 'queryParams': {'start': '500', 'aa': '222', 'end': '150000', 'read': '100', 'cdf': 'we2', 'skip': '200', 'type': 'readskip'}, 'scheme': 'http'}
    
test_kw_parse_urls
    @{urls}    Create List    
    ...    http://127.0.0.1:5000/tools.test.com/AutoTest?action=DemoAction&version=2.0
    ...    http://127.0.0.1:5001/tools.test.com/AutoTest?action=DemoAction&version=3.0
    ...    http://127.0.0.1:5002/tools.test.com/AutoTest?action=DemoAction&version=5.0
    ${ret}    kw parse url    @{urls}
    Should Be Equal As Strings    ${ret}[0]    {'hostname': '127.0.0.1', 'netloc': '127.0.0.1:5000', 'path': '/tools.test.com/AutoTest', 'port': 5000, 'queryParams': {'action': 'DemoAction', 'version': '2.0'}, 'scheme': 'http'}
    Should Be Equal As Strings    ${ret}[1]    {'hostname': '127.0.0.1', 'netloc': '127.0.0.1:5001', 'path': '/tools.test.com/AutoTest', 'port': 5001, 'queryParams': {'action': 'DemoAction', 'version': '3.0'}, 'scheme': 'http'}
    Should Be Equal As Strings    ${ret}[2]    {'hostname': '127.0.0.1', 'netloc': '127.0.0.1:5002', 'path': '/tools.test.com/AutoTest', 'port': 5002, 'queryParams': {'action': 'DemoAction', 'version': '5.0'}, 'scheme': 'http'}
   
test_kw_get_path_by_replace_host_port
    ${ret}    kw get path by replace host port    ${URL}    127.1.1.1:9999
    Should Be Equal As Strings    ${ret}    http://127.1.1.1:9999/tools.test.com/AutoTest/ABCD.12345.FILE?start=500&aa=222&end=150000&read=100&cdf=we2&skip=200&type=readskip

test_kw_get_path_by_replace_query_params
    ${queryParams}    Evaluate    {"start": 600, "aa": 333, "type": "noskip"}    
    ${ret}    kw get path by replace query params    ${URL}    ${queryParams}
    Should Be Equal As Strings    ${ret}    http://127.0.0.1:5000/tools.test.com/AutoTest/ABCD.12345.FILE?start=600&aa=333&end=150000&read=100&cdf=we2&skip=200&type=noskip
  
    
test_kw_get_host_port_with_prefix
    ${ret}    kw get host port with prefix    ${URL}
    Should Be Equal As Strings    ${ret}    http://127.0.0.1:5000  
        

    

    




	    
    
    
    
    
    
    
    
    
    
    
    
    
    
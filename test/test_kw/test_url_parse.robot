*** Setting ***    
Library    TestLibrary

*** Variable ***
${host}    http://127.0.0.1:5000
@{path}   127.0.0.1:5000    tools.test.com    AutoTest    ABCD.12345.FILE
&{param}   action=DemoAction    version=2.0    timestamp=2019-01-01T15:34:00

*** Test Cases ***
test_kw_generate_url
    ${ret}    kw generate url    @{path}     &{param}
    Log    ${ret}
    
test_kw_test
    kw test
    

    



	    
    
    
    
    
    
    
    
    
    
    
    
    
    
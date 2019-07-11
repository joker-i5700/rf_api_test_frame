*** Setting ***    
Library    TestLibrary

*** Variable ***
${host}    http://127.0.0.1:5000


*** Test Cases ***
test_kw_aes_cbc_encrypt
    Set Suite Variable    ${t_sourceKey}    e677cc9c0c695aeaa01732a32170040b
    Set Suite Variable    ${t_iv}    e677cc9c0c695aeaa01732a32170040b
    Set Suite Variable    ${t_data}    {'appid': '123', 'appName': 'com.jet.sdk', 'deviceid': 'hijkl89012'}
    ${ret}    kw aes cbc encrypt    ${t_sourceKey}    ${t_iv}    ${t_data}
    Log    ${ret}
    Should Be Equal As Strings    ${ret}    8d7g0vWz8qKz/55fffCuei7Jq/0oInXVcpahJFUI6KSxiFuEsvpLEpwJTnT+aDfnAf0TO1IS1RJZTLEjbDDHKZd4a+XDtChrTCkoA4kOfEI=
    Set Suite Variable    ${t_endata}    ${ret}
    
test_set_suite_variable
    ${sourceKey}    Get Variable Value    ${t_sourceKey}
    ${iv}    Get Variable Value    ${t_iv}
    ${data}    Get Variable Value        ${t_endata}
    ${data_exp}    Get Variable Value    ${t_data}
    Should Be Equal As Strings    ${sourceKey}    e677cc9c0c695aeaa01732a32170040b
    Should Be Equal As Strings    ${iv}    e677cc9c0c695aeaa01732a32170040b
    Should Be Equal As Strings    ${data}    8d7g0vWz8qKz/55fffCuei7Jq/0oInXVcpahJFUI6KSxiFuEsvpLEpwJTnT+aDfnAf0TO1IS1RJZTLEjbDDHKZd4a+XDtChrTCkoA4kOfEI=
    Should Be Equal As Strings    ${data_exp}    {'appid': '123', 'appName': 'com.jet.sdk', 'deviceid': 'hijkl89012'}
    
test_get_variables_variable
    ${getvar}    Get Variables
    Log    ${getvar}
    Should Be Equal As Strings    ${getvar}[\$\{t_sourceKey\}]    e677cc9c0c695aeaa01732a32170040b
    Should Be Equal As Strings    ${getvar}[\$\{t_iv\}]    e677cc9c0c695aeaa01732a32170040b
    Should Be Equal As Strings    ${getvar}[\$\{t_endata\}]    8d7g0vWz8qKz/55fffCuei7Jq/0oInXVcpahJFUI6KSxiFuEsvpLEpwJTnT+aDfnAf0TO1IS1RJZTLEjbDDHKZd4a+XDtChrTCkoA4kOfEI=
    Should Be Equal As Strings    ${getvar}[\$\{t_data\}]    {'appid': '123', 'appName': 'com.jet.sdk', 'deviceid': 'hijkl89012'}
    
test_kw_aes_cbc_decrypt
    ${sourceKey}    Get Variable Value    ${t_sourceKey}
    ${iv}    Get Variable Value    ${t_iv}
    ${data}    Get Variable Value        ${t_endata}
    ${data_exp}    Get Variable Value    ${t_data}
    ${ret}    kw aes cbc decrypt    ${sourceKey}    ${iv}    ${data}
    Log    ${ret}  
    Should Be Equal As Strings    ${ret}    ${data_exp}



	    
    
    
    
    
    
    
    
    
    
    
    
    
    
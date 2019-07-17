*** Setting ***    
Library    TestLibrary

Suite Setup    kw_init
*** Variable ***
${HOST}    http://127.0.0.1:5000


*** Test Cases ***
test_kw_get_values_by_keys_list_f_0
    ${data}    Get Variable Value    ${m_dict_data}
    ${keys}    Evaluate    ["list", 2, 0, "f"]
    Log    ${data}
    ${ret}    kw get values by keys    ${data}     ${keys}
    Should Be Equal As Strings    ${ret}    [1]
    
test_kw_get_values_by_keys_list_f_*
    ${data}    Get Variable Value    ${m_dict_data}
    ${keys}    Evaluate    ["list", 2, "*", "f"]
    Log    ${data}
    ${ret}    kw get values by keys    ${data}     ${keys}
    Should Be Equal As Strings    ${ret}    [1, 2, 3, 4]
    
test_kw_get_values_by_keys_list_c_*
    ${data}    Get Variable Value    ${m_dict_data}
    ${keys}    Evaluate    ["list", 2, "*", "c"]
    Log    ${data}
    ${ret}    kw get values by keys    ${data}     ${keys}
    Should Be Equal As Strings    ${ret}    [2, 2, 2, 2]
    
test_kw_get_values_by_keys_list_a
    ${data}    Get Variable Value    ${m_dict_data}
    ${keys}    Evaluate    ["list", 0,"a"]
    Log    ${data}
    ${ret}    kw get values by keys    ${data}     ${keys}
    Should Be Equal As Strings    ${ret}    ['abc']
    
test_kw_get_values_by_keys_list_d
    ${data}    Get Variable Value    ${m_dict_data}
    ${keys}    Evaluate    ["list", 1,"d"]
    Log    ${data}
    ${ret}    kw get values by keys    ${data}     ${keys}
    Should Be Equal As Strings    ${ret}    [33]
    
test_kw_get_values_by_keys_a
    ${data}    Get Variable Value    ${m_dict_data}
    ${keys}    Evaluate    ["a"]
    Log    ${data}
    ${ret}    kw get values by keys    ${data}     ${keys}
    Should Be Equal As Strings    ${ret}    [11]
    
test_kw_get_values_by_key_f
    ${data}    Get Variable Value    ${m_dict_data}
    ${key}    Evaluate    'f'
    Log    ${data}
    ${ret}    kw get values by key    ${data}     ${key}
    Should Be Equal As Strings    ${ret}    [1, 2, 3, 4]
    
*** Keywords ***
kw_init
    ${m_dict_data}    Evaluate    {'a': 11, 'list': [{'a': 'abc'}, {'c': 22, 'd': 33}, [{'f': 1, 'c': 2}, {'f': 2, 'c': 2}, {'f': 3, 'c': 2}, {'f': 4, 'c': 2} ]]}
    Set Suite Variable    ${m_dict_data}
        

    

    




	    
    
    
    
    
    
    
    
    
    
    
    
    
    
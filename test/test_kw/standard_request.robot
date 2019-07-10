*** Setting ***    
Library    TestLibrary
*** Variable ***
${host}    http://127.0.0.1:8080
${query_sql}    select * from tb_topic
${db_host}    127.0.0.1
${db_name}    db_demo
${db_username}    db_user
${db_password}    db_pwd

*** Test Cases ***
demo_case_Config
    kw Config Add Item    public    author    jet
    ${result}    kw Config Get Value    public    author
    Log    ${result}
demo_case_dict
    ${strdic}    Set Variable    {1: 'a', 2: 3, 3: 'test', 4: 100}
    ${rstrdic}    Set Variable    {1:'b',2: 5}    
    ${ret}    kw dict update parse    ${strDic}    ${rstrdic}
    log    ${ret}

	    
    
    
    
    
    
    
    
    
    
    
    
    
    
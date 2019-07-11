*** Setting ***    
Library    TestLibrary
Library    RequestsLibrary

*** Variable ***
${host}    http://127.0.0.1:5000
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
    
test_kw_body_parse
    ${resp}    kw_http_get_request    ${host}    /todos
    ${value}    kw body parse    ${resp.content}    todo1
    Log    ${value}
    Should Be Equal As Strings    ${resp.status_code}    200
    Should Be Equal As Strings    ${value}    {'task': 'build an API'}
    
test_kw_body_parse_ex
    ${resp}    kw_http_get_request    ${host}    /todos
    ${value}    kw body parse ex    ${resp.content}    task
    Log    ${value}
    Should Be Equal As Strings    ${resp.status_code}    200
    Should Be Equal As Strings    ${value}    ['build an API', '?????', 'profit!']
    
test_kw_dict_update_parse
    ${strdic}    Set Variable    {1: 'a', 2: 3, 3: 'test', 4: 100}
    ${rstrdic}    Set Variable    {1:'b',2: 5}    
    ${ret}    kw dict update parse    ${strDic}    ${rstrdic}
    log    ${ret}
    Should Be Equal As Strings    ${ret}    {1: "b", 2: 5, 3: "test", 4: 100}
    
test_kw_boundary_generate
    ${dc}    Evaluate    {"sessionType":0,"clientSecret":100,"appid":100,"appName":"WEB-i.xxx.com"}
    ${st}=    Set Variable    ------WebKitFormBoundary5rFTEqcX0liWDgE8
    ${ret}    kw boundary generate    ${dc}    ${st}
    Log    ${ret}
    Should Contain    ${ret}    WEB-i.xxx.com  

test_kw_cover_get_Parameters    
    ${s}    Set Variable    appid=11&Version=10&appName=com.xxx.sdk&clientVersion=v1.0.0&deviceid=abcdefg1234567
    ${d}    Evaluate    {'appid': '123', 'appName': 'com.jet.sdk', 'deviceid': 'hijkl89012'}
    ${ret}    kw cover get Parameters    ${s}    ${d}
    Log    ${ret}
    Should Be Equal As Strings    ${ret}    appid=123&Version=10&appName=com.jet.sdk&clientVersion=v1.0.0&deviceid=hijkl89012

    
*** Keywords ***
kw_http_get_request
    [Arguments]    ${host}    ${url}
    [Documentation]   
    ...    【功能】发送HTTP GET请求
    ...
    ...    【参数】
    ...    host: 服务器主机地址
    ...    url：请求地址
    ...
    ...    【返回值】
    ...    Ret: response对象
    ${headers}    Create Dictionary    User-Agent=RobotFramework RequestsLibrary  Host=127.0.0.1
    Create Session    api    ${host}    ${headers}
    ${Ret}    Get Request   api   ${url}
    [Return]    ${Ret}
    
    
kw_http_post_request
    [Arguments]    ${host}    ${url}    ${data}
    [Documentation]   
    ...    【功能】发送HTTP POST请求
    ...
    ...    【参数】
    ...    host: 服务器主机地址
    ...    url：请求地址
    ...    data: 请求参数
    ...
    ...    【返回值】
    ...    Ret: response对象
    ${headers}    Create Dictionary    User-Agent=RobotFramework RequestsLibrary  Host=127.0.0.1
    Create Session    api    ${host}    ${headers}
    ${Ret}    Post Request   api   ${url}?${data}
    [Return]    ${Ret}


	    
    
    
    
    
    
    
    
    
    
    
    
    
    
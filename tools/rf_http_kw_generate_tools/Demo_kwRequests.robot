*** Settings ***
Library           TestLibrary
Library           RequestsLibrary

*** Keywords ***
Demo_http_api_del_todos_task
    [Arguments]    ${url}    ${data}
    [Documentation]   【功能】测试flask server demo的put接口
    ...
    ...    【参数】
    ...    无
    ...
    ...    【返回值】
    ...    Ret: response对象
    ${headers}    Create Dictionary    User-Agent=RobotFramework RequestsLibrary  Host=127.0.0.1
    Create Session    api    ${url}    ${headers}   verify=${False}
    ${Ret}    Delete Request   api   /todos/9    data=${data}
    [Return]    ${Ret}

Demo_http_api_get_todos
    [Arguments]    ${url}    ${data}
    [Documentation]   【功能】测试flask server demo的todos接口
    ...
    ...    【参数】
    ...    无
    ...
    ...    【返回值】
    ...    Ret: response对象
    ${headers}    Create Dictionary    User-Agent=RobotFramework RequestsLibrary  Host=127.0.0.1
    Create Session    api    ${url}    ${headers}   verify=${False}
    ${Ret}    Get Request   api   /todos${data}
    [Return]    ${Ret}

Demo_http_api_get_todos_task
    [Arguments]    ${url}    ${data}
    [Documentation]   【功能】测试flask server demo的put接口
    ...
    ...    【参数】
    ...    无
    ...
    ...    【返回值】
    ...    Ret: response对象
    ${headers}    Create Dictionary    User-Agent=RobotFramework RequestsLibrary  Host=127.0.0.1
    Create Session    api    ${url}    ${headers}   verify=${False}
    ${Ret}    Get Request   api   /todos/9${data}
    [Return]    ${Ret}

Demo_http_api_post_tasks
    [Arguments]    ${url}    ${data}
    [Documentation]   【功能】测试flask server demo的tasks接口
    ...
    ...    【参数】
    ...    无
    ...
    ...    【返回值】
    ...    Ret: response对象
    ${headers}    Create Dictionary    Content-Type=application/json  User-Agent=RobotFramework RequestsLibrary  Host=127.0.0.1
    Create Session    api    ${url}    ${headers}   verify=${False}
    ${Ret}    Post Request   api   /tasks    data=${data}
    [Return]    ${Ret}

Demo_http_api_put_todos_task
    [Arguments]    ${url}    ${data}
    [Documentation]   【功能】测试flask server demo的put接口
    ...
    ...    【参数】
    ...    无
    ...
    ...    【返回值】
    ...    Ret: response对象
    ${headers}    Create Dictionary    User-Agent=RobotFramework RequestsLibrary  Host=127.0.0.1
    Create Session    api    ${url}    ${headers}   verify=${False}
    ${Ret}    Put Request   api   /todos/9${data}
    [Return]    ${Ret}


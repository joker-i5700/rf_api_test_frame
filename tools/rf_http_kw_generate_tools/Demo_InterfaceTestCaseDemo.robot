*** Settings ***
Suite Setup       Log    Suite Setup
Suite Teardown    Log    Suite Teardown
Test Setup        log    Test Setup
Test Teardown     log    Teardown
Resource          Demo_kwRequests.robot
Resource          Demo_kwExcel.robot

*** Variables ***
${IP_PORT}     http://127.0.0.1:5000

*** Test Cases ***
http_api_del_todos_task.Case01
    [Tags]    
    ${data}    ${exp}    Demo_Get_http_api_del_todos_task_Parameters    Case01
    ${Resp_data}    Demo_http_api_del_todos_task    ${IP_PORT}    ${data}
    Log    ${Resp_data.text}
    Should Be Equal As Strings    ${Resp_data.status_code}    200
    Should Be Equal    ${Resp_data.text}    ${exp}

http_api_get_todos.Case01
    [Tags]    
    ${data}    ${exp}    Demo_Get_http_api_get_todos_Parameters    Case01
    ${Resp_data}    Demo_http_api_get_todos    ${IP_PORT}    ${data}
    Log    ${Resp_data.text}
    Should Be Equal As Strings    ${Resp_data.status_code}    200
    Should Be Equal    ${Resp_data.text}    ${exp}

http_api_get_todos_task.Case01
    [Tags]    
    ${data}    ${exp}    Demo_Get_http_api_get_todos_task_Parameters    Case01
    ${Resp_data}    Demo_http_api_get_todos_task    ${IP_PORT}    ${data}
    Log    ${Resp_data.text}
    Should Be Equal As Strings    ${Resp_data.status_code}    200
    Should Be Equal    ${Resp_data.text}    ${exp}

http_api_post_tasks.Case01
    [Tags]    
    ${data}    ${exp}    Demo_Get_http_api_post_tasks_Parameters    Case01
    ${Resp_data}    Demo_http_api_post_tasks    ${IP_PORT}    ${data}
    Log    ${Resp_data.text}
    Should Be Equal As Strings    ${Resp_data.status_code}    200
    Should Be Equal    ${Resp_data.text}    ${exp}

http_api_put_todos_task.Case01
    [Tags]    
    ${data}    ${exp}    Demo_Get_http_api_put_todos_task_Parameters    Case01
    ${Resp_data}    Demo_http_api_put_todos_task    ${IP_PORT}    ${data}
    Log    ${Resp_data.text}
    Should Be Equal As Strings    ${Resp_data.status_code}    200
    Should Be Equal    ${Resp_data.text}    ${exp}


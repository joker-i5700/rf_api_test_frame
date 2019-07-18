*** Settings ***
Library           TestLibrary

*** Keywords ***
Demo_Get_http_api_del_todos_task_Parameters
    [Arguments]    ${CaseNo}
    kw Open Excel    ${CURDIR}${/}Demo_TestCase${/}http_api_del_todos_task.xls
    ${data}    kw Read Cell Data By Name    ${CaseNo}    B2
    ${ExpValue}    kw Read Cell Data By Name    ${CaseNo}    F2
    [Return]    ${data}    ${ExpValue}

Demo_Get_http_api_get_todos_Parameters
    [Arguments]    ${CaseNo}
    kw Open Excel    ${CURDIR}${/}Demo_TestCase${/}http_api_get_todos.xls
    ${data}    kw Read Cell Data By Name    ${CaseNo}    B2
    ${ExpValue}    kw Read Cell Data By Name    ${CaseNo}    F2
    [Return]    ${data}    ${ExpValue}

Demo_Get_http_api_get_todos_task_Parameters
    [Arguments]    ${CaseNo}
    kw Open Excel    ${CURDIR}${/}Demo_TestCase${/}http_api_get_todos_task.xls
    ${data}    kw Read Cell Data By Name    ${CaseNo}    B2
    ${ExpValue}    kw Read Cell Data By Name    ${CaseNo}    F2
    [Return]    ${data}    ${ExpValue}

Demo_Get_http_api_post_tasks_Parameters
    [Arguments]    ${CaseNo}
    kw Open Excel    ${CURDIR}${/}Demo_TestCase${/}http_api_post_tasks.xls
    ${data}    kw Read Cell Data By Name    ${CaseNo}    B2
    ${ExpValue}    kw Read Cell Data By Name    ${CaseNo}    F2
    [Return]    ${data}    ${ExpValue}

Demo_Get_http_api_put_todos_task_Parameters
    [Arguments]    ${CaseNo}
    kw Open Excel    ${CURDIR}${/}Demo_TestCase${/}http_api_put_todos_task.xls
    ${data}    kw Read Cell Data By Name    ${CaseNo}    B2
    ${ExpValue}    kw Read Cell Data By Name    ${CaseNo}    F2
    [Return]    ${data}    ${ExpValue}


*** Setting ***
Library    TestLibrary

Suite Setup    init_kw_demo    999999
*** Variable ***
${host}    http://127.0.0.1:8080

*** Keywords ***
init_kw_demo
    [Arguments]    ${demo_id}
    Log    ${demo_id}
    kw config add item    XL_DP    CIRCLE_ID    ${demo_id}
    [Return]    ${demo_id}
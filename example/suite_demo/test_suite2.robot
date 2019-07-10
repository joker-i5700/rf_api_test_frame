*** Setting ***
Library    TestLibrary

*** Test Cases ***
XL_test
    ${var}    kw config get value    XL_DP    CIRCLE_ID
    Log    ${var}
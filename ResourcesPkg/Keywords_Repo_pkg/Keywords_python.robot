*** Settings ***
Library  ../Pages_pkg/Page1.py  Chrome

*** Keywords ***
Open website1
    [Arguments]     ${URL}
    call page1 open        https://www.google.com
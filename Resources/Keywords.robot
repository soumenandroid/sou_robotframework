*** Settings ***
Library     Selenium2Library
Library    OperatingSystem
Library    ../Tests/CustomLibrary.py
Resource    ../Resources/config_param.robot


*** Keywords ***
Open website
    [Arguments]     ${APP1_URL}  ${BROWSER}
    Get Web Driver  ${APP1_URL}    ${BROWSER}
    Maximize Browser Window

Open website custom
    Create Webdriver    ${BROWSER}       executable_path=${driverpath}
    [Arguments]     ${APP1_URL}  ${BROWSER}
    ${driver}=  Get Webdriver Instance
    Go To    ${APP1_URL}

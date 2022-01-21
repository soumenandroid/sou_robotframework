*** Settings ***
Library     Selenium2Library
Library    OperatingSystem

*** Variables ***
${searchtext}   "makemyterip"

*** Test Cases ***
Makemy trip flight search
    Open website    ${URL}    ${BROWSER}
    Search For Hotels
    Wait Until Element Is Visible    //span[contains(@class,'chHotels')]
    Wait Until Element Is Visible    //a[contains(@class,'widgetSearchBtn')]
    Click Button    //a[contains(@class,'widgetSearchBtn')]
    Click Button    //span[contains(@class,'chHotels')]
    Wait Until Element Is Visible  ${txt_fromcity}
    Input Text      ${txt_fromcity}   CCU


*** Test Cases ***
Google search
    Open website    https://www.google.com  ${BROWSER}
    Input Text      //input[@name='q']      makemytrip
*** Settings ***
Library     Selenium2Library
Resource    ../ResourcesPkg/config_param.robot
Resource    ../ResourcesPkg/Keywords_Repo_pkg/Keywords.robot

*** Test Cases ***
foo
      Open website custom  ${APP1_URL}   ${BROWSER}
      Input Text      //input[@name='q']      makemytrip

*** Test Cases ***
foo1
    Open website custom    $APP1_URL    $BROWSER
    Input Text    //input[@name='q']      goidibo

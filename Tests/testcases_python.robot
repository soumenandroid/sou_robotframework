*** Settings ***
Resource    ../Resources/Keywords_Repo/Keywords_python.robot
#Suite Setup     Open
#Suite Teardown  Close

*** Test Cases ***
Open weather API UI testing
    Open website1  "https://openweathermap.org/api"

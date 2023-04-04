#Test RobotFramework
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://thetestingworld.com/testings/
${Browser}    Chrome

*** Test Cases ***
First Test Case
    open browser    ${URL}   ${Browser}
    maximize browser window
    select radio button    add_type    office
    select checkbox    name:terms
    click link    xpath://*[@id="tab-content1"]/form/div/em/a
    click button    name:close
    sleep    10
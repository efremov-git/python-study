# First Test RobotFramework
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.saucedemo.com/
${Browser}    Chrome

*** Test Cases ***
First Test Case
    open browser    ${URL}   ${Browser}
    maximize browser window
    input text    name:user-name    standard_user
    input password    xpath:/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input    secret_sauce
    click button    name:login-button
    sleep    5
    go back
    sleep    3
    close browser

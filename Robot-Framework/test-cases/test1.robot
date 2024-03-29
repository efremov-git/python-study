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
    sleep    5
    sleep    5
    input password    xpath:/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input    secret_sauce
    clear element text    name:user-name
    click button    name:login-button
    sleep    5
    close browser

# Test RobotFramework
*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/resources.robot

*** Variables ***
${URL}    https://www.saucedemo.com/
${Browser}    Chrome

*** Test Cases ***
Test Case
    Open Browser and Maximize Browser Window    ${URL}    ${Browser}
    input text    name:user-name    standard_user
    input password    xpath:/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input    secret_sauce
    click button    name:login-button
    sleep    5
    go back
    sleep    3
    close browser
# Test RobotFramework
*** Settings ***
Library    SeleniumLibrary
Resource    ../resources/resources.robot
#migration in resources

*** Variables ***
${URL}    https://www.saucedemo.com/
${Browser}    Chrome


# Users
${StandardUser}    standard_user
${LockedOutUser}    locked_out_user

${Password}    secret_sauce

*** Test Cases ***
Test Case
    Open Browser and Maximize Browser Window    ${URL}    ${Browser}
    Login To Website    ${StandardUser}    ${Password}
    ${Title}=    get title
    log    Page title is:${Title}
    ${Cookies}=    get cookie
    log    ${Cookies}
    close browser
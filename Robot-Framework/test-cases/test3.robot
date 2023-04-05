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
    [Setup]    Open Browser and Maximize Browser Window    ${URL}    ${Browser}
    [Teardown]    close browser
    Login To Website    ${StandardUser}    ${Password}
    ${Title}=    get title
    log    Page title is:${Title}
    ${Cookies}=    get cookies
    log    ${Cookies}
    wait until element is visible     xpath://*[@id="page_wrapper"]/footer/ul/li[1]/a
    scroll element into view    xpath://*[@id="page_wrapper"]/footer/ul/li[1]/a
    capture page screenshot
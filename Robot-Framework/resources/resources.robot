*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Browser and Maximize Browser Window
    [Arguments]    ${UserUrl}    ${BrowserName}
    open browser    ${UserUrl}   ${BrowserName}
    maximize browser window
    log    Starting test with ${BrowserName}
    log    Test URL: ${UserUrl}

Login To Website
    [Arguments]    ${Username}    ${Password}
    input text    name:user-name    ${Username}
    input password    xpath:/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input    ${Password}
    click button    name:login-button
    page should not contain element    class:error-message-container

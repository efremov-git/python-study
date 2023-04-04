*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Browser and Maximize Browser Window
    [Arguments]    ${UserUrl}    ${BrowserName}
    open browser    ${UserUrl}   ${BrowserName}
    maximize browser window
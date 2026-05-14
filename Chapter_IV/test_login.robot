*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${URL}        https://www.automationexercise.com/login
${VALID_EMAIL}    nguyenvanro.dev@gmail.com
${VALID_PASSWORD}    Ronv@123123
${INVALID_PASSWORD}    Ronv@123

*** Test Cases ***
Test Login Thành Công
    Open Browser    ${URL}    ${BROWSER}
    Input Text      name=email       ${VALID_EMAIL}
    Input Text      name=password    ${VALID_PASSWORD}
    Click Button    css=button[data-qa="login-button"]
    Title Should Be    Automation Exercise
    Close Browser
 
Test Login Thất Bại
    Open Browser    ${URL}    ${BROWSER}
    Input Text      name=email       ${VALID_EMAIL}
    Input Text      name=password    ${INVALID_PASSWORD}
    Click Button    css=button[data-qa="login-button"]
    Page Should Contain    Your email or password is incorrect!
    Close Browser
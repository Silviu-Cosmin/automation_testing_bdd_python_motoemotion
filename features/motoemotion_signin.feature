Feature: I want to check that the login button from the Motoemotion website is working properly and I can access my account.
  @T1 @negativeTesting
    Scenario Outline: Trying to login with invalid password
      Given I am on the Motoemotion homepage and I want to initiate the login process with invalid password
      When I click on "Contul meu" button
      When I enter my valid email
      When I enter my invalid password "<password>"
      When I click on "Intra in cont" button
      Then I receive an "<error_message>"
      Examples:
        |password|error_message|
        |testing |Email address or password are incorrect|
        |incorect|Email address or password are incorrect|
        |marvel  |Email address or password are incorrect|

  @T2 @positiveTesting
    Scenario: I am on the Motoemotion homepage and I want to initiate the login process with valid credentials
      When I click on "Contul meu" button
      When I enter my valid email
      When I enter my valid password
      When I click on "Intra in cont"
      Then I am redirected to my account page
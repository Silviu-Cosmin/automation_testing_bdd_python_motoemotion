Feature: I want to search for a product in the search bar and add it to the cart
  @T3 @positiveTesting
    Scenario: I want to search for products using the search bar
      Given I am logged in my account
      When I type the product in the search bar
      When I click on the search button
      Then The search results are displayed containing "Rezultatele cautarii pentru:"
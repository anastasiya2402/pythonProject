# Created by anastasiashabanskaya at 3/2/21

# Feature: Hello World

#   Scenario: Test
 #   Given Navigate to Google

Feature: Regression for eBay Search Combo box.

  Scenario: Verify that search displays right items
  Given Open eBay.com
  And Search for "dress"
  And Push button "Search"
    Then All items are dresses


  Scenario: Verifying that typing "dress" displays category "Dresses"
    Given Open eBay.com
    And Search for "dress"
    And Push button "Search"
    Then Category Dresses displayed

    Scenario: Trying to find a dress using filter "Buy It Now"
    Given Open eBay.com
    And Search for "dress"
      And Push button "Search"
    And Choose filter "Buy It Now"
      Then Verifying that the dress you want is there

   Scenario: Verifying that typing "dress1" puts it to category "Dresses"
     Given Open eBay.com
    And Search for "dress1"
    And Press Enter/Return in "Search for anything" field
    Then Category Dresses displayed

  Scenario: Verifying that typing "dress#" puts it to category "Dresses"
     Given Open eBay.com
    And Search for "dress#"
    And Push button "Search"
    Then Category Dresses displayed

   Scenario: Verifying autocompletion: typing "dres" puts it to category "Dresses"
     Given Open eBay.com
    And Search for "dres"
    And Press Enter/Return in "Search for anything" field
    And Stats show large number dresses
    Then There is also a suggestion to search for "dres" instead

  Scenario: Pushing button Search while box is empty displays categories.
    Given Open eBay.com
    And Push button "Search"
    Then All categories are displayed

     Scenario: Verifying that combination of special characters (without whitespace) are allowed in Search.(Actual: not allowed)
    Given Open eBay.com
    And Enter some special characters
    And Press Enter/Return in "Search for anything" field
    Then All categories are displayed

  Scenario: Verifying that only a whitespace is allowed in Search (Actual: not allowed)
   Given Open eBay.com
    And Press space key in Search combo box
    And Press Enter/Return in "Search for anything" field
    Then All categories are displayed

   Scenario: Verifying that capacity of "Search" combo box is 300.
     Given Open eBay.com
     And Enter iphone 11
     And Enter iphone 11
     And Enter iphone 11
     And Enter iphone 11
     And Enter iphone 11
     And Select/Copy/Paste the result
    And  And paste 5 more times(Total 315 characters)
     And Count # of actual elements in the field and compare with 300
    Then Push button "Search"
    Then Verify the message "No exact matches found"

    Scenario: Click on Sell
      Given Open eBay.com
      And Click "Sell" header element

     Scenario: Click on My eBay
      Given Open eBay.com
      And Click "My eBay" header element

     Scenario: Click on Notification
      Given Open eBay.com
      And Click "Notification" header element











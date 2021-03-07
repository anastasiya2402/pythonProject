# Created by anastasiashabanskaya at 3/2/21

# Feature: Hello World

#   Scenario: Test
 #   Given Navigate to Google

Feature: Regression for eBay Search Combo box.

  Scenario: Verify that search displays right items
  Given Open eBay.com
  And Search for "dress"
  And Click the Search button
    Then All items are dresses
#  Then Close the Chrome browser

  Scenario: Verifying that typing "dress" displays category "Dresses"
    Given Open eBay.com
    And Search for "dress"
    And Press Enter/Return
    Then Category Dresses displayed

   Scenario: Verifying that typing "dress1" puts it to category "Dresses"
     Given Open eBay.com
    And Search for "dress1"
    And Press Enter/Return
    Then Category Dresses displayed

  Scenario: Verifying that typing "dress#" puts it to category "Dresses"
     Given Open eBay.com
    And Search for "dress#"
    And Click the Search button
    Then Category Dresses displayed

   Scenario: Verifying autocompletion: typing "dres" puts it to category "Dresses"
     Given Open eBay.com
    And Search for "dres"
    And Press Enter/Return
    And Stats show large number dresses
    Then There is also a suggestion to search for "dres" instead

  Scenario: Pushing button Search while box is empty displays categories.
    Given Open eBay.com
    And Push button "Search"
    Then All categories are displayed

     Scenario: Verifying that combination of special characters (without whitespace) are allowed in Search.(Actual: not allowed)
    Given Open eBay.com
    And Enter some special characters
    And Press Enter/Return
    Then All categories are displayed

  Scenario: Verifying that only a whitespace is allowed in Search (Actual: not allowed)
   Given Open eBay.com
    And Press space key in Search combo box
    And Press Enter/Return
    Then All categories are displayed




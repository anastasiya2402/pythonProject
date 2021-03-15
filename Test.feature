# Created by anastasiashabanskaya at 3/2/21

# Feature: Hello World

#   Scenario: Test
 #   Given Navigate to Google

Feature: Regression for eBay Search Combo box.

  Scenario: Verify that search displays right items
  Given Open eBay.com
  And In search bar type "dress"
  And Push button "Search"
   Then Search results are "Dress" related


  Scenario: Verifying that typing "dress1" puts it to category "Dresses"
    Given Open eBay.com
    And In search bar type "dress1"
    And Push button "Search"
    Then Search results are "Dress" related

  Scenario: Verifying that typing "dress#" puts it to category "Dresses"
    Given Open eBay.com
    And In search bar type "dress#"
    And Push button "Search"
      Then Search results are "Dress" related

   Scenario: Verifying autocompletion: typing "dres" puts it to category "Dresses"
   Given Open eBay.com
    And In search bar type "dres"
    And Push button "Search"
     Then Search results are "Dress" related

  Scenario: Trying to find a dress using filters "Buy It Now" and "Free Shipping"
    Given Open eBay.com
    And In search bar type "dress"
    And Push button "Search"
    And Choose filter "Buy It Now"
    And Next choose more filters: "Shipping"
    And and "Free Shipping"
    Then Verifying that the "Dresses" with such filters are there on the first page


  Scenario: Pushing button Search while box is empty displays categories.
    Given Open eBay.com
    And Push button "Search"
     Then "All Categories" are displayed

  Scenario: Verifying that a whitespace is allowed in Search
   Given Open eBay.com
    And In search bar type " "
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "`" is allowed in Search
   Given Open eBay.com
    And In search bar type "`"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "~" is allowed in Search
   Given Open eBay.com
    And In search bar type "~"
    And Push button "Search"
    Then "All Categories" are displayed

   Scenario: Verifying that a special character "!" is allowed in Search
   Given Open eBay.com
    And In search bar type "!"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "@" is allowed in Search
   Given Open eBay.com
    And In search bar type "@"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "#" is allowed in Search
   Given Open eBay.com
    And In search bar type "#"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "$" is allowed in Search
   Given Open eBay.com
    And In search bar type "$"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "%" is allowed in Search
   Given Open eBay.com
    And In search bar type "%"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "^" is allowed in Search
   Given Open eBay.com
    And In search bar type "^"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "&" is allowed in Search
   Given Open eBay.com
    And In search bar type "&"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "*" is allowed in Search
   Given Open eBay.com
    And In search bar type "*"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "(" is allowed in Search
   Given Open eBay.com
    And In search bar type "("
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character ")" is allowed in Search
   Given Open eBay.com
    And In search bar type ")"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "-" is allowed in Search
   Given Open eBay.com
    And In search bar type "-"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "_" is allowed in Search
   Given Open eBay.com
    And In search bar type "_"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "+" is allowed in Search
   Given Open eBay.com
    And In search bar type "+"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "=" is allowed in Search
   Given Open eBay.com
    And In search bar type "="
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "\" is allowed in Search
   Given Open eBay.com
    And In search bar type "\"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "}" is allowed in Search
   Given Open eBay.com
    And In search bar type "}"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "]" is allowed in Search
   Given Open eBay.com
    And In search bar type "]"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "[" is allowed in Search
   Given Open eBay.com
    And In search bar type "["
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "'" is allowed in Search
   Given Open eBay.com
    And In search bar type "'"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character " is allowed in Search
   Given Open eBay.com
    And In search bar type """
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character ":" is allowed in Search
   Given Open eBay.com
    And In search bar type ":"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character ";" is allowed in Search
   Given Open eBay.com
    And In search bar type ";"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "/" is allowed in Search
   Given Open eBay.com
    And In search bar type "/"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "?" is allowed in Search
   Given Open eBay.com
    And In search bar type "?"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "." is allowed in Search
   Given Open eBay.com
    And In search bar type "."
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character ">" is allowed in Search
   Given Open eBay.com
    And In search bar type ">"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "," is allowed in Search
   Given Open eBay.com
    And In search bar type ","
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a special character "<" is allowed in Search
   Given Open eBay.com
    And In search bar type "<"
    And Push button "Search"
    Then "All Categories" are displayed

  Scenario: Verifying that a certain combination of special characters (without whitespace) are allowed in Search.
   Given Open eBay.com
   And Enter some special characters
   And Push button "Search"
   Then "All Categories" are displayed

   Scenario: Verifying that capacity of "Search" combo box is 300.
     Given Open eBay.com
     And In search bar type "iphone 11"
     And In search bar type "iphone 11"
      And In search bar type "iphone 11"
      And In search bar type "iphone 11"
      And In search bar type "iphone 11"
     And Select/Copy/Paste the result
    And  And paste 5 more times(Total 315 characters)
     And Count # of actual elements in the field and compare with 300
    Then Push button "Search"
    Then Verify the message "No exact matches found"

  Scenario: Trying to find an iPhone 11 using filters "New", "Buy It Now" and "Free Shipping"
    Given Open eBay.com
    And In search bar type "iphone 11"
    And Push button "Search"
    And Choose filter "Buy It Now"
    And Next choose more filters: "Shipping"
    And and "Free Shipping"
    And Next choose more filters: "Condition"
    And and "New"
    Then Verifying that all items are "iPhone 11" with filters

  Scenario: Click on Sell
      Given Open eBay.com
      And Click "Sell" header element

     Scenario: Click on My eBay
      Given Open eBay.com
      And Hover over "My eBay" header element
      And and go to "Recently Viewed" items


     Scenario: Click on Notification
      Given Open eBay.com
      And Click "Notification" header element











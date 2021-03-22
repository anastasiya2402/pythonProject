# Created by anastasiashabanskaya at 3/2/21


Feature: Regression for eBay Search Combo box.

  Scenario: Verify that search displays right items
  Given Open eBay.com
  And In search bar type "dress"
  And Push button "Search"
  Then Search results are "dress" related


  Scenario: Verifying that typing "dress1" puts it to category "Dresses"
    Given Open eBay.com
    And In search bar type "dress1"
    And Push button "Search"
    Then Search results are "dress" related

  Scenario: Verifying that typing "dress#" puts it to category "Dresses"
    Given Open eBay.com
    And In search bar type "dress#"
    And Push button "Search"
    Then Search results are "dress" related

   Scenario: Verifying autocompletion: typing "dres" puts it to category "Dresses"
    Given Open eBay.com
    And In search bar type "dres"
    And Push button "Search"
    Then Search results are "dress" related
 #   Then Delete all cookies

  Scenario: Trying to find a dress using filters "Buy It Now" and "Free Shipping"
    Given Open eBay.com
    And In search bar type "dress"
    And Push button "Search"
    And Choose filter "Buy It Now"
    And Next choose more filters: "Shipping"
    And and "Free Shipping"
    Then Verifying that all items are "dresses" with filters "Free shipping" and "Buy It Now"

  Scenario: Trying to find an iPhone 11 using filters "New", "Buy It Now" and "Free Shipping"
    Given Open eBay.com
    And In search bar type "iphone 11"
    And Push button "Search"
    And Choose filter "Buy It Now"
    And Next choose more filters: "Shipping"
    And and "Free Shipping"
    And Next choose more filters: "Condition"
    And and "New"
    Then Verifying that all items are "iPhone 11" with filters "Free Shipping", "Brand New" and "Buy It Now"(or Best Offer)

  Scenario Outline: Verifying that items are Search related using Table as a variable
    Given Open eBay.com
    And In search bar type "<search_item>"
    And Push button "Search"
    And Choose filter "Buy It Now"
    And Next choose more filters: "Shipping"
    And and "Free Shipping"
    Then Verifying that all items are "<search_item>" related

  Examples:
    | search_item |
    | dress       |
    | iphone      |
    | baby dress  |


  Scenario: Verifying that filters work
    Given Open eBay.com
    And In search bar type "shoes"
    And Push button "Search"
    And From chosen 60 checkbox filters starting with Brand, choose filters: "0", "5", "6", "16"
    And Then choose more filters: "New with tags"
    And and also "Free Shipping"
    Then Verifying that all items are "shoes" related and contain "Free shipping"


   Scenario: Verifying that filters work: finding a pair for myself
    Given Open eBay.com
    And In search bar type "shoes"
    And Push button "Search"
    And Click on Women
    And Choose size 8.5
    And From Color, choose White
    And In Brand click on see all
    And In New Window choose Not Specified
    Then Push Apply button
    Then Search results are "shoes" related

    Scenario: Verifying that filters work: finding a pair of skechers for myself
    Given Text as a variable
      """
      Verifying that all items are "skechers" related and contain "Free shipping"

      """
    And Open eBay.com
    And In search bar type "skechers"
    And Push button "Search"
    And Choose size 8.5
    And From Color options, choose Pink
    And Choose more filters: "New with tags"
    And and also choose "Free Shipping"
    And Verifying that all items are "skechers" related and contain "Free shipping"


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











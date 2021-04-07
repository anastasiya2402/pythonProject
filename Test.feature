# Created by anastasiashabanskaya at 3/2/21


Feature: Regression testing for eBay.

#  Scenario: Verify that search displays right items
#  Given Open eBay.com
#  And In search bar type "dress"
#  And Push button "Search"
#  Then Search results are "dress" related


#  Scenario: Verifying that typing "dress1" puts it to category "Dresses"
#    Given Open eBay.com
#    And In search bar type "dress1"
#    And Push button "Search"
#    Then Search results are "dress" related
#
#  Scenario: Verifying that typing "dress#" puts it to category "Dresses"
#    Given Open eBay.com
#    And In search bar type "dress#"
#    And Push button "Search"
#    Then Search results are "dress" related
#
#   Scenario: Verifying autocompletion: typing "dres" puts it to category "Dresses"
#    Given Open eBay.com
#    And In search bar type "dres"
#    And Push button "Search"
#    Then Search results are "dress" related


  Scenario: Trying to find a dress using filters "Buy It Now" and "Free Shipping"
    Given Open eBay.com
    And In search bar type "dress"
    And Push button "Search"
    And Choose filter "Buy It Now"
    And Next choose more filters: "Shipping"
    And and "Free Shipping"
    Then Verifying that all items are "dress" related


  Scenario: Trying to find an iPhone 11 using filters "New", "Buy It Now" and "Free Shipping"
    Given Open eBay.com
    And In search bar type "iphone 11"
    And Push button "Search"
    And Choose filter "Buy It Now"
    And Next choose more filters: "Shipping"
    And and "Free Shipping"
    And Next choose more filters: "Condition"
    And and "New"
    Then Verifying that all items are "iPhone 11" with above filters


  Scenario Outline: Filtering men items
    Given Open eBay.com
    And In search bar type "<search_item>"
    And Push button "Search"
    Then Apply following filters

    | Filter         |  value          | text          |  size           | title          | color          |
    | <filter_name> | <filter_value>   | <filter_text> | <filter_size>   | <filter_title> | <filter_color> |


   Examples: Men shoes
    | search_item | filter_name    | filter_value  | filter_text   | filter_size | filter_title | filter_color |
    | shoes       | Brand          | adidas        | US Shoe Size  | 8.5         | Color        | Pink         |
    | shoes       | Upper Material | Leather       | US Shoe Size  | 9           | Color        | Red          |
    | shoes       | Features       | Comfort       | US Shoe Size  | 9.5         | Color        | Black        |
    | shoes       | Pattern        | Solid         | US Shoe Size  | 10          | Color        | Gray         |

    Then Search results are "<search_item>" related


   Scenario Outline: Filtering checkbox&radio buttons related items
    Given Open eBay.com
    And In search bar type "<search_item>"
    And Push button "Search"
    Then Apply the following filters

    | Items          |  value           |
    | <filter_name1> | <filter_value1>  |
    | <filter_name2> | <filter_value2>  |

   Examples: Dress and shoe related
    | search_item | filter_name1    | filter_value1  | filter_name2  | filter_value2 |
    | baby dress  | Brand          | Disney        | Color           | Pink          |
    | pumps       | Upper Material | Leather       | Heel Height     | Low           |
    | skechers    | Occasion       | Casual        | Upper Material  | Suede         |

   Examples: Jewelries
    | search_item   | filter_name1   | filter_value1 | filter_name2  | filter_value2          |
    | stud earrings | Item Location  | North America | Color         | Pink                   |
    | necklace      | Color          | Yellow        | Metal         | Yellow Gold Filled     |
    | seiko         | Department     | Women         | Movement      | Mechanical (Automatic) |

   Examples: Dog related items
    | search_item   | filter_name1   | filter_value1 | filter_name2  | filter_value2  |
    | dog clothing  | Dog Size       | XS            | Type          | Hoodie         |
    | dog supplies  | Material       | Cotton        | Dog Breed     | Maltese        |

    Then Search results are "<search_item>" related

   Scenario: Validating filters doing a man search of Nike shoes
    Given Open eBay.com
    And In search bar type "shoes"
    And Push button "Search"
    And Choose Size 8.5
    And From Color, choose Red
    And In Brand choose Nike
    And In Shipping Options choose Free Shipping
    Then Validating the filters and the text "shoes" when the search contains Free shipping
      | filter                  | value         |
      | Brand                   | Nike          |
      | US Shoe Size (Men's)    | 8.5           |
      | Color                   | Red           |

  Scenario: Working on filters doing a woman search of Nike shoes
    Given Open eBay.com
    And In search bar type "shoes"
    And Push button "Search"
    And In Brand choose Nike
    And Click on Women
    And Choose Size 8.5
    And We choose from Color, Pink
    And In Shipping Options choose Free Shipping
    Then Validating the filters and the text "shoes" when the search contains Free shipping
      | filter                      | value         |
      | Brand                       | Nike          |
      | US Shoe Size (Women's)      | 8.5           |
      | Color                       | Pink          |
      | Department                  | Women         |



    Scenario Outline: Verifying that filters work: finding a pair of skechers
    Given Text as a variable
      """
      Verifying that all items are "skechers" related, contain "Free shipping" and satisfy the filters given below

      """
    And Open eBay.com
    And In search bar type "skechers"
    And Push button "Search"
    And Choose Size 9
    And In Occasion choose Casual
    And From Color, choose White
    And In Shipping Options choose Free Shipping
    Then Validating that all items have text "skechers", contain Free shipping and satisfy the filters given below

      | Filter         |  value          | text          |  output         | title          | color          |
      | <filter_name>  | <filter_value>  | <filter_text> | <filter_output> | <filter_title> | <filter_color> |

    Examples:
      | filter_name    | filter_value   | filter_text            | filter_output | filter_title | filter_color |
      | Occasion       | Casual         | US Shoe Size (Women's) | 9             | Color        | White        |


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

  Scenario: Verifying that a whitespace only is allowed in Search
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
   And In search bar type "@!#$%^&*()-_=+`~|]}[{'/.>,<?"
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

    Scenario: Checking flyout menu
    Given Open eBay.com
    And Do actions with Home & Garden flyout menu Kitchen, Dining & Bar menu item

   Scenario: Playing cards
     Given Open website
     And Drag and drop numbers to texts
     Then Verify a pop-up message "You did it!"











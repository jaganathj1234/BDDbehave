Feature: Registration Functionality

  @Sanity
  Scenario Outline: Registration with valid data
    Given User is on Registration Page
    When User enters gender
    And User enters first name"<FirstName>"
    And User enters last name"<LastName>"
    And User enters email"<Email>"
    And User enters password"<Password>"
    And User enters Confirm Password"<ConfirmPassword>"
    And User clicks on Register button
    Then User should be registered successfully

    Examples: RegisterDetails
      | FirstName | LastName | Email            | Password | ConfirmPassword |
      | Jag       | J        | email1@email.com | ps1234   | ps1234          |

  @Sanity
  Scenario Outline: Registration with duplicate data
    Given User is on Registration Page
    When User enters gender
    And User enters first name"<FirstName>"
    And User enters last name"<LastName>"
    And User enters duplicate email"<Email>"
    And User enters password"<Password>"
    And User enters Confirm Password"<ConfirmPassword>"
    And User clicks on Register button
    Then User should not be registered successfully

    Examples: RegisterDetails
      | FirstName | LastName | Email            | Password | ConfirmPassword |
      | Jag       | J        | email1@email.com | ps1234   | ps1234          |
      | abc       | D        | email1@email.com | ps1234   | ps1234          |

   @Regression
   Scenario Outline: Place an order
     Given user is on website
     When User logs into website"<login_name>""<login_pass>"
     And user adds items to cart
     And user confirms checkout
     And user enters Billing address"<ba_company>""<ba_city>""<ba_address1>""<ba_address2>""<ba_zip>""<ba_phone>""<ba_fax>"
     And user enters Shipping address
     And user enters Shipping method
     And user enters Payment method
     And user enters Payment information
     And user Confirms order

     Examples: OrderDetails
      | login_name   | login_pass | ba_company | ba_city| ba_address1 | ba_address2 | ba_zip | ba_phone | ba_fax |
      | email2@e.com | abc123     | MT         |sydney  | add1        | add2        | 2066   | 1231313  | 2131232|

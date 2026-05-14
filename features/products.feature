Feature: The product service back-end
    As a Product Manager
    I need a RESTful catalog service
    So that I can keep track of all my products

Background:
    Given the following products
        | name       | description | price | available | category   |
        | Fedora     | A hat       | 29.50 | True      | CLOTHS     |
        | iPhone     | A phone     | 899.0 | True      | UNKNOWN    |
        | Wrench     | A tool      | 15.00 | False     | TOOLS      |
        | Apples     | Fruit       | 2.50  | True      | FOOD       |

Scenario: Read a Product
    When I visit the "Home Page"
    And I set the "Name" to "Fedora"
    And I press the "Search" button
    Then I should see "Fedora" in the "Name" field
    When I press the "Clear" button
    And I press the "Search" button
    Then I should see "Fedora" in the results

Scenario: Update a Product
    When I visit the "Home Page"
    And I set the "Name" to "Fedora"
    And I press the "Search" button
    Then I should see "Fedora" in the "Name" field
    When I change "Name" to "Sombrero"
    And I press the "Update" button
    Then I should see the message "Success"

Scenario: Delete a Product
    When I visit the "Home Page"
    And I set the "Name" to "Fedora"
    And I press the "Search" button
    Then I should see "Fedora" in the "Name" field
    When I press the "Delete" button
    Then I should see the message "Product has been Deleted!"

Scenario: List all Products
    When I visit the "Home Page"
    And I press the "Search" button
    Then I should see "Fedora" in the results
    And I should see "iPhone" in the results
    And I should see "Wrench" in the results

Scenario: Search for a Product by Name
    When I visit the "Home Page"
    And I set the "Name" to "Fedora"
    And I press the "Search" button
    Then I should see "Fedora" in the results
    And I should not see "iPhone" in the results

Scenario: Search for a Product by Category
    When I visit the "Home Page"
    And I select "CLOTHS" in the "Category" dropdown
    And I press the "Search" button
    Then I should see "Fedora" in the results
    And I should not see "Apples" in the results

Scenario: Search for a Product by Availability
    When I visit the "Home Page"
    And I select "False" in the "Available" dropdown
    And I press the "Search" button
    Then I should see "Wrench" in the results
    And I should not see "Fedora" in the results

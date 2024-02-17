Feature: Save text from a web page

  Scenario: User needs to save text from webpage
    Given I have opened the webpage
    When I copy text from the webpage
    Then I should be able to save the text to a "copiedText.txt" file

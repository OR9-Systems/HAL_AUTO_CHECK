Feature: Save text from a halcion page

  Scenario: User needs to save text from halcion
    Given I opened the halcion page
    When I copy text from halcion
    Then I should be able to save the text to an input text file name of my choosing exp: "copiedText.txt" file

Feature: Capture screenshot for a webpage
    Scenario: Take screenshot for a URL
        Given I visit a URL "https://learnattack.de/deutsch"
        Then execute JavaScript function to scroll
        Then capture screenshot of the page

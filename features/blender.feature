Feature: Demo av blender-test
  Scenario: Blend apple
    Given I put "apple" in a blender
    When I switch the blender on
    Then it should transform into "apple juice"

  Scenario: Blend frog
    Given I put "frog" in a blender
    When I switch the blender on
    Then it should transform into "something disgusting"

  Scenario: Blend banana
    Given I put "banana" in a blender
    When I switch the blender on
    Then it should transform into "something disgusting"
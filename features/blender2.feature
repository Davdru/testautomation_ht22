Feature: More thing with the blender class
  Scenario Outline: Blend different thing
    Given I put "<thing>" in a blender
    When I switch the blender on
    Then it should transform into "<resulting thing>"
  Examples: Thing to mix
    | thing   | resulting thing       |
    | apple   | apple juice           |
    | banana  | something disgusting  |
    | orange  | orange juice          |

# I put "apple" in a blender
# I put "banana" in a blender
# I put "orange" in a blender
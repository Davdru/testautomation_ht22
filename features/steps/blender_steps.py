from behave import *
from blender import Blender

# I put "banana" in a blender
@given(u'I put "{text}" in a blender')
def step_impl(context, text):
    context.blender = Blender()
    context.blender.add(text)


@when(u'I switch the blender on')
def step_impl(context):
    context.blender.switch_on()

# it should transform into "something disgusting"
@then(u'it should transform into "{text}"')
def step_impl(context, text):
    assert context.blender.result == text, f"got {context.blender.result} expected {text}"


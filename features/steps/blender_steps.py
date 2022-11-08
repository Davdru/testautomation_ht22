from behave import *
from blender import Blender


@given(u'I put appple in a blender')
def step_impl(context):
    context.blender = Blender()
    context.blender.add("apple")


@when(u'I switch the blender on')
def step_impl(context):
    context.blender.switch_on()


@then(u'it should transform into apple juice')
def step_impl(context):
    assert context.blender.result == "apple juice"


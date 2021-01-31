import os

@given(u'Jestem  zalogowany na komputerze')
def step_impl(context):
    #    raise NotImplementedError(u'STEP: Given Jestem  zalogowany na komputerze')
    context.os = os

@when(u'sprawdzam ile procesorow posiada komputer')
def step_impl(context):
    #    raise NotImplementedError(u'STEP: When sprawdzam ile procesorow posiada komputer')
    os = context.os
    context.ilosc_linijek = os.popen("grep process /proc/cpuinfo |wc -l").read().strip()

@then(u'Otrzymuje ilosc procesorow = 2')
def step_impl(context):
    #    raise NotImplementedError(u'STEP: Then Otrzymuje ilosc procesorow = 2')
    assert context.ilosc_linijek == "2"

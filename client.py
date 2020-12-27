from xmlrpc import client
knx=client.ServerProxy('http://192.168.1.5:8000/')


print(knx.scenario_up())
print(knx.scenario_down())
print(knx.scenario_left())
print(knx.scenario_right())
print(knx.scenario_front())
print(knx.scenario_back())
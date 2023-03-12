from typing import Type

# switch, on, off

class Switch:
    def __init__(self, room: str):
        self.__room = room
    
    def on(self):
        print('lighting up {}'.format(self.__room))
    
    def off(self):
        print('turning off {}'.format(self.__room))

class Person:
    def lighting_up(self, switch: Type[Switch]):
        switch.on()
    
    def turning_off(self, switch: Type[Switch]):
        switch.off()
    
    def sleep(self):
        print('I went to sleep')

people = Person()
room_switch = Switch('room')
kitchen_switch = Switch('kitchen')

room_switch.on()
people.lighting_up(kitchen_switch)
people.turning_off(room_switch)
people.sleep()
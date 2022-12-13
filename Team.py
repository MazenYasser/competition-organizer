# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:08:26 2022

@author: as292
"""

class Team ():
    def __init__(self):
        self.name = ''
        self.strength = 0
        self.point = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.win_count = 0
        self.lose_count = 0 
        self.draw_count = 0
        
    def set_name (self, name):
        self.name = name
        
    def set_strength(self, strength):
        self.strength = strength
    
    def set_point(self, point):
        self.point = point


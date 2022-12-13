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
    
    
    def set_goals_scored(self, goals_scored):
        self.goals_scored = goals_scored
    
    def set_goals_conceded(self, goals_conceded):
        self.goals_conceded = goals_conceded
    
    def set_win_count(self, win_count):
        self.win_count = win_count
    
    def set_lose_count(self, lose_count):
        self.lose_count = lose_count
    
    def set_draw_count(self, draw_count):
        self.draw_count = draw_count
    
    


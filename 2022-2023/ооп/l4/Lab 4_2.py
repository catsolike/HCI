class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0


    def score(self, newGoals = 1):
        self.goals += newGoals


    def make_assist(self, newAssists = 1):
        self.assists += newAssists


    def statistics(self):
        print(f'{self.name} {self.surname} - голы: {self.goals}, передачи: {self.assists}')


leo = SoccerPlayer('Leo', 'Messi')  
leo.score(700)  
leo.make_assist(500)  
leo.statistics()

kokorin = SoccerPlayer('Alex', 'Kokorin')  
kokorin.score()  
kokorin.statistics()
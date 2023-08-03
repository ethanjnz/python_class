players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers",
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls",
    },
]

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets",
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics",
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets",
}

# Create your Player instances here!
# player_jason = ???


# first question - how do i pass through the each key value pair into class?
# well first lets pass the player list into the class parameter


class Player:
    team = []

    def __init__(self, player_dictionary):
        self.name = player_dictionary["name"]
        self.age = player_dictionary["age"]
        self.position = player_dictionary["position"]
        self.team = player_dictionary["team"]

    def __repr__(self):
        return f"Player: {self.name} is {self.age} years old, and plays {self.position} on the {self.team}"

        # create a place to store the return of the class method
        # iterate over team_list with a for loop
        # push the obect onto the class variable with append

    @classmethod
    def get_team(cls, team_list):
        for obj in team_list:
            cls.team.append(obj)
            # ^sends the ojbects of players to team empty list^


# loop over the players list
# create a variable player and set the list object equal to that
# push into new list with append
new_team = []
# loops over the Players list
for specific_dict in players:
    # creates a variable called basketball_player and assign it that specific object while also creating a instance
    basketball_player = Player(specific_dict)
    # pushes the basketball_player on to new list
    new_team.append(basketball_player)


player_jason = Player(jason)
player_Kevin = Player(kevin)
player_Kyrie = Player(kyrie)
Player.get_team(players)
print(Player.team)
# print(player_jason)
# print(player_Kevin)
# print(player_Kyrie)

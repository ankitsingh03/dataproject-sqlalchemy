from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, func
from sqlalchemy.orm import sessionmaker
import csv
import json
from collections import defaultdict


engine = create_engine('postgresql://ankit:ankit@localhost:5432/ankitdb')
Base = declarative_base()
Session = sessionmaker(bind=engine)


def create_table():

    class Umpire(Base):
        __tablename__ = ('umpire')
        id = Column(Integer, primary_key=True)
        umpire = Column(String)
        nationality = Column(String)
        first_officiated = Column(Integer)
        last_officiated = Column(Integer)
        no_of_matches = Column(Integer)

    class Deliveries(Base):
        __tablename__ = ('deliveries')
        id = Column(Integer, primary_key=True)
        match_id = Column(Integer)
        inning = Column(Integer)
        batting_team = Column(String)
        bowling_team = Column(String)
        over = Column(Integer)
        ball = Column(Integer)
        batsman = Column(String)
        non_striker = Column(String)
        bowler = Column(String)
        is_super_over = Column(Integer)
        wide_runs = Column(Integer)
        bye_runs = Column(Integer)
        legbye_runs = Column(Integer)
        noball_runs = Column(Integer)
        penalty_runs = Column(Integer)
        batsman_runs = Column(Integer)
        extra_runs = Column(Integer)
        total_runs = Column(Integer)
        player_dismissed = Column(String)
        dismissal_kind = Column(String)
        fielder = Column(String)

    class Matches(Base):
        __tablename__ = ('matches')
        id = Column(Integer, primary_key=True)
        season = Column(Integer)
        city = Column(String)
        date = Column(Date)
        team1 = Column(String)
        team2 = Column(String)
        toss_winner = Column(String)
        toss_decision = Column(String)
        result = Column(String)
        dl_applied = Column(Integer)
        winner = Column(String)
        win_by_runs = Column(Integer)
        win_by_wickets = Column(Integer)
        player_of_match = Column(String)
        venue = Column(String)
        umpire1 = Column(String)
        umpire2 = Column(String)
        umpire3 = Column(String)

    Base.metadata.create_all(bind=engine)
    return Umpire, Deliveries, Matches


def push_data(Umpire, Deliveries, Matches):
    session = Session()
    # umpire_data
    with open('assets/umpire_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()
        for line in csv_reader:
            session.add(Umpire(
                umpire=line[0], nationality=line[1],
                first_officiated=line[2], last_officiated=line[3],
                no_of_matches=line[4]))

    # top batsman data
    # open the csv file and clean data
    with open('assets/deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()
        for line in csv_reader:
            session.add(Deliveries(
                match_id=line[0], inning=line[1],
                batting_team=line[2], bowling_team=line[3],
                over=line[4], ball=line[5], batsman=line[6],
                non_striker=line[7], bowler=line[8],
                is_super_over=line[9], wide_runs=line[10],
                bye_runs=line[11], legbye_runs=line[12],
                noball_runs=line[13], penalty_runs=line[14],
                batsman_runs=line[15], extra_runs=line[16],
                total_runs=line[17], player_dismissed=line[18],
                dismissal_kind=line[19], fielder=line[20]))

    with open('assets/matches.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()
        # creating dict {season: list of teams name}
        for line in csv_reader:
            session.add(Matches(
                season=line[1], city=line[2],
                date=line[3], team1=line[4],
                team2=line[5], toss_winner=line[6],
                toss_decision=line[7], result=line[8],
                dl_applied=line[9], winner=line[10],
                win_by_runs=line[11], win_by_wickets=line[12],
                player_of_match=line[13], venue=line[14],
                umpire1=line[15], umpire2=line[16],
                umpire3=line[17]))
    session.commit()
    session.close()


def database_json_1(Umpire):
    session = Session()
    # umpire
    umpire_data = session.query(
        Umpire.nationality, func.count(Umpire.nationality))\
        .group_by(Umpire.nationality)\
        .order_by(func.count(Umpire.nationality).desc())\
        .filter(Umpire.nationality != 'India').all()

    with open(
        "assets/foreign_umpire_analysis.json", "w"
              ) as outfile:
        json.dump(dict(umpire_data), outfile)


def database_json_2(Deliveries):
    # top 10 batsman by total run over the year
    session = Session()
    top_batsman = session.query(
        Deliveries.batsman,
        func.sum(Deliveries.batsman_runs)).group_by(Deliveries.batsman)\
        .order_by(func.sum(Deliveries.batsman_runs).desc()).limit(10).all()

    with open(
        "assets/top_batsman_for_royal_challengers_bangalore.json", "w"
              ) as outfile:
        json.dump(dict(top_batsman), outfile)


def database_json_3(Deliveries):
    # top 10 team by run over the history
    session = Session()
    top_teams = session.query(
        Deliveries.batting_team, func.sum(Deliveries.total_runs))\
        .group_by(Deliveries.batting_team)\
        .order_by(func.sum(Deliveries.total_runs).desc()).all()

    # Pushing all the required data to json file
    with open("assets/total_runs_scored_by_team.json", "w") as outfile:
        json.dump(dict(top_teams), outfile)


def database_json_4(Matches):
    session = Session()
    # y = [i.season for i in session.query(Matches)
    # .distinct(Matches.season).all()]
    # print(y)
    result = session.query(
        Matches.season, Matches.team1, func.count(Matches.team1))\
        .group_by(Matches.season, Matches.team1)\
        .order_by(Matches.season).all()
    print(result)
    print()
    result = session.query(
        Matches.season, Matches.team2, func.count(Matches.team2))\
        .group_by(Matches.season, Matches.team2)\
        .order_by(Matches.season).all()
    print(result)
    print()

    result = session.query(Matches).all()
    season = defaultdict(list)
    teams = set()
    for i in result:
        season[i.season].extend([i.team1, i.team2])
        teams.update({i.team1, i.team2})

    # creating dict {season: {team: number of matches played in one season}}
    total = {}
    for p, q in season.items():
        for i in q:
            total[p] = {i: q.count(i) for i in q}
    print(total)
    year = sorted(total.keys())

    # formation of dict {team_name: [data over the year]}
    team_data = defaultdict(list)
    for i in teams:
        for j in year:
            team_data[i].append(total[j].get(i, 0))

    # print(team_data)
    # data = {'years': year,
    #         'team_data':
    #         [{'name': i, 'data': j} for i, j in team_data.items()]
    #         }
    # with open(
    #     "assets/stacked_chart_of_matches_played_by_team_by_season.json", "w"
    #           ) as outfile:
    #     json.dump(data, outfile)


if __name__ == "__main__":
    umpire, deliveries, matches = create_table()
    push_data(umpire, deliveries, matches)
    database_json_1(umpire)
    database_json_2(deliveries)
    database_json_3(deliveries)
    database_json_4(matches)

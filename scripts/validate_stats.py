import csv

def read_csv(filename):
    with open(filename, 'r') as file:
        return list(csv.DictReader(file))

def basic_stats(filename):
    print(f"\n=== Basic Statistics for the file: {filename} ===")
    data = read_csv(filename)

    # fix BOM issue in 'Player' column
    if '\ufeffPlayer' in data[0]:
        for row in data:
            row['Player'] = row.pop('\ufeffPlayer')

    print("Available columns:", list(data[0].keys()))

    # total players
    total_players = len(data)
    print(f"\nTotal players: {total_players}")

    # total games (max of 'Games Played')
    try:
        games_played = [int(row['Games Played']) for row in data if row['Games Played'].isdigit()]
        total_games = max(games_played)
        print(f"Total games in season: {total_games}")
    except:
        print("⚠️ Error calculating total games.")

    # total team points
    try:
        total_points = sum(int(row['Points']) for row in data if row['Points'].isdigit())
        print(f"Total team points: {total_points}")
    except:
        print("⚠️ Error calculating total team points.")

    # top scorer
    try:
        top_scorer = max(data, key=lambda row: int(row['Points']) if row['Points'].isdigit() else -1)
        print(f"Top scorer: {top_scorer['Player']} with {top_scorer['Points']} points")
    except:
        print("⚠️ Column 'Points' not found for top scorer.")

    # most assists
    try:
        top_assists = max(data, key=lambda row: int(row['Assists']) if row['Assists'].isdigit() else -1)
        print(f"Most assists: {top_assists['Player']} with {top_assists['Assists']} assists")
    except:
        print("⚠️ Column 'Assists' not found.")

    # most ground balls
    try:
        top_defense = max(data, key=lambda row: int(row['Ground Balls']) if row['Ground Balls'].isdigit() else -1)
        print(f"Most ground balls: {top_defense['Player']} with {top_defense['Ground Balls']}")
    except:
        print("⚠️ Column 'Ground Balls' not found.")

    # average points per player
    print("\nAverage points per game per player:")
    for row in data:
        try:
            gp = int(row['Games Played'])
            pts = int(row['Points'])
            avg = round(pts / gp, 2) if gp > 0 else 0
            print(f"{row['Player']}: {avg}")
        except:
            print(f"{row.get('Player', 'Unknown')}: ⚠️ Invalid or missing data")

if __name__ == '__main__':
    filename = '../data/syracuse_wlax_stats_2025.csv'
    basic_stats(filename)

import os
import pandas as pd
from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import (
    leaguegamefinder,
    playergamelogs,
    commonteamroster,
)
import time

# ── Dossier de sortie ─────────────────────────────────────────────────────────
OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SEASON = "2024-25"  # saison à récupérer


# ── 1. Équipes ────────────────────────────────────────────────────────────────

def fetch_teams():
    print("Récupération des équipes...")
    df = pd.DataFrame(teams.get_teams())
    df.to_csv(f"{OUTPUT_DIR}/teams.csv", index=False)
    print(f"  ✓ {len(df)} équipes sauvegardées")
    return df


# ── 2. Joueurs actifs ─────────────────────────────────────────────────────────

def fetch_players():
    print("Récupération des joueurs actifs...")
    df = pd.DataFrame(players.get_active_players())
    df.to_csv(f"{OUTPUT_DIR}/players.csv", index=False)
    print(f"  ✓ {len(df)} joueurs sauvegardés")
    return df


# ── 3. Matchs de la saison ────────────────────────────────────────────────────

def fetch_games(season=SEASON):
    print(f"Récupération des matchs {season}...")
    gamefinder = leaguegamefinder.LeagueGameFinder(
        season_nullable=season,
        league_id_nullable="00",  # NBA
    )
    df = gamefinder.get_data_frames()[0]
    df.to_csv(f"{OUTPUT_DIR}/games.csv", index=False)
    print(f"  ✓ {len(df)} lignes de matchs sauvegardées")
    return df


# ── 4. Stats joueurs par match ────────────────────────────────────────────────

def fetch_player_game_logs(season=SEASON):
    print(f"Récupération des stats joueurs {season}...")
    logs = playergamelogs.PlayerGameLogs(
        season_nullable=season,
        league_id_nullable="00",
    )
    df = logs.get_data_frames()[0]
    df.to_csv(f"{OUTPUT_DIR}/player_game_logs.csv", index=False)
    print(f"  ✓ {len(df)} lignes de stats sauvegardées")
    return df


# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    print(f"=== Ingestion NBA — Saison {SEASON} ===\n")

    fetch_teams()
    time.sleep(1)

    fetch_players()
    time.sleep(1)

    fetch_games()
    time.sleep(1)

    fetch_player_game_logs()

    print("\n=== Ingestion terminée ===")
    print(f"Fichiers disponibles dans le dossier '{OUTPUT_DIR}/'")


if __name__ == "__main__":
    run()
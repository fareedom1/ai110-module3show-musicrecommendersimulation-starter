"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "="*45)
    print(" 🎵       YOUR TOP RECOMMENDATIONS         🎵")
    print("="*45 + "\n")

    for i, rec in enumerate(recommendations, 1):
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{i}. {song['title'].upper()} by {song['artist']}")
        print(f"   🏆 Final Score: {score:.2f}")
        print("   ✨ Why you'll love it:")
        
        # Split the semicolon-separated reasons into clean bullet points
        reasons = explanation.split("; ")
        for reason in reasons:
            print(f"      • {reason}")
        print("-" * 45)


if __name__ == "__main__":
    main()

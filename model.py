import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from mood_classifier import classify_mood
from spotify_client import create_spotify_client
import spotipy

# Crée le client Spotify
sp = create_spotify_client()


def fetch_song_from_spotify(song_name):
    """
    Recherche une chanson sur Spotify et retourne une ligne DataFrame avec les audio features.
    Retourne None si la chanson n'est pas trouvée ou si les features sont indisponibles.
    """
    try:
        result = sp.search(q=song_name, type="track", limit=1)

        if not result["tracks"]["items"]:
            return None

        track = result["tracks"]["items"][0]
        track_id = track["id"]

        features_list = sp.audio_features(track_id)
        if not features_list or features_list[0] is None:
            return None
        features = features_list[0]

        artists = ", ".join([a["name"] for a in track["artists"]])

        song_data = {
            "name": track["name"],
            "artists": artists,
            **{k: v for k, v in features.items() if isinstance(v, (float, int))}
        }

        return pd.DataFrame([song_data])

    except spotipy.SpotifyException as e:
        print(f"Spotify API error: {e}")
        return None


def recommend_songs(song_name, df, top_n=10):
    """
    Recommande des chansons similaires en utilisant le dataset et Spotify si nécessaire.
    Filtrage par mood via NLP. 
    Insensible à la casse.
    Retourne None si la chanson n'est trouvée nulle part.
    """
    if not isinstance(song_name, str) or not song_name.strip():
        return None

    # 1. Préparer la comparaison insensible à la casse
    song_name_lower = song_name.lower()
    df["name_lower"] = df["name"].str.lower()

    # 2. Vérifier si la chanson est dans le dataset local
    if song_name_lower in df["name_lower"].values:
        song_row = df[df["name_lower"] == song_name_lower]
    else:
        # 3. Sinon, chercher sur Spotify
        song_row = fetch_song_from_spotify(song_name)
        if song_row is None:
            # chanson non trouvée
            df.drop(columns=["name_lower"], inplace=True)
            return None
        df = pd.concat([df, song_row], ignore_index=True)

    # 4. Calculer la similarité audio
    numeric_df = df.select_dtypes(include="number")
    song_vector = numeric_df[df["name_lower"] == song_name_lower].values
    if len(song_vector) == 0:
        df.drop(columns=["name_lower"], inplace=True)
        return None

    similarities = cosine_similarity(song_vector, numeric_df)[0]
    df["similarity"] = similarities

    recommended = df[df["name_lower"] != song_name_lower].sort_values(
        by="similarity", ascending=False
    ).head(top_n)

    # 5. Mood filtering
    input_mood = classify_mood(song_name)
    recommended["mood"] = recommended["name"].apply(classify_mood)

    same_mood = recommended[recommended["mood"] == input_mood]

    # 6. Nettoyage colonne temporaire
    df.drop(columns=["name_lower"], inplace=True)

    # 7. Retourner recommendations
    return same_mood if not same_mood.empty else recommended

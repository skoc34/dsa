# Spotify Mood Analysis 🎧

## Introduction
This project aims to analyze my personal Spotify listening data to uncover patterns in my music habits and their relationship with my mood. Using the Spotify Web API, I will collect data on the tracks I listen to, their audio features (e.g., energy, valence), and associated metadata such as genres and artists. The ultimate goal is to understand how music impacts my mood and provide personalized recommendations based on the insights.

---

## Dataset Description
### Spotify Web API
**Purpose:** Provides access to personal Spotify data.  
**Data Retrieved:**
- **Listening History:** Information about recently played tracks, including track names, artists, and albums.
- **Audio Features:** Details such as energy, valence, danceability, and tempo for each track.
- **Genres and Artists:** Classification of tracks by genre and artist metadata.

---

## Project Idea and Plan
### Objectives
- **Understand Listening Habits:** Analyze listening history to identify patterns over time (e.g., daily, weekly trends).
- **Discover Mood Patterns:** Examine correlations between audio features (valence, energy) and mood categories.
- **Personalized Recommendations:** Suggest mood-enhancing playlists and rediscover overlooked tracks.

### Data Collection
- **Fetch Listening History:** Retrieve recently played tracks using the Spotify API.
- **Gather Audio Features:** Collect energy, valence, tempo, and other musical attributes for each track.
- **Analyze Genres and Artists:** Retrieve genre and artist metadata for deeper insights.

### Data Analysis
#### **Listening Trends**
- Calculate daily and weekly listening habits.
- Identify top artists, genres, and tracks over specific time frames.

#### **Mood Patterns**
- Cluster tracks based on valence and energy scores to define mood categories:
  - **Happy:** High valence, high energy
  - **Calm:** High valence, low energy
  - **Sad:** Low valence, low energy
  - **Energetic:** Low valence, high energy
- Analyze mood distribution over time (e.g., morning vs. evening listening patterns).

#### **Rediscover Underplayed Tracks**
- Identify tracks or genres with high valence and energy that are underplayed.
- Create a list of tracks to revisit.

#### **Playlist Recommendations**
- Use mood analysis to generate personalized playlists tailored to specific activities (e.g., study, workout, relaxation).

### Generating Insights
- Summarize key findings about listening habits and mood correlations.
- Visualize listening trends and mood distribution through graphs and charts.

---

## Expected Outcomes
By analyzing my Spotify data, I expect to:
1. Gain insights into my music preferences and how they vary by mood and time of day.
2. Understand the role of specific genres or artists in influencing my mood.
3. Receive mood-specific playlist recommendations for a better listening experience.

from typing import List, Dict
import random
from app.models import Influencer, StrategyInput

# Mock database of influencers
# In a real app, this would be a database or scraped from Instagram/TikTok APIs
MOCK_INFLUENCERS_DB = [
    {
        "id": 1,
        "name": "Teknoloji Gurusu",
        "handle": "@tech_guru_tr",
        "platform": "Instagram",
        "niche": ["teknoloji", "oyun", "yazılım", "gadgets"],
        "followers": 150000,
        "engagement_rate": 4.5,
        "bio": "En son teknoloji haberleri ve incelemeleri burada!",
        "sample_comments": ["Harika bir inceleme!", "Bu telefonu almalı mıyım?", "Fiyat performans kralı."]
    },
    {
        "id": 2,
        "name": "Moda İkonu Ayşe",
        "handle": "@ayse_style",
        "platform": "Instagram",
        "niche": ["moda", "giyim", "lifestyle", "makyaj"],
        "followers": 500000,
        "engagement_rate": 3.2,
        "bio": "Günlük stil önerileri ve makyaj tüyoları.",
        "sample_comments": ["Elbisen nereden?", "Çok yakışmış!", "Link gelir mi?"]
    },
    {
        "id": 3,
        "name": "Fit Yaşam",
        "handle": "@fityasam_tr",
        "platform": "TikTok",
        "niche": ["spor", "sağlık", "diyet", "fitness"],
        "followers": 300000,
        "engagement_rate": 6.8,
        "bio": "Sağlıklı yaşam için ipuçları. Harekete geç!",
        "sample_comments": ["Bu hareketi evde yapabilir miyim?", "Diyet programını paylaşır mısın?", "Motivation!"]
    },
    {
        "id": 4,
        "name": "Gezen Adam",
        "handle": "@travel_man_tr",
        "platform": "YouTube",
        "niche": ["seyahat", "tatil", "kamp", "doğa"],
        "followers": 100000,
        "engagement_rate": 5.1,
        "bio": "Dünyayı geziyorum, deneyimlerimi paylaşıyorum.",
        "sample_comments": ["Orası neresi?", "Vize istiyor mu?", "Manzara efsane."]
    },
    {
        "id": 5,
        "name": "Oyun Canavarı",
        "handle": "@game_monster",
        "platform": "Twitch",
        "niche": ["oyun", "espor", "teknoloji"],
        "followers": 80000,
        "engagement_rate": 8.5,
        "bio": "Her gün 20:00'da yayındayım. LoL ve Valorant.",
        "sample_comments": ["GG WP", "O nasıl vuruştu!", "Hangi mouse'u kullanıyorsun?"]
    },
     {
        "id": 6,
        "name": "Anne Bebek Dünyası",
        "handle": "@mom_baby_love",
        "platform": "Instagram",
        "niche": ["anne", "bebek", "aile", "eğitim"],
        "followers": 250000,
        "engagement_rate": 4.0,
        "bio": "Annelik serüvenim ve bebek bakımı önerileri.",
        "sample_comments": ["Hangi mamayı kullanıyorsun?", "Çok tatlı maşallah", "Uyku tulumu önerisi lazım."]
    },
]

def analyze_strategy_and_match(strategy: StrategyInput) -> List[Influencer]:
    """
    Analyzes the brand strategy input and matches it with suitable influencers.
    In a real app, this would use NLP to analyze the target audience and product description.
    Here, we do simple keyword matching.
    """
    
    input_text = f"{strategy.product_type} {strategy.target_audience} {strategy.description or ''}".lower()
    
    matched_influencers = []
    
    for inf_data in MOCK_INFLUENCERS_DB:
        score = 0
        # Basic scoring logic
        niche_matches = sum(1 for niche in inf_data["niche"] if niche.lower() in input_text)
        
        if niche_matches > 0:
            score += niche_matches * 10
            
        # Platform bias (just for variety)
        # If input mentions 'video' or 'uzun', prefer Youtube, etc.
        if "video" in input_text and inf_data["platform"] in ["YouTube", "TikTok"]:
            score += 5
            
        if "foto" in input_text and inf_data["platform"] == "Instagram":
            score += 5

        # If score > 0, we consider it a match
        if score > 0:
            inf = Influencer(**inf_data)
            inf.match_score = score
            matched_influencers.append(inf)
    
    # Sort by score descending
    matched_influencers.sort(key=lambda x: x.match_score, reverse=True)
    
    # If no matches found, return generic high-engagement influencers
    if not matched_influencers:
         # Fallback: Top 3 by engagement rate
         sorted_db = sorted(MOCK_INFLUENCERS_DB, key=lambda x: x['engagement_rate'], reverse=True)
         for inf_data in sorted_db[:3]:
             inf = Influencer(**inf_data)
             inf.match_score = 0.1 # Low score indicating fallback
             matched_influencers.append(inf)

    return matched_influencers

def mock_scrape_update(influencer_id: int):
    """
    Simulates fetching updated data from the internet.
    """
    # In a real app, this would trigger a scraper or API call
    # Here just randomize followers slightly to show 'live' feeling
    for inf in MOCK_INFLUENCERS_DB:
        if inf['id'] == influencer_id:
            change = random.randint(-10, 10)
            inf['followers'] += change
            return inf
    return None

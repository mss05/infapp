from pydantic import BaseModel
from typing import List, Optional

class Influencer(BaseModel):
    id: int
    name: str
    handle: str
    platform: str
    niche: List[str]
    followers: int
    engagement_rate: float
    bio: str
    sample_comments: List[str]
    match_score: Optional[float] = 0.0

class StrategyInput(BaseModel):
    brand_name: str
    product_type: str
    target_audience: str
    description: Optional[str] = None

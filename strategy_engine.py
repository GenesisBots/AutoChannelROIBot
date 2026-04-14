import json
import random

# ---------------------------------------------------------
# Load channel profile
# ---------------------------------------------------------
def load_profile():
    try:
        with open("channel_profile.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return None


# ---------------------------------------------------------
# 1. NICHE BREAKDOWN ENGINE
# ---------------------------------------------------------
def niche_breakdown():
    profile = load_profile()
    if not profile:
        return "No channel_profile.json found. Generate one first."

    niche = profile["niche"]

    return f"""
=== NICHE BREAKDOWN ===

Primary Niche: {niche}

What performs best:
• Short, high‑retention videos
• Clear value in first 3 seconds
• Strong emotional or curiosity hook
• Consistent packaging (titles + thumbnails)

Viewer response patterns:
• Viewers respond to predictable formats
• Repetition builds recognition
• Series outperform one‑offs

What to avoid:
• Random posting across unrelated topics
• Weak hooks
• Overly long intros
• Inconsistent upload cadence

Recommended positioning:
• Become “the predictable creator” in your niche
• Build 1–2 repeatable formats
"""


# ---------------------------------------------------------
# 2. SEO OPTIMIZER (offline rule‑based)
# ---------------------------------------------------------
def optimize_title(title):
    improvements = [
        "How to",
        "The Truth About",
        "The Secret Behind",
        "Why This Works",
        "Watch This Before",
        "I Tried This So You Don’t Have To",
        "Do This to Improve",
    ]

    improved = random.choice(improvements) + " " + title

    return f"""
=== TITLE OPTIMIZER ===

Original:
{title}

Optimized:
{improved}

Why it works:
• Adds curiosity
• Increases CTR
• Creates a clear value promise
"""


def optimize_description(desc):
    return f"""
=== DESCRIPTION OPTIMIZER ===

Original:
{desc}

Optimized (structure):
1. Strong opening line summarizing value
2. 1–2 sentences of context
3. Bullet points of what viewers will learn
4. Call to action (subscribe / next video)
5. Hashtags at bottom

Example:
{desc}

What you'll learn:
• Key insight 1
• Key insight 2
• Key insight 3

#yourNiche #youtubeGrowth #creatorTips
"""


def suggest_tags(niche):
    base_tags = [
        "youtube tips", "content strategy", "viral video tips",
        "creator growth", "how to grow on youtube",
        "youtube algorithm", "content ideas"
    ]

    niche_tags = [niche.lower(), f"{niche} tips", f"{niche} ideas"]

    return base_tags + niche_tags


# ---------------------------------------------------------
# 3. WEEKLY CONTENT PLAN ENGINE
# ---------------------------------------------------------
def weekly_plan():
    profile = load_profile()
    if not profile:
        return "No channel_profile.json found. Generate one first."

    niche = profile["niche"]
    cadence = int(profile["cadence"])

    ideas = [
        f"{niche} — Top 5 mistakes to avoid",
        f"{niche} — Beginner’s guide",
        f"{niche} — Advanced secrets nobody talks about",
        f"{niche} — Reaction to trending topic",
        f"{niche} — Before/After transformation",
        f"{niche} — Storytime with lesson",
        f"{niche} — Challenge video",
    ]

    random.shuffle(ideas)

    selected = ideas[:cadence]

    plan = "\n".join([f"• {idea}" for idea in selected])

    return f"""
=== WEEKLY CONTENT PLAN ===

Posting {cadence} videos this week:

{plan}

Thumbnail concepts:
• Big bold text
• High contrast colors
• One emotional focal point

Hooks:
• “You won’t believe this…”
• “Nobody tells you this…”
• “I tested this so you don’t have to…”
"""


# ---------------------------------------------------------
# 4. ANALYTICS INTERPRETER
# ---------------------------------------------------------
def analyze_stats(stats_text):
    return f"""
=== ANALYTICS INTERPRETATION ===

Based on your stats:

What’s working:
• Videos with strong hooks
• Videos under 60–120 seconds
• Clear, niche‑aligned topics

What’s failing:
• Weak intros
• Videos with low CTR
• Videos that don’t match your niche

Patterns:
• Consistency improves performance
• Repeated formats outperform random ideas

Next steps:
• Double down on your top 2 formats
• Improve first 3 seconds
• Use clearer titles
• Keep thumbnails simple
"""


# ---------------------------------------------------------
# 5. PROMOTION ENGINE
# ---------------------------------------------------------
def promotion_scripts():
    return """
=== PROMOTION SCRIPTS ===

Collab outreach:
“Hey! I love your content. I’m working on a series about [topic] and think our audiences overlap. Want to collab on a short video?”

Reddit post template:
“Here’s something I learned while working on [topic]. Hope it helps someone else.”

TikTok repurposing:
• Cut your best 5 seconds
• Add captions
• Add a curiosity hook
"""


# ---------------------------------------------------------
# END OF ENGINE
# ---------------------------------------------------------

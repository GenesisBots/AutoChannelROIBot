import json

def ask(q, default=None):
    print("\n" + q)
    if default:
        print(f"[Press Enter for default: {default}]")
    ans = input("> ").strip()
    return ans if ans else default

def run_bot():
    print("AutoChannelROIbot — YouTube ROI Strategy Assistant")
    print("This bot helps creators optimize content, packaging, and growth strategy.\n")

    niche = ask("What niche is this channel?", "AI Dogs / Travel / Motivation")
    goals = ask("What is the creator's main goal?", "More views, more subs, better retention")
    cadence = ask("How many videos per week?", "3")
    pain = ask("What is the creator struggling with?", "Consistency and packaging")

    profile = {
        "niche": niche,
        "goals": goals,
        "cadence": cadence,
        "pain_points": pain
    }

    with open("channel_profile.json", "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)

    print("\nProfile saved to channel_profile.json")
    print("Use this file to generate weekly plans, SEO optimization, and analytics reviews.")

def run_bot_interactive(niche, goals, cadence, pain):
    """Used by the UI — no input(), no prints."""
    profile = {
        "niche": niche,
        "goals": goals,
        "cadence": cadence,
        "pain_points": pain
    }

    with open("channel_profile.json", "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)

    return profile

if __name__ == "__main__":
    run_bot()

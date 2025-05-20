import random

def generate_title_and_description(story_text):
    emojis = ["🦁", "🐜", "🐘", "🐦", "🐻", "🌈", "🌟", "📚", "🎉"]
    title_subjects = ["The Brave Parrot", "The Selfish Lion", "The Clever Fox", "The Worker Ant"]

    title = random.choice(title_subjects) + " " + random.choice(emojis) + random.choice(emojis)
    description = (
        f"{title} is a short animated kids story teaching values like teamwork, honesty, and kindness.\n\n"
        "🎬 Watch more kids stories on our channel!\n\n"
        "#kids #stories #animation"
    )
    return title, description

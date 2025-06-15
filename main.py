from ai import call_gpt

def welcome():
    print("\n" * 2)
    print("✨ tbh I was trying to make something different but I’m just so lost rn.")
    print("💭 maybe that’s why nothing is working out.")
    print("so I just hope this helps me — and maybe you too.")
    print()
    print("🔁 being lost is so overwhelming, just a loop right?")
    print("but this is gonna be different for everyone —")
    print("how one figures things out... feels personal.")
    print()
    print("🌱 hopefully this space becomes a little more human, a little more *you*.")
    print("-" * 10 + " 💫 WELCOME TO LOST ME 💫 " + "-" * 10)
    print()
    input("👉 Press ENTER when you're ready. No rush. ")
    print("\n" * 2)

    print("🤝 I don’t want to intrude on your life, but to respond according to your needs,")
    print("I'll need to understand you a little better.")
    print("No pressure — stop whenever it feels like too much.\n")
    input("🕊️ Press ENTER to begin\n")

    # Updated prompt without assuming lostness, with warm analysis and suggestions
    system_prompt = (
        "You are a compassionate, trauma-informed psychologist and life mentor.\n\n"
        "You’ve received honest responses to 11 deeply personal and introspective questions. "
        "Your job is to gently understand what this person may be experiencing emotionally, cognitively, or behaviorally — "
        "but without assuming anything.\n\n"
        "Please:\n"
        "1. Identify themes or patterns based on their answers (if any).\n"
        "2. Reflect back their possible emotional state in a warm and grounded tone.\n"
        "3. Offer supportive insights that can help them move toward clarity, purpose, or peace.\n"
        "4. If appropriate, suggest a few resources like books, habits, or films to explore further.\n\n"
        "I would like for yut o start nicely with empathy,and the analytics should be valid and detailed enough, but no hallucination just science for the user to understnd onesef, and don't refer to as user,"
        "Use this format:\n"
        "---\n"
        "**What Stands Out**\n"
        "• Point 1\n"
        "• Point 2\n"
        "• Point 3\n"
        "...\n\n"
        "**Reflective Support**\n"
        "Write a short compassionate paragraph based on their current emotional state.\n\n"
        "**You Might Find These Helpful**\n"
        "📖 Books:\n"
        "• ...\n"
        "🎬 Films:\n"
        "• ...\n"
        "🌱 Habits:\n"
        "• ...\n"
        "---"
    )

    questions = {
        1: "What’s been feeling most confusing or heavy in your life right now?",
        2: "Do you feel like you're searching for something? If yes, what do you think it is?",
        3: "When was the last time you felt a sense of direction or clarity?",
        4: "Do you feel emotionally connected to the people around you?",
        5: "Were you ever made to feel like your emotions were 'too much' or invalid?",
        6: "Is there a belief you carry about yourself that feels heavy or painful?",
        7: "Do you often feel pressure to be someone you’re not?",
        8: "What do you long for most, even if it feels unrealistic right now?",
        9: "When you were a child, what made you feel safe or joyful?",
        10: "If your feelings could speak freely, what do you think they’d say?",
        11: "Is there anything else you'd like to say or express?"
    }

    answers = {}
    for i in range(1, 12):
        print(f"\n{i}. {questions[i]}")
        user_input = input("💬 > ")
        answers[i] = user_input

    # Combine all Q&A for GPT prompt
    combined = ""
    for i in range(1, 12):
        combined += f"\nQ{i}: {questions[i]}\nA{i}: {answers[i]}\n"

    print("\n⏳ Processing your self-reflection... please wait.\n")
    analysis = call_gpt(system_prompt + combined)
    print(analysis)

    # Start a gentle chat loop for user to talk more or ask questions
    print("\n🤖 You can now continue chatting or reflecting here. Type 'exit' or 'quit' to end.")
    chat_context = system_prompt + combined + "\n\n" + analysis + "\nUser:"

    while True:
        user_input = input("\nYou: ")
        if user_input.strip().lower() in ("exit", "quit"):
            break

        chat_context += f"\nUser: {user_input}\nAssistant:"
        response = call_gpt(chat_context)
        print(f"\nAssistant: {response}")

        chat_context += response  # append assistant reply to keep context

    # Ending message
    print("\n✨ Thank you for sharing your journey here. Remember, it's okay to take things one step at a time.")
    print("Be gentle with yourself. Growth often happens in small, quiet moments.")
    print("Whenever you feel ready, this space is always here for you.\n")

def main():
    welcome()

if __name__ == "__main__":
    main()

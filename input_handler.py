import msvcrt

def handle_input():
    print("📧 Email Management Console")
    print("=" * 30)
    print("Choose an option:")
    print("  [s] ➜ Generate 'unique_senders.json'")
    print("  [d] ➜ Delete mails based on query")
    print("  [l] ➜ Count total mails based on query")
    print("  [a] ➜ Delete all mails")
    print("  [p] ➜ Show first 10 mails")
    print("=" * 30)
    
    char = msvcrt.getch().decode('utf-8').lower()  # Added `.lower()` to handle uppercase too
    print(f"\n✅ You entered: '{char}'")

    return char

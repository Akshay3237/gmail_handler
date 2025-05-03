from services import get_unique_senders,save_senders_to_file,delete_emails_by_sender_keyword,delete_all_mails,list_emails,total_number_of_mail
from get_mail_service import get_gmail_service
def service_call(input_character):
    service=get_gmail_service()
    print("\n📬 Mail Service Operation Selected:\n")
    match input_character:
        case 's':
            print("📝 Generating 'unique_senders.json'...")
            senders_list=get_unique_senders(service)
            save_senders_to_file(senders_list)
        case 'd':
            print("🗑️ Deleting mails based on query...")
            print('Enter keyword')
            keyword = input("Please enter keyword: ")
            print("You entered:", keyword)
            delete_emails_by_sender_keyword(service, keyword)
        case 'l':
            print("📊 Fetching total number of mails based on query...")
            total_number_of_mail(service,"")
        case 'a':
            print("⚠️ Deleting all mails...")
            delete_all_mails(service)
        case 'p':
            print("📨 Showing the first 10 mails...")
            list_emails(service)
        case _:
            print("❌ Invalid input. Please try again.")

    print("\n✅ Thanks for using the Mail Service!\n")

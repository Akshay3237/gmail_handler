
import base64
import email
import os
def get_unique_senders(service):
    try:
        sender_set = set()
        next_page_token = None

        print("Fetching all emails to extract unique senders...")

        while True:
            response = service.users().messages().list(
                userId='me',
                labelIds=['INBOX'],
                pageToken=next_page_token
            ).execute()

            messages = response.get('messages', [])
            if not messages:
                break

            for msg in messages:
                msg_id = msg['id']
                msg_detail = service.users().messages().get(
                    userId='me',
                    id=msg_id,
                    format='metadata',
                    metadataHeaders=['From']
                ).execute()

                headers = msg_detail.get('payload', {}).get('headers', [])
                for header in headers:
                    if header['name'] == 'From':
                        sender_set.add(header['value'])

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        print(f"\n✅ Unique senders found ({len(sender_set)}):")
        # for sender in sorted(sender_set):
        #     print(sender)

        return list(sender_set)

    except HttpError as error:
        print(f"An error occurred: {error}")
        return []



def save_senders_to_file(sender_list, filename= 'unique_senders.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(sender_list, f, indent=4, ensure_ascii=False)
        print(f"\n📁 Successfully saved {len(sender_list)} unique senders to '{filename}'")
    except Exception as e:
        print(f"❌ Error saving to file: {e}")



def delete_emails_by_sender_keyword(service, keyword):
    """Delete emails from Gmail where the sender's name or email contains the given keyword."""
    try:
        print(f"\n🔍 Searching for messages with sender containing '{keyword}'...")

        query = f'from:{keyword}'
        next_page_token = None
        total_deleted = 0

        while True:
            response = service.users().messages().list(
                userId='me',
                q=query,
                pageToken=next_page_token
            ).execute()

            messages = response.get('messages', [])
            if not messages:
                break

            for msg in messages:
                msg_id = msg['id']
                # Optional: check headers again if needed
                service.users().messages().delete(userId='me', id=msg_id).execute()
                total_deleted += 1

            print(f"✅ Deleted {len(messages)} messages in this batch...")
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        print(f"\n🗑️ Done! Total messages deleted: {total_deleted}")

    except Exception as e:
        print(f"❌ Error while deleting: {e}")


def delete_all_mails(service):
    """Delete emails from Gmail."""
    try:
        print(f"\n🔍 Searching for messages ")

        
        next_page_token = None
        total_deleted = 0

        while True:
            response = service.users().messages().list(
                userId='me',
                pageToken=next_page_token
            ).execute()

            messages = response.get('messages', [])
            if not messages:
                break

            for msg in messages:
                msg_id = msg['id']
                # Optional: check headers again if needed
                service.users().messages().delete(userId='me', id=msg_id).execute()
                total_deleted += 1

            print(f"✅ Deleted {len(messages)} messages in this batch...")
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        print(f"\n🗑️ Done! Total messages deleted: {total_deleted}")

    except Exception as e:
        print(f"❌ Error while deleting: {e}")


def list_emails(service):
    try:
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="").execute()
        messages = results.get('messages', [])

        if not messages:
            print('No messages found.')
        else:
            print('Messages:')
            for message in messages[:10]:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                headers = msg.get('payload', {}).get('headers', [])
                from_header = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
                print(f"From: {from_header}")
                print(f"Snippet: {msg.get('snippet')}")
                print('-' * 50)

    except HttpError as error:
        print(f'An error occurred: {error}')

def total_number_of_mail(service, keyword):
    """
    Count and optionally delete all emails from a specific sender based on a keyword.

    Parameters:
    - service: Authorized Gmail API service instance.
    - keyword: The sender's email or part of it to filter messages.
    """
    query = f'from:{keyword}'
    next_page_token = None
    total_found = 0

    while True:
        response = service.users().messages().list(
            userId='me',
            q=query,
            pageToken=next_page_token
        ).execute()

        messages = response.get('messages', [])
        if not messages:
            break

        for msg in messages:
            msg_id = msg['id']
            # Optional: Remove the line below if you don't want to delete
            service.users().messages().delete(userId='me', id=msg_id).execute()
            total_found += 1

        print(f"✅ Counted {len(messages)} messages in this batch...")
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    print(f"\n✅ Done! Total messages counted (and deleted): {total_found}")

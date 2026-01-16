emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

spam_emails = emails_received & spam_list  # Intersection
# Alternatywnie: emails_received.intersection(spam_list)

print("Spam emails:", spam_emails)
#! python3
import re, pyperclip

# Create a regex for phone numbers
phone_regex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(((\d\d\d) | (\(\d\d\d\)))?      # area code (optional)
(\s|- )                        # first separator
\d\d\d                        # first 3 digits
-                            # separator
\d\d\d                      # last 4 digits
(((ext(\.)?\s)|x)           # extension optional
 (\d{2,5}))?)
''', re.VERBOSE)
# Create a regex for email addresses
email_regex = re.compile(r'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''')
# get the text off the clipboard
text =  pyperclip.paste()
# Extract the email /phone from this text
extracted_phone =  phone_regex.findall(text)
all_phone_numbers = []
for phone_number in extracted_phone:
  all_phone_numbers.append(phone_number[0])
extracted_email = email_regex.findall(text)
print(extracted_email)
print(all_phone_numbers)
# Copy the extracted email/phone to the clipboard
results = '\n'.join(extracted_email) + '\n' + '\n'.join(all_phone_numbers)
print(results)
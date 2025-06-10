def can_trust_message(message):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    message_letters = set(message.replace(' ', ''))
    return alphabet.issubset(message_letters)

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
print("Input your email name before @: ")
email = input()

print("Email level 1:\n\n\n\n\n\n\n\n\n")

level_1_emails_variations_given = 0

def add_letter_at_position(string, added_letter, pos):
    return string[:pos] + added_letter + string[pos:]

for i in range(len(email)):
    if i > 0: # no .amogusop
        email_new = email
        string_v_1 = add_letter_at_position(email_new, ".", i)
        #print(email_new)
        print(string_v_1)
        level_1_emails_variations_given += 1

print("Email level 2:\n\n\n\n\n\n\n\n\n")

level_2_emails_variations_given = 0

for i in range(len(email)):
    if i > 0: # no .amogusop
        email_new = email
        string_v_1 = add_letter_at_position(email_new, ".", i)
        #print(email_new)
        #print(string_v_1)
        for v in range(len(email)):
            if v > 0 and v - i != 0 and i - v != 0 and v - i != 1 and i - v != -1:  # no .amogusop
                string_v_2 = add_letter_at_position(string_v_1, ".", v)
                #print(email_new)
                print(string_v_2)
                #print(str(v - i) + " " + str(i - v))
                level_2_emails_variations_given += 1

print("Email level 3:\n\n\n\n\n\n\n\n\n")

level_3_emails_variations_given = 0

for i in range(len(email)):
    if i > 0: # no .amogusop
        email_new = email
        string_v_1 = add_letter_at_position(email_new, ".", i)
        #print(email_new)
        #print(string_v_1)
        for v in range(len(email)):
            if v > 0 and v - i != 0 and i - v != 0 and v - i != 1 and i - v != -1:  # no .amogusop
                string_v_2 = add_letter_at_position(string_v_1, ".", v)
                #print(email_new)
                #print(string_v_2)
                #print(str(v - i) + " " + str(i - v))
                for b in range(len(email)): # b = v; i = v
                    if b > 0 and b - v != 0 and v - b != 0 and b - v != 1 and v - b != -1:  # no .amogusop
                        #if b > 0 and b - i != 0 and i - b != 0 and b - i != 1 and i - b != -1:
                        if b > 0 and b - i != 0 and i - b != 0 and b - i != 1 and i - b != -1 and b - i != 2 and i - b != -2:
                            string_v_3 = add_letter_at_position(string_v_2, ".", b)
                            #print(email_new)
                            #print(string_v_1)
                            #print(string_v_2)
                            print(string_v_3)
                            #print(str(b - v) + " " + str(v - b))
                            #print(str(b - i) + " " + str(i - b))
                            #print(str(i) + " " + str(v) + " " + str(b))
                            level_3_emails_variations_given += 1

print("Level 1 emails variations given: " + str(level_1_emails_variations_given))
print("Level 2 emails variations given: " + str(level_2_emails_variations_given))
print("Level 3 emails variations given: " + str(level_3_emails_variations_given))
print("All emails variations given: " + str(level_1_emails_variations_given + level_2_emails_variations_given + level_3_emails_variations_given))

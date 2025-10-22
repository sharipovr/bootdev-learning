def filter_messages(messages):
    filtered_messages = []
    dang_counter = []

    for msg in messages:
        words = msg.split()
        msg_good_words = []
        msg_dangs = []
        for word in words:
            if word == "dang":
                msg_dangs.append(word)
            else:
                msg_good_words.append(word)
        msg_filtered = " ".join(msg_good_words)
        filtered_messages.append(msg_filtered)
        dang_counter.append(len(msg_dangs))

    return filtered_messages, dang_counter
        

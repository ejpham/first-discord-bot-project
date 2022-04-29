Friday, April 29, 2022 at 03:52.

I am extremely sleep deprived from finals but I cannot sleep.
My mind decided to wander and look for ways to improve my coding knowledge,
since I just revamped my resume.

Here I am.

Let's make my first discord bot.

    on_ready():
        when logged in, print to console
    
    on_message(message):
        if message is sent from bot itself, return
        if message contains 'bing', reply 'bong'
        if message contains forms of 'ok', react with custom 'ok' emoji
        if message starts with 'o phi o phi', reply 'g!'
    
    on_message_delete(message):
        if message was sent in #logs channel, return
        prepare embed message with content of deleted message
        prepare multiple embed messages for every image
        add fields for every file
        send message to #logs

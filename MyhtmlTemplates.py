css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.8rem;
    margin-bottom: 1.2rem;
    display: flex;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}
.chat-message.user {
    background-color: #394867;
}
.chat-message.bot {
    background-color: #526D82;
}
.chat-message .avatar {
    width: 15%;
}
.chat-message .avatar img {
    max-width: 64px;
    max-height: 64px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #DDE6ED;
}
.chat-message .message {
    width: 85%;
    padding: 0 1.2rem;
    color: #E6F1FF;
    font-family: Arial, sans-serif;
    font-size: 1rem;
    line-height: 1.5;
}
</style>
'''
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.imgur.com/JTA1txV.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''

<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.imgur.com/ku8irFY.jpeg" alt="User Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
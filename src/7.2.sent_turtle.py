class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, message_body, urgent=False):
        """Send a message to a recipient.
        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param title: the title of the message
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1

        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'unread': True,
            'title': title,
            'urgent': urgent
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user, n=0):
        """
            Reads messages from a user's inbox.

            Parameters:
            - user (str): The username whose inbox will be accessed.
            - n (int): Number of recent messages to return (0 returns all).

            Marks returned messages as read (`unread = False`).

            Returns:
            - List of message dictionaries.
        """
        if not user in self.boxes:
            raise KeyError("User does not exist.")
        user_box = self.boxes[user]
        if n == 0 or n == len(user_box):
            for message in user_box:
                message['unread'] = False
            return user_box
        msg = user_box[:n+1]
        for message in user_box[:n+1]:
            message['unread'] = False
        return msg

    def search_inbox(self, username, word):
        """
            Searches for a keyword in a user's inbox messages.

            Parameters:
            - username (str): The user's name.
            - word (str): The keyword to search for in message bodies or titles.

            Returns:
            - List of messages that contain the keyword.
            Prints an error if the user does not exist.
        """
        if not username in self.boxes:
            print("User does not exist.")
            return []

        word = word.lower()
        return [msg for msg in self.read_inbox(username) if word in msg['body'].lower() or word in msg['title'].lower()]
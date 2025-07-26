import React, { useState } from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (text) => {
    setLoading(true);
    setMessages((prev) => [...prev, { text, sender: 'user' }]);

    try {
      const res = await fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text }),
      });
      const data = await res.json();
      setMessages((prev) => [...prev, { text: data.response, sender: 'bot' }]);
    } catch (error) {
      setMessages((prev) => [...prev, { text: "Error getting response.", sender: 'bot' }]);
    }

    setLoading(false);
  };

  return (
    <div>
      <MessageList messages={messages} />
      {loading && <p>Loading...</p>}
      <UserInput onSend={sendMessage} />
    </div>
  );
};

export default ChatWindow;

import React from 'react';
import Message from './Message';

const MessageList = ({ messages }) => (
  <div>
    {messages.map((msg, idx) => (
      <Message key={idx} message={msg} />
    ))}
  </div>
);

export default MessageList;

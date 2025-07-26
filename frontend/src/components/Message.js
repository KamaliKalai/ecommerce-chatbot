import React from 'react';

const Message = ({ message }) => {
  const style = {
    backgroundColor: message.sender === 'user' ? '#DCF8C6' : '#ECECEC',
    padding: '8px',
    margin: '5px',
    borderRadius: '8px',
    maxWidth: '60%',
    alignSelf: message.sender === 'user' ? 'flex-end' : 'flex-start',
  };

  return <div style={style}>{message.text}</div>;
};

export default Message;

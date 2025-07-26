

import React from "react"; import MessageList from "./MessageList"; import UserInput from "./UserInput"; import ConversationPanel from "./ConversationPanel";

const ChatWindow = ({ messages, onSend, loading, conversations, onSelect }) => { return ( <div className="chat-window"> <ConversationPanel conversations={conversations} onSelect={onSelect} /> <div className="chat-box"> <MessageList messages={messages} /> <UserInput onSend={onSend} loading={loading} /> </div> </div> ); };

export default ChatWindow;

File: frontend/src/components/MessageList.jsx

import React from "react"; import Message from "./Message";

const MessageList = ({ messages }) => (

  <div className="message-list">
    {messages.map((msg, index) => (
      <Message key={index} {...msg} />
    ))}
  </div>
);export default MessageList;

File: frontend/src/components/Message.jsx

import React from "react";

const Message = ({ role, content }) => (

  <div className={message ${role === "user" ? "user-message" : "ai-message"}}>
    <p>{content}</p>
  </div>
);export default Message;











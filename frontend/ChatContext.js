

import React, { createContext, useContext, useState } from "react";

const ChatContext = createContext();

export const ChatProvider = ({ children }) => { const [messages, setMessages] = useState([]); const [conversations, setConversations] = useState([]); const [loading, setLoading] = useState(false);

const value = { messages, setMessages, conversations, setConversations, loading, setLoading, };

return <ChatContext.Provider value={value}>{children}</ChatContext.Provider>; };

export const useChat = () => useContext(ChatContext);
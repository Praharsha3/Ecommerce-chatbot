

import React from "react";

const ConversationPanel = ({ conversations, onSelect }) => (

  <div className="conversation-panel">
    <h3>Past Conversations</h3>
    <ul>
      {conversations.map((conv) => (
        <li key={conv.id} onClick={() => onSelect(conv.id)}>
          {new Date(conv.created_at).toLocaleString()}
        </li>
      ))}
    </ul>
  </div>
);export default ConversationPanel;


import React, { useState } from "react";

const UserInput = ({ onSend, loading }) => { const [input, setInput] = useState("");

const handleSubmit = (e) => { e.preventDefault(); if (!input.trim()) return; onSend(input); setInput(""); };

return ( <form onSubmit={handleSubmit} className="user-input"> <input type="text" value={input} onChange={(e) => setInput(e.target.value)} placeholder="Type your message..." /> <button type="submit" disabled={loading}> {loading ? "Sending..." : "Send"} </button> </form> ); };

export default UserInput;
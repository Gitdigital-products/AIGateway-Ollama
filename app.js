// app.js
// Simple Node client for AI Gateway (Ollama)

import fetch from 'node-fetch'; // For Node 18+ you can use global fetch instead

const GATEWAY_URL = process.env.GATEWAY_URL || 'http://localhost:8000/v1/chat/completions';
const API_KEY = process.env.API_KEY || 'dev-key-123'; // match your .env / gateway config

async function runChat(prompt) {
  try {
    const response = await fetch(GATEWAY_URL, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        messages: [
          {
            role: 'user',
            content: prompt || 'Review this function',
          },
        ],
      }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Gateway error:', response.status, errorText);
      process.exit(1);
    }

    const data = await response.json();
    console.log('Gateway response:');
    console.dir(data, { depth: null });
  } catch (err) {
    console.error('Request failed:', err);
  }
}

// Allow prompt via CLI arg, otherwise default
const userPrompt = process.argv.slice(2).join(' ');
runChat(userPrompt);

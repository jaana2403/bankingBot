
        const chatbotContainer = document.getElementById("chatbot");
        const chatbotBody = document.getElementById("chatbotBody");
        const chatbotInput = document.getElementById("chatbotInput");
  
        function toggleChatbot() {
          chatbotContainer.style.display = chatbotContainer.style.display === "flex" ? "none" : "flex";
        }
  
        function sendMessage() {
          const userMessage = chatbotInput.value.trim();
          if (userMessage === "") return;
  
          // Add user message to chat
          const userChat = document.createElement("div");
          userChat.className = "chat-message user";
          userChat.textContent = userMessage;
          chatbotBody.appendChild(userChat);
  
          // Scroll to the bottom
          chatbotBody.scrollTop = chatbotBody.scrollHeight;
  
          chatbotInput.value = "";
  
          // Add bot response
          setTimeout(() => {
            const botChat = document.createElement("div");
            botChat.className = "chat-message bot";
            botChat.textContent = getBotResponse(userMessage);
            chatbotBody.appendChild(botChat);
            chatbotBody.scrollTop = chatbotBody.scrollHeight;
          }, 500);
        }
  
        function getBotResponse(message) {
          // Simple responses (can be expanded for sophistication)
          if (message.toLowerCase().includes("hello")) {
            return "Hi! How can I assist you today?";
          } else if (message.toLowerCase().includes("loan")) {
            return "We offer various loan options. Please visit our Loans section for more details.";
          } else if (message.toLowerCase().includes("account")) {
            return "You can manage your account easily via our app or website.";
          } else {
            return "I'm here to help! Could you please clarify your question?";
          }
        }

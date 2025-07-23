'use client'

import { useState, useRef, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Send, AlertTriangle, Book, Phone } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Badge } from '@/components/ui/badge'
import { conversationsData, type Message } from '@/data/conversations'
import useSWR from 'swr'

const quickReplies = [
  'Tell me about your services',
  'I need prayer',
  'How can I give?',
  'I want to volunteer',
]

const sensitiveKeywords = ['depressed', 'suicide', 'hurt', 'crisis', 'emergency']

export function ChatWindow() {
  const [selectedConversation, setSelectedConversation] = useState(conversationsData[0])
  const [newMessage, setNewMessage] = useState('')
  const [messages, setMessages] = useState<Message[]>(selectedConversation.messages)
  const [isTyping, setIsTyping] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const { data: conversations } = useSWR('/api/inbound/conversations', {
    fallbackData: conversationsData,
  })

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const containsSensitiveContent = (text: string) => {
    return sensitiveKeywords.some(keyword => 
      text.toLowerCase().includes(keyword.toLowerCase())
    )
  }

  const handleSendMessage = async () => {
    if (!newMessage.trim()) return

    const userMessage: Message = {
      id: Date.now().toString(),
      content: newMessage,
      sender: 'user',
      timestamp: new Date().toISOString(),
    }

    setMessages(prev => [...prev, userMessage])
    setNewMessage('')
    setIsTyping(true)

    try {
      // Try to call the backend API first
      const response = await fetch('http://localhost:8000/api/v1/inbound/process', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: newMessage,
          user_id: 'anonymous',
          source: 'website',
          language: 'en'
        }),
      })

      if (response.ok) {
        const data = await response.json()

        const aiResponse: Message = {
          id: (Date.now() + 1).toString(),
          content: data.response,
          sender: 'ai',
          timestamp: new Date().toISOString(),
          needsEscalation: data.needs_escalation,
          faqMatched: data.faq_matched
        }

        setMessages(prev => [...prev, aiResponse])
        setIsTyping(false)
        return
      } else {
        throw new Error('API response not ok')
      }
    } catch (error) {
      console.warn('Backend API not available, using fallback response:', error)
      
      // Fallback to hardcoded response when API is not available
      setTimeout(() => {
        const aiResponse: Message = {
          id: (Date.now() + 1).toString(),
          content: `Thank you for your message. I understand you're reaching out about "${newMessage}". Let me provide you with some guidance and support. "Cast all your anxiety on him because he cares for you." - 1 Peter 5:7`,
          sender: 'ai',
          timestamp: new Date().toISOString(),
          scripture: '1 Peter 5:7',
          needsEscalation: containsSensitiveContent(newMessage),
        }

        setMessages(prev => [...prev, aiResponse])
        setIsTyping(false)
      }, 2000)
    }
  }

  const handleQuickReply = (reply: string) => {
    setNewMessage(reply)
  }

  const handleEscalate = () => {
    // Handle escalation to human pastor
    alert('Escalating to human pastor. They will be notified immediately.')
  }

  return (
    <div className="max-w-7xl mx-auto h-full flex">
      {/* Conversations List */}
      <div className="w-1/3 bg-white rounded-l-xl shadow-lg border-r border-gray-200">
        <div className="p-6 border-b border-gray-200">
          <h2 className="font-playfair text-xl font-bold text-ministry-navy">
            Conversations
          </h2>
          <p className="text-sm text-gray-600">Recent ministry interactions</p>
        </div>
        
        <div className="overflow-y-auto h-full">
          {conversations.map((conversation) => (
            <motion.div
              key={conversation.id}
              whileHover={{ backgroundColor: '#F8F9FA' }}
              onClick={() => {
                setSelectedConversation(conversation)
                setMessages(conversation.messages)
              }}
              className={`p-4 cursor-pointer border-b border-gray-100 ${
                selectedConversation.id === conversation.id ? 'bg-ministry-gray' : ''
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <h3 className="font-semibold text-ministry-navy">
                  {conversation.name}
                </h3>
                <Badge variant={conversation.status === 'active' ? 'default' : 'secondary'}>
                  {conversation.status}
                </Badge>
              </div>
              <p className="text-sm text-gray-600 truncate">
                {conversation.lastMessage}
              </p>
              <p className="text-xs text-gray-400 mt-1">
                {new Date(conversation.timestamp).toLocaleDateString()}
              </p>
            </motion.div>
          ))}
        </div>
      </div>

      {/* Chat Area */}
      <div className="flex-1 bg-white rounded-r-xl shadow-lg flex flex-col">
        {/* Chat Header */}
        <div className="p-6 border-b border-gray-200">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="font-semibold text-ministry-navy">
                {selectedConversation.name}
              </h2>
              <p className="text-sm text-gray-600">{selectedConversation.email}</p>
            </div>
            <div className="flex space-x-2">
              <Button variant="outline" size="sm">
                <Book size={16} className="mr-2" />
                Scripture
              </Button>
              <Button variant="outline" size="sm" onClick={handleEscalate}>
                <Phone size={16} className="mr-2" />
                Escalate
              </Button>
            </div>
          </div>
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-6 space-y-4">
          <AnimatePresence>
            {messages.map((message) => (
              <motion.div
                key={message.id}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
                className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div className={`max-w-xs lg:max-w-md ${
                  message.sender === 'user' ? 'chat-bubble-user' : 'chat-bubble-ai'
                }`}>
                  <p className="whitespace-pre-wrap">{message.content}</p>
                  
                  {message.scripture && (
                    <div className="mt-3 p-2 bg-white bg-opacity-20 rounded-lg">
                      <p className="text-xs font-medium opacity-75">Scripture Reference:</p>
                      <p className="text-sm">{message.scripture}</p>
                    </div>
                  )}
                  
                  {message.needsEscalation && (
                    <div className="mt-3 flex items-center space-x-2 p-2 bg-red-100 rounded-lg">
                      <AlertTriangle size={16} className="text-red-600" />
                      <span className="text-xs text-red-600 font-medium">
                        Sensitive content detected
                      </span>
                    </div>
                  )}
                  
                  <p className="text-xs opacity-50 mt-2">
                    {new Date(message.timestamp).toLocaleTimeString()}
                  </p>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>
          
          {isTyping && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="flex justify-start"
            >
              <div className="chat-bubble-ai">
                <div className="flex space-x-1">
                  <div className="w-2 h-2 bg-ministry-gold rounded-full animate-bounce"></div>
                  <div className="w-2 h-2 bg-ministry-gold rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                  <div className="w-2 h-2 bg-ministry-gold rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                </div>
              </div>
            </motion.div>
          )}
          
          <div ref={messagesEndRef} />
        </div>

        {/* Quick Replies */}
        <div className="p-4 border-t border-gray-200">
          <div className="flex flex-wrap gap-2 mb-4">
            {quickReplies.map((reply) => (
              <Button
                key={reply}
                variant="outline"
                size="sm"
                onClick={() => handleQuickReply(reply)}
                className="text-xs"
              >
                {reply}
              </Button>
            ))}
          </div>
        </div>

        {/* Message Input */}
        <div className="p-6 border-t border-gray-200">
          <div className="flex space-x-4">
            <Input
              value={newMessage}
              onChange={(e) => setNewMessage(e.target.value)}
              placeholder="Type your message..."
              onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
              className="flex-1"
            />
            <Button onClick={handleSendMessage} className="ministry-button">
              <Send size={16} />
            </Button>
          </div>
        </div>
      </div>
    </div>
  )
}

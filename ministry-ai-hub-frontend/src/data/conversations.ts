export interface Message {
  id: string
  content: string
  sender: 'user' | 'ai'
  timestamp: Date
  type?: 'prayer' | 'question' | 'escalation'
}

export interface Conversation {
  id: string
  title: string
  messages: Message[]
  status: 'active' | 'resolved' | 'escalated'
  lastActivity: Date
}

export const conversationsData: Conversation[] = [
  {
    id: '1',
    title: 'Prayer Request - Family Health',
    status: 'active',
    lastActivity: new Date(),
    messages: [
      {
        id: '1',
        content: 'Please pray for my mother who is in the hospital',
        sender: 'user',
        timestamp: new Date(),
        type: 'prayer'
      },
      {
        id: '2',
        content: 'I will escalate this to a human minister who will certainly pray for your mother\'s healing. May I ask what she is being treated for so I can pray more specifically?',
        sender: 'ai',
        timestamp: new Date()
      }
    ]
  }
]

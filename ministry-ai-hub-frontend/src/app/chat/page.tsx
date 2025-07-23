import { ChatWindow } from '@/components/chat/ChatWindow'

export default function ChatPage() {
  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-gray-900">Digital Minister</h1>
        <p className="text-gray-600">AI-powered ministry conversations and support</p>
      </div>
      <ChatWindow />
    </div>
  )
}

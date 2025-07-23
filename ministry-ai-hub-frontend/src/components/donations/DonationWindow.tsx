'use client'

import { useState, useRef, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Send, Heart, DollarSign, Gift, ArrowRight, ArrowLeft } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Badge } from '@/components/ui/badge'

interface DonorData {
  name: string
  email: string
  amount: string
  donationType: string
}

interface DonationMessage {
  id: string
  content: string
  type: 'thank_you' | 'impact_story' | 'recurring_promotion' | 'qa_response'
  timestamp: string
}

const donationQuickActions = [
  'How can I give?',
  'Is my donation tax deductible?',
  'Tell me about recurring giving',
  'Show me ministry impact',
]

export function DonationWindow() {
  const [currentStep, setCurrentStep] = useState(1)
  const [donorData, setDonorData] = useState<DonorData>({
    name: '',
    email: '',
    amount: '',
    donationType: 'one_time'
  })
  const [messages, setMessages] = useState<DonationMessage[]>([])
  const [newQuestion, setNewQuestion] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleGenerateThankYou = async () => {
    if (!donorData.name || !donorData.amount) return

    setIsLoading(true)
    try {
      const response = await fetch('http://localhost:8000/api/v1/donation/thank-you', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          donor_name: donorData.name,
          amount: donorData.amount,
          email: donorData.email
        }),
      })

      if (response.ok) {
        const data = await response.json()
        const thankYouMessage: DonationMessage = {
          id: Date.now().toString(),
          content: data.thank_you_message,
          type: 'thank_you',
          timestamp: new Date().toISOString(),
        }
        setMessages(prev => [...prev, thankYouMessage])
      } else {
        throw new Error('API response not ok')
      }
    } catch (error) {
      console.warn('Backend API not available, using fallback:', error)
      const fallbackMessage: DonationMessage = {
        id: Date.now().toString(),
        content: `Dear ${donorData.name}, thank you for your generous gift of ${donorData.amount}. Your support makes a tremendous difference in our ministry. "Each of you should give what you have decided in your heart to give, not reluctantly or under compulsion, for God loves a cheerful giver." - 2 Corinthians 9:7`,
        type: 'thank_you',
        timestamp: new Date().toISOString(),
      }
      setMessages(prev => [...prev, fallbackMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handleGenerateImpactStory = async () => {
    setIsLoading(true)
    try {
      const response = await fetch('http://localhost:8000/api/v1/donation/impact-story', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          category: 'general',
          donor_segment: 'regular_donor'
        }),
      })

      if (response.ok) {
        const data = await response.json()
        const impactMessage: DonationMessage = {
          id: Date.now().toString(),
          content: data.impact_story,
          type: 'impact_story',
          timestamp: new Date().toISOString(),
        }
        setMessages(prev => [...prev, impactMessage])
      } else {
        throw new Error('API response not ok')
      }
    } catch (error) {
      console.warn('Backend API not available, using fallback:', error)
      const fallbackMessage: DonationMessage = {
        id: Date.now().toString(),
        content: "Your generous support continues to transform lives and advance God's kingdom through our ministry work. Last month, we were able to provide meals for 150 families, support 25 students with scholarships, and expand our community outreach programs to reach 500 more people with the Gospel.",
        type: 'impact_story',
        timestamp: new Date().toISOString(),
      }
      setMessages(prev => [...prev, fallbackMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handlePromoteRecurring = async () => {
    if (!donorData.name) return

    setIsLoading(true)
    try {
      const response = await fetch('http://localhost:8000/api/v1/donation/recurring', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          donor_name: donorData.name,
          current_amount: donorData.amount,
          suggested_frequency: 'monthly'
        }),
      })

      if (response.ok) {
        const data = await response.json()
        const recurringMessage: DonationMessage = {
          id: Date.now().toString(),
          content: data.recurring_message,
          type: 'recurring_promotion',
          timestamp: new Date().toISOString(),
        }
        setMessages(prev => [...prev, recurringMessage])
      } else {
        throw new Error('API response not ok')
      }
    } catch (error) {
      console.warn('Backend API not available, using fallback:', error)
      const fallbackMessage: DonationMessage = {
        id: Date.now().toString(),
        content: `Dear ${donorData.name}, consider making your giving a regular spiritual discipline through recurring donations. "Honor the Lord with your wealth, with the firstfruits of all your crops." - Proverbs 3:9. Monthly giving helps us plan ministry activities and creates a consistent rhythm of stewardship in your spiritual journey.`,
        type: 'recurring_promotion',
        timestamp: new Date().toISOString(),
      }
      setMessages(prev => [...prev, recurringMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handleDonationQuestion = async () => {
    if (!newQuestion.trim()) return

    setIsLoading(true)
    try {
      const response = await fetch('http://localhost:8000/api/v1/donation/qa', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question: newQuestion,
          donor_context: 'general'
        }),
      })

      if (response.ok) {
        const data = await response.json()
        const qaMessage: DonationMessage = {
          id: Date.now().toString(),
          content: data.answer,
          type: 'qa_response',
          timestamp: new Date().toISOString(),
        }
        setMessages(prev => [...prev, qaMessage])
      } else {
        throw new Error('API response not ok')
      }
    } catch (error) {
      console.warn('Backend API not available, using fallback:', error)
      const fallbackMessage: DonationMessage = {
        id: Date.now().toString(),
        content: "Thank you for your question about giving. Our ministry team will provide you with detailed information about donation policies and tax benefits. All donations to our ministry are tax-deductible, and we provide receipts for your records.",
        type: 'qa_response',
        timestamp: new Date().toISOString(),
      }
      setMessages(prev => [...prev, fallbackMessage])
    } finally {
      setIsLoading(false)
      setNewQuestion('')
    }
  }

  const handleQuickAction = (action: string) => {
    setNewQuestion(action)
  }

  const nextStep = () => {
    if (currentStep < 4) setCurrentStep(currentStep + 1)
  }

  const prevStep = () => {
    if (currentStep > 1) setCurrentStep(currentStep - 1)
  }

  return (
    <div className="max-w-7xl mx-auto h-full flex">
      {/* Donation Flow Steps */}
      <div className="w-1/3 bg-white rounded-l-xl shadow-lg border-r border-gray-200">
        <div className="p-6 border-b border-gray-200">
          <h2 className="font-playfair text-xl font-bold text-ministry-navy">
            Stewardship Companion
          </h2>
          <p className="text-sm text-gray-600">4-Step Donation Engagement</p>
        </div>

        <div className="p-6 space-y-6">
          {/* Step Indicator */}
          <div className="flex items-center space-x-2">
            {[1, 2, 3, 4].map((step) => (
              <div
                key={step}
                className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium ${
                  step === currentStep
                    ? 'bg-blue-600 text-white'
                    : step < currentStep
                    ? 'bg-green-500 text-white'
                    : 'bg-gray-200 text-gray-600'
                }`}
              >
                {step}
              </div>
            ))}
          </div>

          {/* Step 1: Donor Information */}
          {currentStep === 1 && (
            <div className="space-y-4">
              <h3 className="font-semibold text-gray-900">Donor Information</h3>
              <Input
                placeholder="Donor Name"
                value={donorData.name}
                onChange={(e) => setDonorData(prev => ({ ...prev, name: e.target.value }))}
              />
              <Input
                placeholder="Email (optional)"
                type="email"
                value={donorData.email}
                onChange={(e) => setDonorData(prev => ({ ...prev, email: e.target.value }))}
              />
              <Input
                placeholder="Donation Amount (e.g., $50)"
                value={donorData.amount}
                onChange={(e) => setDonorData(prev => ({ ...prev, amount: e.target.value }))}
              />
              <select
                className="w-full p-2 border border-gray-300 rounded-md"
                value={donorData.donationType}
                onChange={(e) => setDonorData(prev => ({ ...prev, donationType: e.target.value }))}
              >
                <option value="one_time">One-time Gift</option>
                <option value="recurring">Recurring Gift</option>
                <option value="first_time">First-time Donor</option>
              </select>
            </div>
          )}

          {/* Step 2: Thank You Generation */}
          {currentStep === 2 && (
            <div className="space-y-4">
              <h3 className="font-semibold text-gray-900">Generate Thank You</h3>
              <p className="text-sm text-gray-600">
                Create a personalized thank you message for {donorData.name}
              </p>
              <Button
                onClick={handleGenerateThankYou}
                disabled={isLoading || !donorData.name || !donorData.amount}
                className="w-full ministry-button"
              >
                <Heart className="w-4 h-4 mr-2" />
                {isLoading ? 'Generating...' : 'Generate Thank You'}
              </Button>
            </div>
          )}

          {/* Step 3: Impact Story */}
          {currentStep === 3 && (
            <div className="space-y-4">
              <h3 className="font-semibold text-gray-900">Share Impact</h3>
              <p className="text-sm text-gray-600">
                Show how donations make a difference in ministry
              </p>
              <Button
                onClick={handleGenerateImpactStory}
                disabled={isLoading}
                className="w-full ministry-button"
              >
                <Gift className="w-4 h-4 mr-2" />
                {isLoading ? 'Generating...' : 'Generate Impact Story'}
              </Button>
            </div>
          )}

          {/* Step 4: Recurring Giving */}
          {currentStep === 4 && (
            <div className="space-y-4">
              <h3 className="font-semibold text-gray-900">Promote Recurring Giving</h3>
              <p className="text-sm text-gray-600">
                Encourage ongoing stewardship partnership
              </p>
              <Button
                onClick={handlePromoteRecurring}
                disabled={isLoading || !donorData.name}
                className="w-full ministry-button"
              >
                <DollarSign className="w-4 h-4 mr-2" />
                {isLoading ? 'Generating...' : 'Promote Recurring Giving'}
              </Button>
            </div>
          )}

          {/* Navigation */}
          <div className="flex justify-between pt-4">
            <Button
              onClick={prevStep}
              disabled={currentStep === 1}
              variant="outline"
              size="sm"
            >
              <ArrowLeft className="w-4 h-4 mr-2" />
              Previous
            </Button>
            <Button
              onClick={nextStep}
              disabled={currentStep === 4}
              size="sm"
            >
              Next
              <ArrowRight className="w-4 h-4 ml-2" />
            </Button>
          </div>
        </div>
      </div>

      {/* Messages Area */}
      <div className="flex-1 bg-white rounded-r-xl shadow-lg flex flex-col">
        {/* Header */}
        <div className="p-6 border-b border-gray-200">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="font-semibold text-ministry-navy">
                Donation Engagement Messages
              </h2>
              <p className="text-sm text-gray-600">Generated stewardship content</p>
            </div>
            <Badge variant="default">
              Step {currentStep} of 4
            </Badge>
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
                className="flex justify-start"
              >
                <div className="max-w-lg chat-bubble-ai">
                  <div className="flex items-center space-x-2 mb-2">
                    <Badge variant="secondary" className="text-xs">
                      {message.type.replace('_', ' ').toUpperCase()}
                    </Badge>
                  </div>
                  <p className="whitespace-pre-wrap">{message.content}</p>
                  <p className="text-xs opacity-50 mt-2">
                    {new Date(message.timestamp).toLocaleTimeString()}
                  </p>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>

          {isLoading && (
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

        {/* Quick Actions */}
        <div className="p-4 border-t border-gray-200">
          <div className="flex flex-wrap gap-2 mb-4">
            {donationQuickActions.map((action) => (
              <Button
                key={action}
                variant="outline"
                size="sm"
                onClick={() => handleQuickAction(action)}
                className="text-xs"
              >
                {action}
              </Button>
            ))}
          </div>
        </div>

        {/* Question Input */}
        <div className="p-6 border-t border-gray-200">
          <div className="flex space-x-4">
            <Input
              value={newQuestion}
              onChange={(e) => setNewQuestion(e.target.value)}
              placeholder="Ask a question about donations..."
              onKeyPress={(e) => e.key === 'Enter' && handleDonationQuestion()}
              className="flex-1"
            />
            <Button onClick={handleDonationQuestion} className="ministry-button">
              <Send size={16} />
            </Button>
          </div>
        </div>
      </div>
    </div>
  )
}
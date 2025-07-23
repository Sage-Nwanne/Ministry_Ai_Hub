'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ChevronLeft, ChevronRight, Check, Heart, Send } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Progress } from '@/components/ui/progress'

const steps = [
  { id: 1, title: 'Donor Information', description: 'Enter donor details' },
  { id: 2, title: 'Thank-You Message', description: 'Craft personalized message' },
  { id: 3, title: 'Impact Story', description: 'Share ministry impact' },
  { id: 4, title: 'Follow-Up', description: 'Schedule next steps' },
]

export function DonationFlow() {
  const [currentStep, setCurrentStep] = useState(1)
  const [donorData, setDonorData] = useState({
    name: '',
    email: '',
    amount: '',
    donationType: 'one-time',
  })
  const [thankYouMessage, setThankYouMessage] = useState('')
  const [impactStory, setImpactStory] = useState('')
  const [isComplete, setIsComplete] = useState(false)

  const progress = (currentStep / steps.length) * 100

  const handleNext = () => {
    if (currentStep < steps.length) {
      setCurrentStep(currentStep + 1)
    }
  }

  const handlePrevious = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1)
    }
  }

  const handleSubmit = () => {
    setIsComplete(true)
    // Simulate API call
    setTimeout(() => {
      alert('Donation engagement sent successfully!')
      setIsComplete(false)
      setCurrentStep(1)
    }, 2000)
  }

  const generateThankYou = () => {
    const message = `Dear ${donorData.name},

Your generous gift of ${donorData.amount} brings such joy to our hearts and advances God's kingdom in powerful ways. Your faithfulness reflects the heart of a true steward.

"Each of you should give what you have decided in your heart to give, not reluctantly or under compulsion, for God loves a cheerful giver." - 2 Corinthians 9:7

Thank you for being a blessing to our ministry family.

Blessings,
Dr. Myles Monroe Ministry`

    setThankYouMessage(message)
  }

  const generateImpactStory = () => {
    const story = `Through faithful partners like you, our ministry has:

🌟 Reached over 500 families this month with food assistance
🌟 Provided scholarships for 25 students to attend leadership training
🌟 Supported 12 missionary families across 8 countries
🌟 Hosted community events that brought 200+ people to Christ

Your ${donorData.amount} gift specifically helps fund our youth mentorship program, where young leaders are discovering their God-given purpose and potential.

"Train up a child in the way he should go; even when he is old he will not depart from it." - Proverbs 22:6`

    setImpactStory(story)
  }

  return (
    <div className="max-w-7xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="mb-8"
      >
        <h1 className="font-playfair text-3xl font-bold text-ministry-navy mb-4">
          Stewardship Companion
        </h1>
        <p className="text-gray-600">
          Create personalized donor engagement experiences that inspire continued giving.
        </p>
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
        {/* Main Flow */}
        <div className="lg:col-span-3">
          <Card className="ministry-card">
            <CardHeader>
              <div className="flex items-center justify-between mb-4">
                <CardTitle className="font-playfair text-xl text-ministry-navy">
                  {steps[currentStep - 1].title}
                </CardTitle>
                <span className="text-sm text-gray-500">
                  Step {currentStep} of {steps.length}
                </span>
              </div>
              <Progress value={progress} className="w-full" />
            </CardHeader>

            <CardContent>
              <AnimatePresence mode="wait">
                {currentStep === 1 && (
                  <motion.div
                    key="step1"
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0, x: -20 }}
                    className="space-y-6"
                  >
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          Donor Name
                        </label>
                        <Input
                          value={donorData.name}
                          onChange={(e) => setDonorData({ ...donorData, name: e.target.value })}
                          placeholder="Enter donor name"
                        />
                      </div>
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          Email Address
                        </label>
                        <Input
                          type="email"
                          value={donorData.email}
                          onChange={(e) => setDonorData({ ...donorData, email: e.target.value })}
                          placeholder="Enter email address"
                        />
                      </div>
                    </div>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          Donation Amount
                        </label>
                        <Input
                          value={donorData.amount}
                          onChange={(e) => setDonorData({ ...donorData, amount: e.target.value })}
                          placeholder="$100"
                        />
                      </div>
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          Donation Type
                        </label>
                        <select
                          value={donorData.donationType}
                          onChange={(e) => setDonorData({ ...donorData, donationType: e.target.value })}
                          className="w-full p-2 border border-gray-300 rounded-md"
                        >
                          <option value="one-time">One-time Gift</option>
                          <option value="monthly">Monthly Recurring</option>
                          <option value="annual">Annual Gift</option>
                
'use client'

import { motion } from 'framer-motion'
import { SummaryCard } from '@/components/summaries/SummaryCard'
import { summariesData } from '@/data/summaries'

export default function SummariesPage() {
  return (
    <div className="max-w-7xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Dr. Myles Munroe Sermon Library</h1>
        <p className="text-gray-600">Explore transformational teachings with AI-powered insights and biblical analysis</p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {summariesData.map((summary, index) => (
          <SummaryCard key={summary.id} summary={summary} index={index} />
        ))}
      </div>
    </div>
  )
}

'use client'

import { motion } from 'framer-motion'
import { Play, Calendar, Clock, ArrowRight } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import Link from 'next/link'
import Image from 'next/image'

interface Summary {
  id: string
  title: string
  date: string
  speaker: string
  duration: string
  takeaways: string[]
  transcript: string
  tags: string[]
  youtubeUrl?: string
  thumbnailUrl?: string
}

interface SummaryCardProps {
  summary: Summary
  index: number
}

export function SummaryCard({ summary, index }: SummaryCardProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: index * 0.1 }}
    >
      <Card className="ministry-card h-full group hover:shadow-xl transition-all duration-300">
        <CardHeader className="pb-4">
          {/* Thumbnail */}
          <div className="relative w-full h-48 mb-4 rounded-lg overflow-hidden bg-gray-100">
            {summary.thumbnailUrl ? (
              <Image
                src={summary.thumbnailUrl}
                alt={summary.title}
                fill
                className="object-cover group-hover:scale-105 transition-transform duration-300"
              />
            ) : (
              <div className="w-full h-full bg-gradient-to-br from-ministry-navy to-ministry-gold flex items-center justify-center">
                <Play className="w-12 h-12 text-white" />
              </div>
            )}
            {summary.youtubeUrl && (
              <div className="absolute top-2 right-2">
                <Badge variant="secondary" className="bg-red-600 text-white">
                  <Play className="w-3 h-3 mr-1" />
                  YouTube
                </Badge>
              </div>
            )}
          </div>

          <CardTitle className="font-playfair text-lg text-ministry-navy mb-2 line-clamp-2">
            {summary.title}
          </CardTitle>
          
          <div className="flex items-center space-x-4 text-sm text-gray-600 mb-3">
            <div className="flex items-center">
              <Calendar className="w-4 h-4 mr-1" />
              <span>{summary.date}</span>
            </div>
            <div className="flex items-center">
              <Clock className="w-4 h-4 mr-1" />
              <span>{summary.duration}</span>
            </div>
          </div>

          <p className="text-sm text-gray-600 mb-3">{summary.speaker}</p>
        </CardHeader>

        <CardContent className="pt-0">
          {/* Tags */}
          <div className="flex flex-wrap gap-2 mb-4">
            {summary.tags.slice(0, 3).map((tag) => (
              <Badge key={tag} variant="secondary" className="text-xs">
                {tag}
              </Badge>
            ))}
          </div>

          {/* Key Takeaways Preview */}
          <div className="mb-6">
            <h4 className="font-semibold text-ministry-navy mb-2 text-sm">Key Insights</h4>
            <ul className="space-y-1">
              {summary.takeaways.slice(0, 2).map((takeaway, idx) => (
                <li key={idx} className="flex items-start text-xs text-gray-700">
                  <div className="w-1.5 h-1.5 bg-ministry-gold rounded-full mr-2 mt-1.5 flex-shrink-0"></div>
                  <span className="line-clamp-2">{takeaway}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Enter Button */}
          <Link href={`/summaries/${summary.id}`}>
            <Button className="w-full ministry-button group-hover:scale-105 transition-transform">
              Enter Sermon
              <ArrowRight className="w-4 h-4 ml-2" />
            </Button>
          </Link>
        </CardContent>
      </Card>
    </motion.div>
  )
}

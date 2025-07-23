'use client'

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { ArrowLeft, Play, ExternalLink, Book, Lightbulb, Calendar, Clock, User } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import Link from 'next/link'
import Image from 'next/image'
import { summariesData } from '@/data/summaries'

interface SermonDetailPageProps {
  params: {
    id: string
  }
}

export default function SermonDetailPage({ params }: SermonDetailPageProps) {
  const [sermon, setSermon] = useState(summariesData.find(s => s.id === params.id))
  const [aiAnalysis, setAiAnalysis] = useState<string>('')
  const [isLoadingAnalysis, setIsLoadingAnalysis] = useState(false)

  useEffect(() => {
    if (sermon) {
      generateAIAnalysis()
    }
  }, [sermon])

  const generateAIAnalysis = async () => {
    if (!sermon) return
    
    setIsLoadingAnalysis(true)
    try {
      const response = await fetch('http://localhost:8000/api/v1/sermon/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: sermon.title,
          transcript: sermon.transcript,
          tags: sermon.tags
        }),
      })

      if (response.ok) {
        const data = await response.json()
        setAiAnalysis(data.analysis)
      } else {
        throw new Error('API response not ok')
      }
    } catch (error) {
      console.warn('Backend API not available, using fallback analysis:', error)
      setAiAnalysis(`This powerful sermon on "${sermon.title}" demonstrates Dr. Myles Monroe's profound understanding of Kingdom principles. The message emphasizes the importance of understanding our divine purpose and living according to God's original design. Key scriptural foundations include the referenced verses which provide biblical support for the teachings presented. This sermon challenges listeners to move beyond mere existence into purposeful living, aligning their lives with God's eternal purposes.`)
    } finally {
      setIsLoadingAnalysis(false)
    }
  }

  const openBibleVerse = (verse: string) => {
    // Using Bible Gateway API
    const formattedVerse = verse.replace(/\s+/g, '+')
    window.open(`https://www.biblegateway.com/passage/?search=${formattedVerse}&version=NIV`, '_blank')
  }

  if (!sermon) {
    return (
      <div className="max-w-4xl mx-auto text-center py-20">
        <h1 className="text-2xl font-bold text-gray-900 mb-4">Sermon Not Found</h1>
        <Link href="/summaries">
          <Button>Return to Sermon Library</Button>
        </Link>
      </div>
    )
  }

  return (
    <div className="max-w-6xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <Link href="/summaries">
          <Button variant="outline" className="mb-4">
            <ArrowLeft className="w-4 h-4 mr-2" />
            Back to Sermon Library
          </Button>
        </Link>
        
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-xl shadow-lg p-8"
        >
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {/* Video Thumbnail */}
            <div className="lg:col-span-1">
              <div className="relative w-full h-64 rounded-lg overflow-hidden bg-gray-100">
                {sermon.thumbnailUrl ? (
                  <Image
                    src={sermon.thumbnailUrl}
                    alt={sermon.title}
                    fill
                    className="object-cover"
                  />
                ) : (
                  <div className="w-full h-full bg-gradient-to-br from-ministry-navy to-ministry-gold flex items-center justify-center">
                    <Play className="w-16 h-16 text-white" />
                  </div>
                )}
                {sermon.youtubeUrl && (
                  <div className="absolute inset-0 flex items-center justify-center">
                    <a
                      href={sermon.youtubeUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="bg-red-600 hover:bg-red-700 text-white px-6 py-3 rounded-lg flex items-center transition-colors"
                    >
                      <Play className="w-5 h-5 mr-2" />
                      Watch on YouTube
                    </a>
                  </div>
                )}
              </div>
            </div>

            {/* Sermon Info */}
            <div className="lg:col-span-2">
              <h1 className="text-3xl font-bold text-ministry-navy mb-4">{sermon.title}</h1>
              
              <div className="flex flex-wrap items-center gap-4 mb-4 text-gray-600">
                <div className="flex items-center">
                  <User className="w-4 h-4 mr-2" />
                  <span>{sermon.speaker}</span>
                </div>
                <div className="flex items-center">
                  <Calendar className="w-4 h-4 mr-2" />
                  <span>{sermon.date}</span>
                </div>
                <div className="flex items-center">
                  <Clock className="w-4 h-4 mr-2" />
                  <span>{sermon.duration}</span>
                </div>
              </div>

              <div className="flex flex-wrap gap-2 mb-6">
                {sermon.tags.map((tag) => (
                  <Badge key={tag} variant="secondary">
                    {tag}
                  </Badge>
                ))}
              </div>

              {sermon.youtubeUrl && (
                <a
                  href={sermon.youtubeUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center text-blue-600 hover:text-blue-800"
                >
                  <ExternalLink className="w-4 h-4 mr-2" />
                  Open in YouTube
                </a>
              )}
            </div>
          </div>
        </motion.div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Main Content */}
        <div className="lg:col-span-2 space-y-8">
          {/* Key Takeaways */}
          <Card className="ministry-card">
            <CardHeader>
              <CardTitle className="flex items-center">
                <Lightbulb className="w-5 h-5 mr-2 text-ministry-gold" />
                Key Takeaways
              </CardTitle>
            </CardHeader>
            <CardContent>
              <ul className="space-y-3">
                {sermon.takeaways.map((takeaway, idx) => (
                  <li key={idx} className="flex items-start">
                    <div className="w-2 h-2 bg-ministry-gold rounded-full mr-3 mt-2 flex-shrink-0"></div>
                    <span className="text-gray-700">{takeaway}</span>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>

          {/* AI Analysis */}
          <Card className="ministry-card">
            <CardHeader>
              <CardTitle className="flex items-center">
                <Book className="w-5 h-5 mr-2 text-ministry-navy" />
                AI Sermon Analysis
              </CardTitle>
            </CardHeader>
            <CardContent>
              {isLoadingAnalysis ? (
                <div className="flex items-center justify-center py-8">
                  <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-ministry-navy"></div>
                  <span className="ml-3 text-gray-600">Generating AI analysis...</span>
                </div>
              ) : (
                <p className="text-gray-700 leading-relaxed">{aiAnalysis}</p>
              )}
            </CardContent>
          </Card>

          {/* Full Transcript */}
          <Card className="ministry-card">
            <CardHeader>
              <CardTitle>Full Transcript</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="prose max-w-none">
                <p className="text-gray-700 leading-relaxed whitespace-pre-line">
                  {sermon.transcript}
                </p>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Scripture References */}
          {sermon.scriptures && (
            <Card className="ministry-card">
              <CardHeader>
                <CardTitle className="flex items-center">
                  <Book className="w-5 h-5 mr-2 text-ministry-gold" />
                  Scripture References
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {sermon.scriptures.map((scripture, idx) => (
                    <div key={idx} className="flex items-center justify-between">
                      <span className="text-gray-700 font-medium">{scripture}</span>
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={() => openBibleVerse(scripture)}
                        className="text-xs"
                      >
                        <ExternalLink className="w-3 h-3 mr-1" />
                        Read
                      </Button>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}

          {/* Related Sermons */}
          <Card className="ministry-card">
            <CardHeader>
              <CardTitle>Related Sermons</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {summariesData
                  .filter(s => s.id !== sermon.id && s.tags.some(tag => sermon.tags.includes(tag)))
                  .slice(0, 3)
                  .map((relatedSermon) => (
                    <Link key={relatedSermon.id} href={`/summaries/${relatedSermon.id}`}>
                      <div className="p-3 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors cursor-pointer">
                        <h4 className="font-medium text-sm text-ministry-navy mb-1 line-clamp-2">
                          {relatedSermon.title}
                        </h4>
                        <p className="text-xs text-gray-600">{relatedSermon.speaker} • {relatedSermon.date}</p>
                      </div>
                    </Link>
                  ))}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}
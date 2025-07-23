'use client'

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { 
  MessageCircle, 
  FileText, 
  Heart, 
  BarChart3, 
  ArrowRight,
  CheckCircle 
} from 'lucide-react'
import Link from 'next/link'
import { motion } from 'framer-motion'

const features = [
  {
    title: 'Digital Minister',
    description: 'AI-powered conversations with biblical wisdom',
    icon: MessageCircle,
    href: '/chat',
    color: 'from-blue-500 to-blue-600',
    features: [
      'Intelligent message processing',
      'Prayer request routing',
      'Scripture-based responses',
      'Multilingual support'
    ]
  },
  {
    title: 'Sermon Insights',
    description: 'Transform sermons into actionable insights',
    icon: FileText,
    href: '/summaries',
    color: 'from-green-500 to-green-600',
    features: [
      'Automatic transcription',
      'Key takeaway extraction',
      'Discussion questions',
      'Follow-up resources'
    ]
  },
  {
    title: 'Stewardship Companion',
    description: 'Enhance donor relationships with personalized engagement',
    icon: Heart,
    href: '/donations',
    color: 'from-red-500 to-red-600',
    features: [
      'Thank-you messages',
      'Impact stories',
      'Giving insights',
      'Stewardship guidance'
    ]
  },
  {
    title: 'Ministry Analytics',
    description: 'Comprehensive analytics for ministry effectiveness',
    icon: BarChart3,
    href: '/analytics',
    color: 'from-purple-500 to-purple-600',
    features: [
      'Real-time metrics',
      'Engagement tracking',
      'Trend analysis',
      'Custom reports'
    ]
  }
]

export function FeaturesSection() {
  return (
    <section className="py-20 bg-gradient-to-br from-slate-50 to-blue-50">
      <div className="max-w-7xl mx-auto px-6">
        {/* Feature Cards - 4 cards taking 25% width each */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, index) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              viewport={{ once: true }}
              className="w-full"
            >
              <Card className="ministry-card h-full group hover:shadow-xl transition-all duration-300 hover:scale-105">
                <CardHeader className="text-center pb-4">
                  <div className={`w-16 h-16 bg-gradient-to-br ${feature.color} rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-medium`}>
                    <feature.icon className="w-8 h-8 text-white" />
                  </div>
                  <CardTitle className="text-xl font-bold text-slate-900 group-hover:text-ministry-navy transition-colors">
                    {feature.title}
                  </CardTitle>
                  <p className="text-slate-600">{feature.description}</p>
                </CardHeader>
                <CardContent className="space-y-6">
                  <ul className="space-y-3">
                    {feature.features.map((item, i) => (
                      <li key={i} className="flex items-center gap-3 text-sm text-slate-600">
                        <CheckCircle className="w-4 h-4 text-green-500 flex-shrink-0" />
                        {item}
                      </li>
                    ))}
                  </ul>
                  <Link href={feature.href} className="block">
                    <Button className="w-full ministry-button group-hover:bg-gradient-to-r group-hover:from-ministry-navy-light group-hover:to-ministry-navy group-hover:shadow-lg transition-all duration-300 hover:scale-105 hover:shadow-xl active:scale-95">
                      Explore
                      <ArrowRight className="w-4 h-4 ml-2" />
                    </Button>
                  </Link>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}

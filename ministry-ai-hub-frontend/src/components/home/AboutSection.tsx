'use client'

import { Card, CardContent } from '@/components/ui/card'
import { Shield, Clock, Heart } from 'lucide-react'

const features = [
  {
    icon: Shield,
    title: 'Secure & Private',
    description: 'All conversations are encrypted and handled with the highest level of pastoral confidentiality'
  },
  {
    icon: Clock,
    title: '24/7 Availability',
    description: 'Provide immediate pastoral care and support whenever your congregation needs it most'
  },
  {
    icon: Heart,
    title: 'Human-Centered',
    description: 'AI assistance that never replaces the human touch of pastoral empathy and care'
  }
]

export function AboutSection() {
  return (
    <section className="py-20" style={{ backgroundColor: '#aa79ebff' }}>
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-6" style={{ color: '#e9e501ff' }}>
            About Our Ministry
          </h2>
          <p className="text-lg max-w-3xl mx-auto" style={{ color: '#dbd037ff', fontWeight: 'bold', fontSize: '1.2rem' }}>
            The Ministry AI Hub serves as your digital ministry companion, providing intelligent, compassionate responses to congregation members while maintaining the heart of pastoral care. Our AI-powered platform handles routine inquiries, prayer requests, and stewardship conversations, allowing pastoral staff to focus on deeper ministry relationships.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <Card key={index} className="ministry-card text-center">
              <CardContent className="p-8">
                <div className="w-16 h-16 bg-gradient-to-br from-ministry-navy to-ministry-navy-light rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-medium">
                  <feature.icon className="w-8 h-8 text-white" />
                </div>
                <h3 className="text-xl font-bold text-slate-900 mb-4">{feature.title}</h3>
                <p className="text-slate-600">{feature.description}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}

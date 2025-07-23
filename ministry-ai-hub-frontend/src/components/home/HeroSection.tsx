'use client'

import { Button } from '@/components/ui/button'
import { MessageCircle, ArrowRight } from 'lucide-react'
import Link from 'next/link'
import Image from 'next/image'

export function HeroSection() {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden" style={{ backgroundColor: '#e7f1f5ff' }}>
      <div className="relative z-10 max-w-7xl mx-auto px-6 text-center">
        {/* Logo and Title */}
        <div className="mb-8">
          <div className="flex items-center justify-center gap-4 mb-6">
            <div className="w-20 h-20 bg-gradient-to-br from-yellow-500 to-yellow-600 rounded-2xl flex items-center justify-center shadow-lg overflow-hidden">
              <Image
                src="/munroe-logo.jpeg"
                alt="Myles Munroe International Logo"
                width={80}
                height={80}
                className="object-cover w-full h-full rounded-2xl"
              />
            </div>
            <h1 className="text-4xl md:text-6xl font-bold text-gray-900">
              Munroe Ministry AI Hub
            </h1>
          </div>
          <p className="text-xl md:text-2xl text-gray-700 max-w-3xl mx-auto leading-relaxed">
            Your Digital Ministry Companion
          </p>
        </div>

        {/* Main content */}
        <div className="space-y-8">
          <p className="text-lg md:text-xl text-gray-700 max-w-4xl mx-auto leading-relaxed">
            Empowering pastoral care through intelligent conversations, prayer support, and stewardship guidance powered by AI technology designed for ministry excellence.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/chat">
              <Button className="bg-gradient-to-r from-yellow-500 to-yellow-600 hover:from-yellow-600 hover:to-yellow-700 text-white text-lg px-8 py-4 h-auto">
                <MessageCircle className="w-5 h-5 mr-2" />
                Start Conversation
              </Button>
            </Link>
            <Link href="/analytics">
              <Button variant="outline" className="bg-transparent border-2 border-gray-700 text-gray-700 hover:bg-gray-700 hover:text-white text-lg px-8 py-4 h-auto">
                View Analytics
                <ArrowRight className="w-5 h-5 ml-2" />
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </section>
  )
}

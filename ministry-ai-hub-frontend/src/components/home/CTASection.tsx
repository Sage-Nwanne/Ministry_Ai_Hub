'use client'

import { Card, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { MessageCircle, BarChart3 } from 'lucide-react'
import Link from 'next/link'
import { motion } from 'framer-motion'

export function CTASection() {
  return (
    <section className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center"
        >
          <Card className="ministry-card max-w-4xl mx-auto">
            <CardContent className="p-12 text-center space-y-6">
              <h3 className="font-playfair text-3xl font-bold text-ministry-navy">
                Ready to Transform Your Ministry?
              </h3>
              <p className="text-lg text-slate-600 max-w-2xl mx-auto">
                Join the growing number of churches using AI to enhance pastoral care, 
                improve stewardship, and create deeper connections with their congregation.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center pt-4">
                <Link href="/chat">
                  <Button className="ministry-button text-lg px-8 py-4 h-auto">
                    <MessageCircle className="w-5 h-5 mr-2" />
                    Start Your First Conversation
                  </Button>
                </Link>
                <Link href="/analytics">
                  <Button variant="outline" className="ghost-button text-lg px-8 py-4 h-auto border-2">
                    <BarChart3 className="w-5 h-5 mr-2" />
                    View Analytics
                  </Button>
                </Link>
              </div>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </section>
  )
}
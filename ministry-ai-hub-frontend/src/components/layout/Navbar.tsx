'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { Button } from '@/components/ui/button'
import { 
  MessageCircle, 
  Heart, 
  Calendar, 
  Settings, 
  FileText, 
  BarChart3,
  Menu,
  X
} from 'lucide-react'
import { useState } from 'react'

const navigation = [
  { name: 'Chat', href: '/chat', icon: MessageCircle },
  { name: 'Donations', href: '/donations', icon: Heart },
  { name: 'Events', href: '/events', icon: Calendar },
  { name: 'Settings', href: '/settings', icon: Settings },
  { name: 'Sermons', href: '/summaries', icon: FileText },
  { name: 'Analytics', href: '/analytics', icon: BarChart3 },
]

export function Navbar() {
  const pathname = usePathname()
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <nav className="bg-white/95 backdrop-blur-sm border-b border-slate-200 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-3">
            <div className="w-8 h-8 bg-gradient-to-br from-ministry-navy to-ministry-navy-light rounded-lg flex items-center justify-center">
              <span className="text-white text-sm font-bold font-playfair">M</span>
            </div>
            <span className="font-playfair text-xl font-bold text-ministry-navy">Ministry Hub</span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-1">
            {navigation.map((item) => {
              const isActive = pathname === item.href
              return (
                <Link key={item.name} href={item.href}>
                  <Button
                    variant={isActive ? "default" : "ghost"}
                    className={`flex items-center gap-2 px-4 py-2 ${
                      isActive 
                        ? 'ministry-button' 
                        : 'hover:bg-slate-100 text-slate-700 hover:text-ministry-navy'
                    }`}
                  >
                    <item.icon className="w-4 h-4" />
                    {item.name}
                  </Button>
                </Link>
              )
            })}
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            >
              {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </Button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {mobileMenuOpen && (
          <div className="md:hidden py-4 border-t border-slate-200">
            <div className="space-y-2">
              {navigation.map((item) => {
                const isActive = pathname === item.href
                return (
                  <Link key={item.name} href={item.href} onClick={() => setMobileMenuOpen(false)}>
                    <Button
                      variant={isActive ? "default" : "ghost"}
                      className={`w-full justify-start gap-3 ${
                        isActive 
                          ? 'ministry-button' 
                          : 'hover:bg-slate-100 text-slate-700'
                      }`}
                    >
                      <item.icon className="w-4 h-4" />
                      {item.name}
                    </Button>
                  </Link>
                )
              })}
            </div>
          </div>
        )}
      </div>
    </nav>
  )
}
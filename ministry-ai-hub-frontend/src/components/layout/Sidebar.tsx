'use client'

import { useState } from 'react'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { 
  Home, 
  MessageCircle, 
  FileText, 
  Heart, 
  BarChart3, 
  X,
  ChevronDown,
  Users,
  Calendar,
  Settings
} from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { cn } from '@/lib/utils'

interface SidebarProps {
  isOpen: boolean
  onClose: () => void
}

const navigation = [
  { name: 'Dashboard', href: '/', icon: Home },
  { name: 'Digital Minister', href: '/chat', icon: MessageCircle, badge: '24' },
  { name: 'Sermon Insights', href: '/summaries', icon: FileText, badge: '8' },
  { name: 'Stewardship', href: '/donations', icon: Heart, badge: '12' },
  { name: 'Analytics', href: '/analytics', icon: BarChart3 },
]

const secondaryNavigation = [
  { name: 'Members', href: '/members', icon: Users },
  { name: 'Events', href: '/events', icon: Calendar },
  { name: 'Settings', href: '/settings', icon: Settings },
]

export function Sidebar({ isOpen, onClose }: SidebarProps) {
  const pathname = usePathname()

  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div 
          className="fixed inset-0 z-40 bg-slate-900/50 backdrop-blur-sm lg:hidden"
          onClick={onClose}
        />
      )}

      {/* Sidebar */}
      <div className={cn(
        "fixed inset-y-0 left-0 z-50 w-64 bg-white border-r border-slate-200/60 transform transition-transform duration-300 ease-in-out lg:translate-x-0 lg:static lg:inset-0",
        isOpen ? "translate-x-0" : "-translate-x-full"
      )}>
        <div className="flex flex-col h-full">
          {/* Header */}
          <div className="flex items-center justify-between h-16 px-6 border-b border-slate-200/60">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-gradient-to-br from-ministry-navy to-ministry-navy-light rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">M</span>
              </div>
              <div>
                <h1 className="font-playfair font-bold text-lg text-slate-900">Ministry Hub</h1>
                <p className="text-xs text-slate-500">Digital Platform</p>
              </div>
            </div>
            <Button
              variant="ghost"
              size="icon"
              onClick={onClose}
              className="lg:hidden"
            >
              <X className="h-5 w-5" />
            </Button>
          </div>

          {/* Navigation */}
          <nav className="flex-1 px-4 py-6 space-y-2 custom-scrollbar overflow-y-auto">
            {/* Primary Navigation */}
            <div className="space-y-1">
              {navigation.map((item) => {
                const isActive = pathname === item.href
                return (
                  <Link
                    key={item.name}
                    href={item.href}
                    className={cn(
                      "nav-item",
                      isActive && "active"
                    )}
                    onClick={() => onClose()}
                  >
                    <item.icon className="h-5 w-5 mr-3 transition-colors" />
                    <span className="flex-1 font-medium">{item.name}</span>
                    {item.badge && (
                      <Badge variant="secondary" className="ml-auto">
                        {item.badge}
                      </Badge>
                    )}
                  </Link>
                )
              })}
            </div>

            {/* Divider */}
            <div className="my-6 border-t border-slate-200"></div>

            {/* Secondary Navigation */}
            <div className="space-y-1">
              <h3 className="px-4 text-xs font-semibold text-slate-500 uppercase tracking-wider mb-3">
                Ministry Tools
              </h3>
              {secondaryNavigation.map((item) => {
                const isActive = pathname === item.href
                return (
                  <Link
                    key={item.name}
                    href={item.href}
                    className={cn(
                      "nav-item",
                      isActive && "active"
                    )}
                    onClick={() => onClose()}
                  >
                    <item.icon className="h-5 w-5 mr-3 transition-colors" />
                    <span className="flex-1 font-medium">{item.name}</span>
                  </Link>
                )
              })}
            </div>
          </nav>

          {/* Footer */}
          <div className="p-4 border-t border-slate-200/60">
            <div className="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
              <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
              <div className="flex-1">
                <p className="text-sm font-medium text-slate-900">All Systems</p>
                <p className="text-xs text-slate-500">Operational</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

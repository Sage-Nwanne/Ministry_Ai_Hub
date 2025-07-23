'use client'

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { 
  MessageCircle, 
  FileText, 
  Heart, 
  BarChart3, 
  Users, 
  TrendingUp,
  Clock,
  CheckCircle,
  ArrowUpRight,
  Activity,
  DollarSign
} from 'lucide-react'
import Link from 'next/link'

const moduleCards = [
  {
    title: 'Digital Minister',
    description: 'AI-powered ministry conversations and prayer support',
    icon: MessageCircle,
    href: '/chat',
    gradient: 'from-blue-500 to-blue-600',
    stats: { active: 24, total: 156, change: '+12%' }
  },
  {
    title: 'Sermon Insights',
    description: 'Transcript management and sermon analysis',
    icon: FileText,
    href: '/summaries',
    gradient: 'from-green-500 to-green-600',
    stats: { active: 8, total: 42, change: '+8%' }
  },
  {
    title: 'Stewardship Companion',
    description: 'Donation engagement and giving analytics',
    icon: Heart,
    href: '/donations',
    gradient: 'from-red-500 to-red-600',
    stats: { active: 12, total: 89, change: '+15%' }
  },
  {
    title: 'Ministry Analytics',
    description: 'Comprehensive ministry effectiveness metrics',
    icon: BarChart3,
    href: '/analytics',
    gradient: 'from-purple-500 to-purple-600',
    stats: { active: 5, total: 23, change: '+5%' }
  }
]

const quickStats = [
  {
    title: 'Active Conversations',
    value: '24',
    change: '+12%',
    icon: MessageCircle,
    color: 'text-blue-600',
    bgColor: 'bg-blue-50'
  },
  {
    title: 'Prayer Requests',
    value: '12',
    change: '+8%',
    icon: Users,
    color: 'text-green-600',
    bgColor: 'bg-green-50'
  },
  {
    title: 'Donations Today',
    value: '$2,450',
    change: '+15%',
    icon: DollarSign,
    color: 'text-red-600',
    bgColor: 'bg-red-50'
  },
  {
    title: 'Response Time',
    value: '1.2s',
    change: '-5%',
    icon: Activity,
    color: 'text-purple-600',
    bgColor: 'bg-purple-50'
  }
]

const recentActivity = [
  { type: 'prayer', message: 'New prayer request received from Sarah M.', time: '2 minutes ago', status: 'new' },
  { type: 'donation', message: 'Thank you message sent to John D. ($250)', time: '15 minutes ago', status: 'completed' },
  { type: 'sermon', message: 'Sunday sermon transcript processed', time: '1 hour ago', status: 'completed' },
  { type: 'escalation', message: 'Message escalated to pastoral team', time: '2 hours ago', status: 'pending' }
]

export function Dashboard() {
  return (
    <div className="space-y-8 animate-in">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-4xl font-bold text-slate-900 mb-2">Ministry AI Hub</h1>
          <p className="text-lg text-slate-600">
            Welcome to your digital ministry command center
          </p>
        </div>
        <div className="flex items-center gap-3">
          <Badge variant="outline" className="status-online">
            <CheckCircle className="w-3 h-3 mr-1" />
            All Systems Operational
          </Badge>
          <Button className="ministry-button">
            View Reports
            <ArrowUpRight className="w-4 h-4 ml-2" />
          </Button>
        </div>
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {quickStats.map((stat, index) => (
          <Card key={stat.title} className="ministry-card slide-in" style={{ animationDelay: `${index * 100}ms` }}>
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div className="space-y-2">
                  <p className="text-sm font-medium text-slate-600">{stat.title}</p>
                  <p className="text-3xl font-bold text-slate-900">{stat.value}</p>
                  <div className="flex items-center gap-1">
                    <TrendingUp className="w-3 h-3 text-green-600" />
                    <span className="text-sm font-medium text-green-600">{stat.change}</span>
                    <span className="text-sm text-slate-500">vs last week</span>
                  </div>
                </div>
                <div className={`p-3 rounded-xl ${stat.bgColor}`}>
                  <stat.icon className={`w-6 h-6 ${stat.color}`} />
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Module Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {moduleCards.map((module, index) => {
          const IconComponent = module.icon
          return (
            <Card key={module.title} className="ministry-card group scale-in" style={{ animationDelay: `${index * 150}ms` }}>
              <CardHeader className="pb-4">
                <div className="flex items-center justify-between mb-4">
                  <div className={`p-3 rounded-xl bg-gradient-to-br ${module.gradient} shadow-soft`}>
                    <IconComponent className="w-6 h-6 text-white" />
                  </div>
                  <Badge variant="secondary" className="font-medium">
                    {module.stats.active} active
                  </Badge>
                </div>
                <CardTitle className="text-xl font-bold text-slate-900 group-hover:text-ministry-navy transition-colors">
                  {module.title}
                </CardTitle>
                <CardDescription className="text-slate-600 leading-relaxed">
                  {module.description}
                </CardDescription>
              </CardHeader>
              <CardContent className="pt-0">
                <div className="flex items-center justify-between mb-4">
                  <div className="text-sm text-slate-500">
                    <span className="font-medium text-slate-700">{module.stats.total}</span> total interactions
                  </div>
                  <div className="flex items-center gap-1 text-green-600">
                    <TrendingUp className="w-3 h-3" />
                    <span className="text-sm font-medium">{module.stats.change}</span>
                  </div>
                </div>
                <Link href={module.href}>
                  <Button className="w-full ministry-button group-hover:scale-105 transition-transform">
                    Open Module
                    <ArrowUpRight className="w-4 h-4 ml-2" />
                  </Button>
                </Link>
              </CardContent>
            </Card>
          )
        })}
      </div>

      {/* Recent Activity & System Status */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card className="ministry-card">
          <CardHeader>
            <CardTitle className="text-xl font-bold text-slate-900">Recent Activity</CardTitle>
            <CardDescription>Latest ministry interactions and updates</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {recentActivity.map((activity, index) => (
                <div key={index} className="flex items-start gap-4 p-4 bg-slate-50 rounded-xl hover:bg-slate-100 transition-colors">
                  <div className={`w-2 h-2 rounded-full mt-2 ${
                    activity.status === 'new' ? 'bg-blue-500' :
                    activity.status === 'completed' ? 'bg-green-500' : 'bg-yellow-500'
                  }`}></div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-slate-900 mb-1">{activity.message}</p>
                    <p className="text-xs text-slate-500">{activity.time}</p>
                  </div>
                  <Badge variant={activity.status === 'completed' ? 'default' : 'secondary'} className="text-xs">
                    {activity.status}
                  </Badge>
                </div>
              ))}
            </div>
            <Button variant="outline" className="w-full mt-4 ghost-button">
              View All Activity
            </Button>
          </CardContent>
        </Card>

        <Card className="ministry-card">
          <CardHeader>
            <CardTitle className="text-xl font-bold text-slate-900">System Health</CardTitle>
            <CardDescription>Current system status and performance metrics</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {[
                { name: 'AI Processing Engine', status: 'Operational', uptime: '99.9%' },
                { name: 'Database Connection', status: 'Connected', uptime: '100%' },
                { name: 'Email Service', status: 'Active', uptime: '99.8%' },
                { name: 'Prayer Routing', status: 'Enabled', uptime: '100%' }
              ].map((service, index) => (
                <div key={service.name} className="flex items-center justify-between p-3 bg-slate-50 rounded-xl">
                  <div className="flex items-center gap-3">
                    <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                    <span className="text-sm font-medium text-slate-900">{service.name}</span>
                  </div>
                  <div className="flex items-center gap-3">
                    <span className="text-xs text-slate-500">{service.uptime}</span>
                    <Badge className="status-online text-xs">
                      {service.status}
                    </Badge>
                  </div>
                </div>
              ))}
            </div>
            <Button variant="outline" className="w-full mt-4 ghost-button">
              System Diagnostics
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

export default Dashboard

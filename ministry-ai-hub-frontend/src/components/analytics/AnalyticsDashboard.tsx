'use client'

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { 
  BarChart3, 
  TrendingUp, 
  Users, 
  MessageCircle, 
  Heart, 
  Clock,
  DollarSign,
  Activity
} from 'lucide-react'

const analyticsData = [
  {
    title: 'Total Conversations',
    value: '1,247',
    change: '+23%',
    icon: MessageCircle,
    color: 'text-blue-600',
    bgColor: 'bg-blue-50'
  },
  {
    title: 'Prayer Requests',
    value: '89',
    change: '+12%',
    icon: Users,
    color: 'text-green-600',
    bgColor: 'bg-green-50'
  },
  {
    title: 'Donations Processed',
    value: '$12,450',
    change: '+18%',
    icon: DollarSign,
    color: 'text-red-600',
    bgColor: 'bg-red-50'
  },
  {
    title: 'Avg Response Time',
    value: '1.2s',
    change: '-8%',
    icon: Clock,
    color: 'text-purple-600',
    bgColor: 'bg-purple-50'
  }
]

export function AnalyticsDashboard() {
  return (
    <div className="space-y-8">
      {/* Key Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {analyticsData.map((metric) => (
          <Card key={metric.title} className="ministry-card">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div className="space-y-2">
                  <p className="text-sm font-medium text-slate-600">{metric.title}</p>
                  <p className="text-3xl font-bold text-slate-900">{metric.value}</p>
                  <div className="flex items-center gap-1">
                    <TrendingUp className="w-3 h-3 text-green-600" />
                    <span className="text-sm font-medium text-green-600">{metric.change}</span>
                    <span className="text-sm text-slate-500">vs last month</span>
                  </div>
                </div>
                <div className={`p-3 rounded-xl ${metric.bgColor}`}>
                  <metric.icon className={`w-6 h-6 ${metric.color}`} />
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Charts and detailed analytics would go here */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card className="ministry-card">
          <CardHeader>
            <CardTitle>Conversation Trends</CardTitle>
            <CardDescription>Daily conversation volume over the past 30 days</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="h-64 flex items-center justify-center text-slate-500">
              Chart visualization would be implemented here
            </div>
          </CardContent>
        </Card>

        <Card className="ministry-card">
          <CardHeader>
            <CardTitle>Top Topics</CardTitle>
            <CardDescription>Most frequently discussed topics this month</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {[
                { topic: 'Prayer Requests', count: 156, percentage: 35 },
                { topic: 'Service Information', count: 89, percentage: 20 },
                { topic: 'Donation Questions', count: 67, percentage: 15 },
                { topic: 'Bible Study', count: 45, percentage: 10 }
              ].map((item) => (
                <div key={item.topic} className="flex items-center justify-between">
                  <span className="text-sm font-medium text-slate-900">{item.topic}</span>
                  <div className="flex items-center gap-2">
                    <span className="text-sm text-slate-500">{item.count}</span>
                    <Badge variant="secondary">{item.percentage}%</Badge>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
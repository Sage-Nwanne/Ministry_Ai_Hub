'use client'

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { 
  MessageCircle, 
  Heart, 
  FileText, 
  Users, 
  AlertTriangle,
  CheckCircle,
  Clock
} from 'lucide-react'

const activities = [
  {
    id: 1,
    type: 'prayer',
    title: 'New prayer request received',
    description: 'Sarah M. submitted a prayer request for healing',
    time: '2 minutes ago',
    status: 'new',
    icon: Users,
    color: 'text-blue-600',
    bgColor: 'bg-blue-50'
  },
  {
    id: 2,
    type: 'donation',
    title: 'Thank you message sent',
    description: 'Personalized gratitude sent to John D. for $250 donation',
    time: '15 minutes ago',
    status: 'completed',
    icon: Heart,
    color: 'text-green-600',
    bgColor: 'bg-green-50'
  },
  {
    id: 3,
    type: 'sermon',
    title: 'Sermon transcript processed',
    description: 'Sunday service "Faith in Action" transcript completed',
    time: '1 hour ago',
    status: 'completed',
    icon: FileText,
    color: 'text-purple-600',
    bgColor: 'bg-purple-50'
  },
  {
    id: 4,
    type: 'escalation',
    title: 'Message escalated to pastoral team',
    description: 'Sensitive conversation requiring human intervention',
    time: '2 hours ago',
    status: 'pending',
    icon: AlertTriangle,
    color: 'text-yellow-600',
    bgColor: 'bg-yellow-50'
  },
  {
    id: 5,
    type: 'conversation',
    title: 'AI conversation completed',
    description: 'Member inquiry about Bible study schedule resolved',
    time: '3 hours ago',
    status: 'completed',
    icon: MessageCircle,
    color: 'text-blue-600',
    bgColor: 'bg-blue-50'
  }
]

export function ActivityFeed() {
  return (
    <div className="space-y-6">
      <Card className="ministry-card">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Clock className="w-5 h-5" />
            Live Activity Feed
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {activities.map((activity) => (
              <div key={activity.id} className="flex items-start gap-4 p-4 bg-slate-50 rounded-xl hover:bg-slate-100 transition-colors">
                <div className={`p-2 rounded-lg ${activity.bgColor}`}>
                  <activity.icon className={`w-5 h-5 ${activity.color}`} />
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 mb-1">
                    <h3 className="text-sm font-semibold text-slate-900">{activity.title}</h3>
                    <Badge 
                      variant={activity.status === 'completed' ? 'default' : activity.status === 'pending' ? 'secondary' : 'outline'}
                      className="text-xs"
                    >
                      {activity.status}
                    </Badge>
                  </div>
                  <p className="text-sm text-slate-600 mb-2">{activity.description}</p>
                  <p className="text-xs text-slate-500">{activity.time}</p>
                </div>
                {activity.status === 'pending' && (
                  <Button size="sm" variant="outline" className="text-xs">
                    Review
                  </Button>
                )}
              </div>
            ))}
          </div>
          <div className="pt-4 border-t border-slate-200 mt-6">
            <Button variant="outline" className="w-full ghost-button">
              Load More Activity
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
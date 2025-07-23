import { ActivityFeed } from '@/components/activity/ActivityFeed'

export default function ActivityPage() {
  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Recent Activity</h1>
        <p className="text-gray-600">Track all ministry interactions and system events in real-time</p>
      </div>
      <ActivityFeed />
    </div>
  )
}
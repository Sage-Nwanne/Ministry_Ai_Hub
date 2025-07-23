import { AnalyticsDashboard } from '@/components/analytics/AnalyticsDashboard'

export default function AnalyticsPage() {
  return (
    <div className="max-w-7xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Ministry Analytics</h1>
        <p className="text-gray-600">Comprehensive insights into your ministry's digital engagement and effectiveness</p>
      </div>
      <AnalyticsDashboard />
    </div>
  )
}
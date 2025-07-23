import { DonationWindow } from '@/components/donations/DonationWindow'

export default function DonationsPage() {
  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-gray-900">Stewardship Companion</h1>
        <p className="text-gray-600">AI-powered donation engagement and stewardship support</p>
      </div>
      <DonationWindow />
    </div>
  )
}

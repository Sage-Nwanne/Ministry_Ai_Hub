import { HeroSection } from '@/components/home/HeroSection'
import { AboutSection } from '@/components/home/AboutSection'
import { FeaturesSection } from '@/components/home/FeaturesSection'
import { CTASection } from '@/components/home/CTASection'

export default function Home() {
  return (
    <main className="min-h-screen">
      <HeroSection />
      <AboutSection />
      <FeaturesSection />
      <CTASection />
    </main>
  )
}

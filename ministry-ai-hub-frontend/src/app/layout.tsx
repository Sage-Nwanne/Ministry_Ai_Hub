import type { Metadata } from 'next'
import { Inter, Playfair_Display } from 'next/font/google'
import './globals.css'
import { SWRProvider } from '@/components/providers/SWRProvider'
import { Navbar } from '@/components/layout/Navbar'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

const playfair = Playfair_Display({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-playfair',
})

export const metadata: Metadata = {
  title: 'Ministry AI Hub - Digital Ministry Platform',
  description: 'Professional AI-driven ministry communication system with inbound processing and donation engagement',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={`${inter.variable} ${playfair.variable}`}>
      <body className={`${inter.className} antialiased`}>
        <SWRProvider>
          <Navbar />
          <main className="min-h-screen">
            {children}
          </main>
        </SWRProvider>
      </body>
    </html>
  )
}

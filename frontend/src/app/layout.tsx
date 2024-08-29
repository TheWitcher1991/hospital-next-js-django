import type { Metadata } from 'next'
import { Jost } from 'next/font/google'
import '@mdi/font/css/materialdesignicons.css'
import '@/shared/css/global.css'
import { ReactNode } from 'react'
import WithProviders from '@/providers'
import Footer from '@/widgets/footer'
import Header from '@/widgets/header'
import { Root } from '@/shared/ui'

const inter = Jost({ subsets: ['latin'] })

export const metadata: Metadata = {
	title: 'СМИС',
	description: "Fullstack application of the polyclinic registrar's office",
	robots: 'index, follow',
}

export default function RootLayout({
	children,
}: Readonly<{
	children: ReactNode
}>) {
	return (
		<html lang="ru" dir="ltr" theme="light">
			<body className={inter.className}>
				<WithProviders>
					<Root>
						<Header />
						{children}
						<Footer />
					</Root>
				</WithProviders>
			</body>
		</html>
	)
}

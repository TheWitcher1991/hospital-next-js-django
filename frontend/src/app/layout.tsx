import { ReactNode } from 'react'
import type { Metadata } from 'next'
import { Jost } from 'next/font/google'

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
		<html lang='ru' dir='ltr' theme='light'>
			<body className={inter.className}>{children}</body>
		</html>
	)
}

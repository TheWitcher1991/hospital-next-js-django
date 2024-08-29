import { ReactNode } from 'react'
import { Container } from '@/shared/ui'

export default function AuthLayout({ children }: { children: ReactNode }) {
	return (
		<Container>
			<section>{children}</section>
		</Container>
	)
}

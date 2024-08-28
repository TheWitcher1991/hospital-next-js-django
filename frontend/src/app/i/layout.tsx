'use client'

import { ReactNode, useEffect } from 'react'
import { useCheckAuth } from '@/models/account'
import { useRouter } from 'next/navigation'

export const Layout = ({ children }: { children: ReactNode }) => {
	const { isAuthenticated } = useCheckAuth()
	const { replace } = useRouter()

	useEffect(() => {
		if (!isAuthenticated) {
			replace('/login')
		}
	}, [isAuthenticated, replace])

	return <>{children}</>
}

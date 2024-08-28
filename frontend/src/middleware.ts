import { NextRequest, NextResponse } from 'next/server'
import { RootState, store } from '@/store'

export function middleware(request: NextRequest) {
	const auth =
		(store().getState() as RootState).account?.isAuthenticated || false

	if (request.nextUrl.pathname.startsWith('/i')) {
		if (!auth) {
			return NextResponse.redirect(new URL('/login', request.url))
		}
	}

	if (request.nextUrl.pathname.startsWith('/auth')) {
		if (auth) {
			return NextResponse.redirect(new URL('/', request.url))
		}
	}

	return NextResponse.next()
}

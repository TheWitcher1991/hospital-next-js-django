import { NextRequest, NextResponse } from 'next/server'
import store from '@/store'

export function middleware(request: NextRequest) {
	const auth = store.getState().account?.isAuthenticated || false

	if (request.nextUrl.pathname === '/')
		if (auth) return NextResponse.redirect(new URL('/i', request.url))

	if (
		request.nextUrl.pathname.includes('login') ||
		request.nextUrl.pathname.includes('signup')
	)
		if (auth) return NextResponse.redirect(new URL('/', request.url))

	if (request.nextUrl.pathname.startsWith('/i'))
		if (!auth) return NextResponse.redirect(new URL('/login', request.url))

	return NextResponse.next()
}

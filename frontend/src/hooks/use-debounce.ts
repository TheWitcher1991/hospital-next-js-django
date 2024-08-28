'use client'

import { useCallback, useRef } from 'react'

export const useDebounce = <T extends (...args: never[]) => ReturnType<T>>(
	fn: T,
	delay = 500,
) => {
	const timer = useRef<ReturnType<typeof setTimeout> | null>(null)

	return useCallback(
		(...args: any) => {
			if (timer.current) clearTimeout(timer.current)

			timer.current = setTimeout(() => {
				fn.apply(this, args)
			}, delay)
		},
		[fn, delay],
	)
}

'use client'

import { FC, PropsWithChildren } from 'react'
import NextProgressBar from 'nextjs-progressbar'

const WithProgressBar: FC<PropsWithChildren> = ({ children }) => {
	return (
		<>
			<NextProgressBar
				color={'#000'}
				startPosition={0.3}
				stopDelayMs={200}
				height={3}
			/>

			{children}
		</>
	)
}

export default WithProgressBar

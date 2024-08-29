import { forwardRef, PropsWithChildren } from 'react'
import styles from './index.module.css'

export const Relative = forwardRef<HTMLDivElement, PropsWithChildren>(
	({ children }, ref) => (
		<div ref={ref} className={styles.relative}>
			{children}
		</div>
	),
)

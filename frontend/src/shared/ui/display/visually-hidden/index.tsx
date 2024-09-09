import { FC, PropsWithChildren } from 'react'
import styles from './index.module.css'

export const VisuallyHidden: FC<PropsWithChildren> = ({ children }) => {
	return (
		<div aria-hidden className={styles.visual__hidden}>
			{children}
		</div>
	)
}

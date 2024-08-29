import { FC, PropsWithChildren } from 'react'
import styles from './index.module.css'

export const Root: FC<PropsWithChildren> = ({ children }) => {
	return (
		<main className={styles.root} role={'main'}>
			{children}
		</main>
	)
}

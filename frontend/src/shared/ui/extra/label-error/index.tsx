import { FC, PropsWithChildren } from 'react'
import styles from './index.module.css'

export const LabelError: FC<PropsWithChildren> = ({ children }) => {
	return <div className={styles.label__error}>{children}</div>
}

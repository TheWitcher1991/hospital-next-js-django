import { FC } from 'react'
import styles from './index.module.css'

export interface SpacingProps {
	v?: 'xss' | 'xs' | 's' | 'm' | 'ml' | 'l' | 'xl' | 'xxl'
}

export const Spacing: FC<SpacingProps> = ({ v = 'm' }) => {
	const spacingStyle = {
		m: styles.spacing,
		xs: styles.spacing__xs,
		xss: styles.spacing__xss,
		s: styles.spacing__s,
		ml: styles.spacing__ml,
		l: styles.spacing__l,
		xl: styles.spacing__xl,
	}

	return <div className={spacingStyle[v]}></div>
}

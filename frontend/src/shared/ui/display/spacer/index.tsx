import { FC } from 'react'
import styles from './index.module.css'

export interface SpacerProps {
	v?: 'xss' | 'xs' | 's' | 'm' | 'ml' | 'l' | 'xl' | 'xxl'
}

export const Spacer: FC<SpacerProps> = ({ v = 'm' }) => {
	const styleSpacer = {
		m: styles.spacer,
		xss: styles.spacer__xss,
		xs: styles.spacer__xs,
		s: styles.spacer__s,
		ml: styles.spacer__ml,
		l: styles.spacer__l,
		xl: styles.spacer__xl,
		xxl: styles.spacer__xxl,
	}

	return <span className={styleSpacer[v]}></span>
}

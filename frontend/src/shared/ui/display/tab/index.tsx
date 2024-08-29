import { FC } from 'react'
import styles from './index.module.css'

export interface TabProps {
	v?: 'xss' | 'xs' | 's' | 'm' | 'ml' | 'l' | 'xl' | 'xxl'
}

export const Tab: FC<TabProps> = ({ v = 'm' }) => {
	const styleTab = {
		m: styles.tab,
		xss: styles.tab__xss,
		xs: styles.tab__xs,
		s: styles.tab__s,
		ml: styles.tab__ml,
		l: styles.tab__l,
		xl: styles.tab__xl,
		xxl: styles.tab__xxl,
	}

	return <span className={styleTab[v]}></span>
}
